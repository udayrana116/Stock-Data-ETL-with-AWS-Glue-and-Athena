# Stock-Data-ETL-with-AWS-Glue-and-Athena
This project demonstrates an end-to-end data pipeline for scraping stock market data from the web, transforming it using AWS Glue, and analyzing it using Amazon Athena. It leverages AWS Glue’s Jobs and Crawlers to automate the ETL process and uses Athena to perform queries on the transformed data for further analysis.
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

