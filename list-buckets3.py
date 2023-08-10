import boto3

# Retrieve the list of existing buckets
s3 = boto3.client('s3', 'us-east-1')
response = s3.list_buckets()

# Output the bucket names
print('f Files in buckets')
for bucket in response['Buckets']:
    	bucket_name = bucket['Name']
    	print(bucket_name)

    	object_list = s3.list_objects_v2(Bucket = bucket_name)
    	print(f'Files in bucket {bucket_name}:')
    	for obj in object_list.get('Contents', []):
            	print(obj['Key'])

