# Real-time Named Entity Recognition with Spark Streaming, Kafka, Elasticsearch, and Kibana

## Overview

This project implements a Spark Streaming application in Python that analyzes real-time data from the NewsAPI, focusing on 20 headlines per minute. The application extracts named entities and sends their counts to Kafka for further processing.

## Setup

1. **Download Dependencies:**
   - Kafka: [Kafka Downloads](https://kafka.apache.org/downloads)
   - Spark: [Spark Downloads](https://spark.apache.org/downloads.html)
   - Logstash, Elasticsearch, Kibana:
     - Logstash: [Logstash Downloads](https://www.elastic.co/downloads/logstash)
     - Elasticsearch: [Elasticsearch Downloads](https://www.elastic.co/downloads/elasticsearch)
     - Kibana: [Kibana Downloads](https://www.elastic.co/downloads/kibana)

2. **Start Kafka Server:**
   - Navigate to the Kafka folder and run Zookeeper and Kafka servers:
     ```bash
     bin/zookeeper-server-start.sh config/zookeeper.properties
     bin/kafka-server-start.sh config/server.properties
     ```

3. **Create Kafka Topics:**
   ```bash
   bin/kafka-topics.sh --create --topic input_topic --partitions 3 --replication-factor 1 --bootstrap-server localhost:9092
   bin/kafka-topics.sh --create --topic output_topic --partitions 3 --replication-factor 1 --bootstrap-server localhost:9092

### Step 4: Run Spark Streaming App

1. Navigate to the Q1 folder and run the NewsAPI streaming application:
    ```bash
    python3 news-api.py
    ```

2. Navigate to the Spark folder and submit the Spark Streaming job:
    ```bash
    bin/spark-submit --packages org.apache.spark:spark-streaming-kafka-0-10_2.12:3.1.2,org.apache.spark:spark-sql-kafka-0-10_2.12:3.1.2 /path/to/spark_streaming.py
    ```

### Step 5: Configure Logstash

1. Copy `configuration_file.conf` from the Q1 folder to Logstash's config folder.

2. Run Logstash:
    ```bash
    bin/logstash -f ./config/configuration_file.conf --config.reload.automatic
    ```

### Step 6: Start Elasticsearch

1. Navigate to the Elasticsearch bin folder and run:
    ```bash
    ./elasticsearch
    ```

### Step 7: Start Kibana

1. Navigate to the Kibana bin folder and run:
    ```bash
    ./kibana
    ```
### Step 8: Configure Kibana Data Views

1. In Kibana, go to:
    - Menu -> Stack Management -> Kibana -> Data Views -> Create Data Views
2. Enter the index pattern as `final` and save the data view to Kibana.

### Step 9: Configure Kibana Index Patterns

1. Click "Add field" for both dataKey and dataValue.
   
    a. For dataKey:
        ```javascript
        // JavaScript code for dataKey
        ```

    b. For dataValue:
        ```javascript
        // JavaScript code for dataValue
        ```

### Step 10: Create Kibana Visualization

1. Navigate to Main Menu -> Create Dashboard -> Create Visualization.
2. Select `final*` as the data view and choose "Bar Vertical Stacked."
3. Create a dashboard using dataKey as the Horizontal-axis and dataValue as the Vertical-axis.

### Step 11: Visualize Data

1. The data can now be visualized in the form of a bar graph on the Kibana dashboard.

