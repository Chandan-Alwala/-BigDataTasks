# Movie Search Engine using PySpark

## Overview

This Jupyter Notebook implements a movie search engine using PySpark on Databricks. The search engine utilizes the tf-idf technique for document-term representation and cosine similarity for query relevance assessment. The dataset comprises 42k movie summaries obtained from the Carnegie Movie Summary Corpus.

## Notebook Structure

- **`Movie_Search_Engine.ipynb`**: Jupyter Notebook containing the PySpark code.
  
## Instructions

1. **Setup Databricks Cluster:**
   - Create a Databricks cluster.
   - Upload the notebook to Databricks.

2. **Upload Data:**
   - Upload the `plot_summaries.txt`, `movie_metadata.tsv`, `singletermsearch-5.txt`, and `multitermsearch-2.txt` files to Databricks.

3. **Run the Notebook:**
   - Execute the cells in the notebook in order.

4. **View Results:**
   - Results will be displayed within the notebook.
     - For a single term query, observe the top 10 documents with the highest tf-idf values.
     - For a multi-term query, explore the top 10 documents with the highest cosine similarity.

## Dependencies

- PySpark
- NLTK

## File Descriptions

- **`plot_summaries.txt`**: Dataset containing 42k movie plot summaries.
- **`movie_metadata.tsv`**: Movie metadata file.
- **`singletermsearch-5.txt`**: File containing single-term search queries.
- **`multitermsearch-2.txt`**: File containing multi-term search queries.

## References

- [NLTK Stopwords](https://www.nltk.org/nltk_data/)
- [Cosine Similarity Explanation](https://courses.cs.washington.edu/courses/cse573/12sp/lectures/17-ir.pdf)

## Note

- Make sure to adjust file paths in the code according to the location of the uploaded files in your Databricks environment.

