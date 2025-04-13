import boto3

# Initialize S3 client
s3 = boto3.client('s3')

# List all buckets
buckets = s3.list_buckets()['Buckets']
print("✅ Your S3 Buckets:")
for bucket in buckets:
    print(f"- {bucket['Name']}")

# Count objects in a specified bucket
bucket_name = 'devops-rishabh-intern-bucket'  # replace if nee>
response = s3.list_objects_v2(Bucket=bucket_name)

object_count = response.get('KeyCount', 0)
print(f"\n📦 Total objects in '{bucket_name}': {object_count}")