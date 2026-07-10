import boto3
import json
import logging

logging.basicConfig(level=logging.DEBUG)
s3 = boto3.client('s3')

try:
    response = s3.list_buckets()
    print("=== information verbose ===")
    print(f"number buckets: {len(response['buckets'])}")
    print(f"Owner: {response['Owner']['DisplayName']} ({response['Owner']['ID']})")
except Exception as e:
    print(f"Error {str(e)}")