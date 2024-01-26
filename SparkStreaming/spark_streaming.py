from pyspark.sql import SparkSession
from pyspark.sql.functions import udf, explode, window, col
from pyspark.sql.types import ArrayType, StringType
import spacy

nlp = spacy.load("en_core_web_sm")

def named_entity_recognition(text):
    doc = nlp(text)
    return [ent.text for ent in doc.ents]

ner_udf = udf(named_entity_recognition, ArrayType(StringType()))

spark = SparkSession.builder \
    .appName('myAppName') \
    .config('spark.eventLog.enabled', 'true') \
    .config('spark.eventLog.dir', '/Users/alwala/Downloads/Hw3_logs') \
    .config('spark.eventLog.logLevel', 'WARN') \
    .getOrCreate()

kafka_topic = "input_topic_1"
output_topic = "output_topic_1"

kafka_df = spark.readStream \
    .format("kafka") \
    .option("kafka.bootstrap.servers", "localhost:9092") \
    .option("subscribe", kafka_topic) \
    .option("failOnDataLoss", "false") \
    .load() \
    .selectExpr("CAST(value AS STRING)", "timestamp")


kafka_df = kafka_df.withWatermark("timestamp", "10 minutes")

kafka_df = kafka_df.withColumn("named_entities", ner_udf(kafka_df.value))

kafka_df = kafka_df.select(explode(col("named_entities")).alias("named_entity"), "timestamp")

result = kafka_df \
    .groupBy(window(kafka_df.timestamp, "10 minutes"), kafka_df.named_entity) \
    .count()

query = result \
    .selectExpr("CAST(window.start AS STRING) AS key",
                "concat(named_entity, ':', count) AS value") \
    .writeStream \
    .format("kafka") \
    .option("kafka.bootstrap.servers", "localhost:9092") \
    .option("topic", output_topic) \
    .option("checkpointLocation", "/Users/alwala/Downloads/Hw3_logs") \
    .outputMode("update") \
    .start()

query.awaitTermination()
