# Stock-Data-ETL-with-AWS-Glue-and-Athena
This project demonstrates an end-to-end data pipeline for scraping stock market data from the web, transforming it using AWS Glue, and analyzing it using Amazon Athena. It leverages AWS Glue’s Jobs and Crawlers to automate the ETL process and uses Athena to perform queries on the transformed data for further analysis.

![1](https://github.com/user-attachments/assets/2b46c12b-95be-4c44-bf0e-f8d59d8d60dc)


Key Features:
- Web Scraping: Scrapes real-time stock market data from publicly available sources using Python.
- Data Processing with AWS Glue: Uses AWS Glue Jobs to automate the extraction, transformation, and loading (ETL) of the scraped data into an S3 bucket. Glue Crawlers are configured to automatically infer the schema of the data and prepare it for querying.
- Data Storage: Stores the scraped and transformed stock data in an Amazon S3 bucket for scalable and secure storage.
- Data Analysis with Athena: Utilizes Amazon Athena to run SQL queries on the transformed data, enabling fast, serverless querying of large datasets.
- Automation: The pipeline is designed to be automated, ensuring regular scraping and updating of stock data for continuous analysis.
- Cost-Efficient: Leverages AWS's serverless offerings (Glue, S3, and Athena), ensuring a scalable and cost-effective solution.
Technologies Used:
- AWS Glue (Jobs, Crawlers)
- Amazon S3
- Amazon Athena
- Python for web scraping
- SQL for data analysis

How It Works:
1.	Data Collection: Python scripts scrape stock data from the web, including key metrics like prices, volumes, and historical performance.
2.	ETL with AWS Glue: AWS Glue jobs are triggered to clean and transform the scraped data into a structured format. Glue Crawlers automatically detect the schema of the data and register it in the Glue Data Catalog.
3.	Data Storage: The processed data is stored in Amazon S3 as structured files (e.g., Parquet or CSV).
4.	Data Analysis: Amazon Athena is used to run SQL queries on the data stored in S3, enabling quick insights and analysis without provisioning any infrastructure.

Potential Use Cases:
- Real-time stock market analysis
- Building stock prediction models
- Portfolio performance monitoring
- Custom stock alerts and dashboards

This project serves as a scalable and automated approach to collect, transform, and analyze stock market data using AWS’s serverless technologies. It's ideal for those looking to experiment with cloud-based ETL processes and perform data analytics at scale.

Steps to follow:-

## IAM role for AWS Glue
Need to grant IAM role permissions that AWS Glue can assume when calling other services .
This document link can be followed to set it up:-
https://docs.aws.amazon.com/glue/latest/dg/create-an-iam-role.html

## AWS Glue Job
1. Select "Script editor", choose "Python shell" engine and start fresh to create script.
2. In the Job details tab chosse the above created IAM role and save it.
3. Take the "Stocks.py" from the script folder and copy-paste it's content in this new created job.
4. In the script update the bucket name and file as per your preference.
5. Running this job will output csv file to the s3 bucket folder.

## AWS Glue Data Catalog
1. Go to Databses in AWS Glue.
2. Select Add database.
3. Provide a name & Description to it and select Create database.

## AWS Glue Crawler
1. Go to Crawlers in AWS Glue.
2. Select Create crawler.
3. Provide some name for this crawler.
4. Keep data source added to "Not yet" and select "Add a data source".
5. In the S3 path section choose the file output by the script and select Add on S3 data source and select next
6. Select the IAM role created for Glue tasks.
7. In database select the one created above.
8. For the crawler schedule leave it to "On demand" for now.  

## Amazon Athena
1. Before using Athena, create a folder in your create s3 bucket with name "athena_results".
2. This will be to store the athena results as an object.
3. Go to Amazon Athena and select Query esitor tabs and go to settings.
4. Select manage under Query result and encryption settings and select the folder "athena_results" under Location of query result.
5. Now we are ready to query the crawled tables.
6. Under data source choose "AwsDataCatalog".
7. And under Database se;ect the one we created above.
8. Now we can see the tables crawled under Tables and we can query the Stocks data we pulled.

## Workflow
To orchestrate the pipeline we can set the triggers under Workflows adn schedule the AWS Glue Jobs and crawler.


