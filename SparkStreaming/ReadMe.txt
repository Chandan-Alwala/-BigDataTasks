Step 1: Go to the Q1 folder in the submission 

Step 2: Download Kafka from web using this link and extract it to a folder(lets say Desktop)
	https://kafka.apache.org/downloads

Step 3: Download Apache Spark using this link and extract it to a folder(lets say Desktop)
	https://spark.apache.org/downloads.html

Step 4: Navigate to Kafka folder which we downloaded and extracted in step2 and Run Kafka server using the below commands:

	bin/zookeeper-server-start.sh config/zookeeper.properties
	
	bin/kafka-server-start.sh config/server.properties

Step 5: Create a topic called input_topic using this command
	
	bin/kafka-topics.sh --create --topic input_topic --partitions 3 --replication-	factor 1 --bootstrap-server localhost:9092

Step 6: Create a topic called output_topic using this command
	
	bin/kafka-topics.sh --create --topic output_topic --partitions 3 --replication-factor 1 --bootstrap-server localhost:9092

Step 7: Navigate to Q1 folder. Run news-api.py file (python3 news-api.py)

Step 8: Navigate to spark folder which we downloaded and extracted in step3

Step 9: Run spark_streaming.py code using this command
	
	bin/spark-submit --packages org.apache.spark:spark-streaming-kafka-0-10_2.12:3.1.2,org.apache.spark:spark-sql-kafka-0-10_2.12:3.1.2 /Users/Chandan/BigData/HW3/spark_streaming.py(Replace this path with the absolute path in your pc)

Step 10: Download logstash , elastic search , kibana from the following links
	
	https://www.elastic.co/downloads/logstash
	https://www.elastic.co/downloads/elasticsearch
	https://www.elastic.co/downloads/kibana

Step 11: Navigate to logstash folder and go to config folder.copy and paste the file configuration_file.conf (present in Q1 folder) into logstash config folder.

Step 12: Run logstash using this command

	bin/logstash -f ./config/lconfiguration_file.conf --config.reload.automatic

Step 13: navigate to bin in elastic search folder and run this command
	
	./elasticsearch
	
	Follow the steps that are shown in terminal

Step 14: navigate to bin in kibana folder and run this command

	./kibana

	Follow the steps that are shown in terminal

Step 15: In kibana navigate

	Menu->Stack Management-> Kibana -> Data Views -> Create Data Views
	Enter index pattern as final and create save data view to kibana

Step 16: a) Click Add field
	
	Enter name as dataKey : 
	Set value as this code:
	
def message = doc['message.keyword'].value;
if (message != null) {
    int colonIndex = message.indexOf(':');
    if (colonIndex > 0) {
        emit(message.substring(0, colonIndex));
        return;
    }
}
emit("");

	b) Click Add field

	Enter name as dataValue:

def message = doc['message.keyword'].value;
if (message != null) {
    int colonIndex = message.indexOf(':');
    if (colonIndex >= 0) {
        emit(message.substring(colonIndex + 1));
        return;
    }
}
emit("");

Step 17: Navigate

	Main Menu -> Create Dashboard -> Create Visualization -> Select final* as data view and Bar Vertical Stacked 
	Create dashboard using dataKey as Horizontal-axis and dataValue as Vertical-axis

Step 18: Now we can visualize the data in form of bar graph
