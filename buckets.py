import boto3

BUCKET_NAME = "green-vibe"

s3 = boto3.client("s3")

#list  all buckets
buckets_resp = s3.list_buckets()
for bucket in buckets_resp["Buckets"]:
    print(bucket["Name"])
    
##list objects in a bucket

response = s3.list_objects_v2(Bucket=BUCKET_NAME)
#print(response["Contents"])
for content in response["Contents"]:
    print(content["Key"])
    
    
#Uploading a file to a bucket
with open ("./requirements.txt","rb") as f:
    s3.upload_fileobj(f,BUCKET_NAME,"new_requirements.txt")

##download a file 
s3.download_file(BUCKET_NAME,"beach.jpg","beach.jpg")

##get limmited time url from bucket
url = s3.generate_presigned_url(
    "get_object",
    Params={"Bucket":BUCKET_NAME,"Key":"beach.jpg"},
    ExpiresIn=10
    )
print(url)

##create a New bucket
bucket_location = s3.create_bucket(ACL="public-read",Bucket="new-destination-bucket-77")
print(bucket_location)

##copy objects between buckets
s3.copy_object(
    ACL="public-read",
    Bucket="new-destination-bucket-77",
    CopySource=f"/{BUCKET_NAME}/beach.jpg",
    Key="Copierbeach.jpg"
)

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
        
#number_buckets(5)