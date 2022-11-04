import boto3

def number_buckets(num):
    client = boto3.client('s3')
    buckets = client.list_buckets()
    count = 0
    for bucket in buckets['Buckets']:
        if count<num:
            current_bucket = bucket['Name']
            print(f"Found Bucket: {current_bucket}")
            count+=1
        else:
            return
        
number_buckets(5)