# Analyzing Social Network Data with Spark GraphX/GraphFrame

## Introduction

This project involves using Spark GraphX/GraphFrame to analyze social network data from a chosen dataset available from the SNAP repository. The goal is to construct a graph and run various queries and algorithms on the graph to derive meaningful insights.

This Google Colab notebook contains code and content related to [https://colab.research.google.com/drive/15mxw4AmSsrTmmAzUdCi6MTddz2f3_LLF?usp=sharing](link). The notebook is designed to be run in Google Colab, a cloud-based platform for executing Python code collaboratively.

## Steps to Reproduce in Google Colab

### 1. Loading Data

- Download the social network dataset from the SNAP repository.
- Define a parser in the notebook to identify and extract relevant fields from the dataset.
- Ensure that the edges are directed. If the dataset contains undirected relationships, convert them into two directed relationships.

### 2. Create Graphs

- Define the edge and vertex structure.
- Create property graphs using GraphX/GraphFrame.

### 3. Running Queries

#### a. Top 5 Nodes with Highest Outdegree

- Use the outDegrees function to find the outdegree of each node.
- Order the result in descending order and limit to the top 5.

#### b. Top 5 Nodes with Highest Indegree

- Use the inDegrees function to find the indegree of each node.
- Order the result in descending order and limit to the top 5.

#### c. PageRank Calculation

- Use the pageRank function to calculate PageRank for each node.
- Order the result in descending order and limit to the top 5.

#### d. Connected Components Algorithm

- Use the connectedComponents function to find connected components.
- Group by components, count the nodes, and order in descending order. Limit to the top 5.

#### e. Triangle Counts Algorithm

- Use the triadCensus function to find triangle counts for each vertex.
- Order the result in descending order and limit to the top 5.

### 4. Output

Ensure to write the output of each query to a file specified by the output parameter.

## Conclusion

This README provides a basic outline of the steps to analyze social network data using Spark GraphX/GraphFrame in Google Colab. Feel free to customize the code based on your specific dataset and requirements.
