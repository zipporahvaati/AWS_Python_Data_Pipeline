import boto3
import pandas as pd

# Connect to S3
s3 = boto3.client('s3')
bucket = 'zippy-vaati-s3-bucket'  # bucket name
file_key = 'BMW Sales.csv'      # your file name

# Read CSV into pandas
obj = s3.get_object(Bucket=bucket, Key=file_key)
df = pd.read_csv(obj['Body'])

print(df.head(100))
