# Stocks data Function
import requests
from bs4 import BeautifulSoup
from io import StringIO
import pandas as pd
import os
import pandas as pd
import json
import boto3
from datetime import datetime

s3 = boto3.client('s3',region_name='us-east-2')

# url to the yahoo page
url = "https://ca.finance.yahoo.com/quote/CADUSD%3DX?p=CADUSD%3DX"
# uBeautifulSoup
stocks_page = requests.get(url).text
soup = BeautifulSoup(stocks_page, "html.parser")
# get first table in dataframe
df = pd.read_html(StringIO(str(soup.find_all("table")[0])), flavor="bs4")[0]
# change column name
df = df.rename(columns={0: "a", 1: "b"})
# create empty list and store the values
Previous_Close = []
Open = []
Bid = []
Previous_Close.append(df[df.a == "Previous Close"].loc[0]["b"])
Open.append(df[df.a == "Open"].loc[1]["b"])
Bid.append(df[df.a == "Bid"].loc[2]["b"])
# repeat the same for the second table
df1 = pd.read_html(StringIO(str(soup.find_all("table")[1])), flavor="bs4")[0]
df1 = df1.rename(columns={0: "a", 1: "b"})
Days_Range = []
Range_52_Week = []
Ask = []
Days_Range.append(df1[df1.a == "Day's Range"].loc[0]["b"])
Range_52_Week.append(df1[df1.a == "52 Week Range"].loc[1]["b"])
Ask.append(df1[df1.a == "Ask"].loc[2]["b"])
# use the lists to create the new data frame and store all the values in 1 row
d = {
    "Index": [soup.title.string[: soup.title.string.index(")")].split("(")[1]],
    "Previous_Close": Previous_Close,
    "Open": Open,
    "Bid": Bid,
    "Days_Range": Days_Range,
    "Range_52_Week": Range_52_Week,
    "Ask": Ask,
    "Time": [pd.Timestamp.now().strftime("%Y-%m-%d %H-%M-%S")],
}
df2 = pd.DataFrame(data=d)
# df2.set_index('Title', inplace=True)

bucket = "bucketName"

# pull data

fileName = 'stocks' + '.csv'
csv_buffer = StringIO()
df2.to_csv(csv_buffer, header=True, index=False)

uploadByteStream = csv_buffer.getvalue()

s3.put_object(Body=uploadByteStream, Bucket=bucket, Key=fileName)

print('Put Complete')