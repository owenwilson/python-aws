import boto3

s3 = boto3.client('s3')
bucket_name = 'python-bucket-s3-dev'
s3.delete_bucket(Bucket=bucket_name)