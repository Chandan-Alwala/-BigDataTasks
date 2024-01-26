
# get_ipython().system('pip install nltk')
from pyspark.sql import SparkSession
sc = SparkSession.builder.appName("DataFrames").getOrCreate()

from math import log
import nltk
from nltk.corpus import stopwords
nltk.download('stopwords')
stopwords = set(stopwords.words("english"))

def frequency(x):
    words = x[1]
    l = []
    for s in words:
        if len(s)>2 and s.lower() not in stopwords:
            l.append(((x[0],s.lower()),1))
    return l

def termFrequency(term,plot_summary):
    word_frequencies = plot_summary.filter(lambda x: word in x[1]).map(lambda x: (x[0], x[1][word]))
    return word_frequencies

def idf(term,plot_summary):
    count = plot_summary.filter(lambda x: word in x[0][1]).count()
    if count != 0:
        return log(N/count)
    else: 
        return 1

def tfIdf(term,plot_summary):
    tfValue = plot_summary.filter(lambda x: term in x[0][1]).map(lambda x: (x[0][0], x[1]))
    idfValue = plot_summary.filter(lambda x: term in x[0][1]).count()
    tfIdfValue = tfValue.map(lambda x: (x[0],x[1]*log(N/idfValue)))
    return tfIdfValue

plot_summary = sc.textFile('/FileStore/tables/plot_summaries.txt')
N = plot_summary.count()
print(N)

# Preprocess the data
plot_summary = plot_summary.map(lambda x: x.split('\t'))
plot_summary = plot_summary.map(lambda x: (x[0],x[1].replace(',','').replace('.','').replace('?','').replace('\"','').lower().split(' ')))

plot_summary = plot_summary.flatMap(frequency).reduceByKey(lambda x,y: x+y)

# Read movie metadata into DataFrame
movieDf = sc.read.options(delimiter='\t').csv('/FileStore/tables/movie_metadata.tsv')
movieDf = movieDf.withColumnRenamed("_c2","movieName").withColumnRenamed("_c0","movieId")
headers = ['movieId','tfIdf']

terms = sc.textFile('/FileStore/tables/singletermsearch-5.txt')
print(terms.collect())

terms = terms.collect()
for term in terms:
    term = term.lower()
    tfIdfValue = tfIdf(term,plot_summary)
    topMovies = tfIdfValue.sortBy(lambda x: -1*x[1]).take(10)
    print(term)
    topMoviesRdd = sc.parallelize(topMovies)
    topMoviesDf = topMoviesRdd.toDF(headers)
    result = movieDf.join(topMoviesDf,topMoviesDf.movieId == movieDf.movieId,"inner")
    result.select('movieName','tfIdf').show(truncate = False)

# cosine similarity
search_query = sc.textFile('/FileStore/tables/multitermsearch-2.txt')
print(search_query.collect())

search_query_words = search_query.flatMap(lambda x: x.split(' ')).map(lambda x: (x.lower(),1)).reduceByKey(lambda x,y:x+y).collect()
print(search_query_words)

l = []
idfValues = {}
for x in search_query_words:
    word = x[0]
    idfValue = idf(word,plot_summary)
    idfValues[word] = idfValue
    l.append((word,x[1]*idfValue))
 
searchRdd = sc.parallelize(l)
 
movieRdd = plot_summary.filter(lambda x: x[0][1] in [w[0] for w in search_query_words]).map(lambda x:(x[0][1],(x[0][0],x[1]*idfValues[x[0][1]])))
 
joinedRdd = searchRdd.join(movieRdd)

from math import sqrt
cosineSimilarity = joinedRdd.map(lambda x : (x[1][1][0], (x[1][0] * x[1][1][1], x[1][0] **2, x[1][1][1] **2)))
cosineSimilarity = cosineSimilarity.reduceByKey(lambda x,y : ((x[0] + y[0], x[1] + y[1], x[2] + y[2])))
cosineSimilarity = cosineSimilarity.map(lambda x : (x[0], 1-x[1][0]/(sqrt(x[1][1]) * sqrt(x[1][2]))))

result = cosineSimilarity.sortBy(lambda x: -x[1])


resultDF = result.toDF(["movieId", "cosineSimilarity"])

finalResult = movieDf.join(resultDF,movieDf.movieId == resultDF.movieId, "inner")

finalResult.select('movieName', 'cosineSimilarity').show(10,False)





