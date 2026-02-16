import boto3
from botocore.exceptions import ClientError

# Create session with specific profile
session = boto3.Session(profile_name='watchelmtraining')

# Test 1: Check current identity
print("=== Current Identity ===")
sts_client = session.client('sts')
identity = sts_client.get_caller_identity()
print(f"Current role: {identity['Arn']}")
print(f"Account: {identity['Account']}")

# Test 2: Test basic S3 access
print("\n=== S3 Access Test ===")
s3_client = session.client('s3')

try:
    # Check if we can list buckets
    response = s3_client.list_buckets()
    print(f"✓ Can list buckets: Found {len(response['Buckets'])} buckets")
    
    # Check if our specific bucket exists
    bucket_found = any(bucket['Name'] == 'spark.demo.data' for bucket in response['Buckets'])
    print(f"✓ spark.demo.data bucket found: {bucket_found}")
    
except ClientError as e:
    print(f"✗ Cannot list buckets: {e}")

# Test 3: Test specific bucket access
print("\n=== Bucket-Specific Access Test ===")
try:
    # Try to get bucket location
    location = s3_client.get_bucket_location(Bucket='spark.demo.data')
    region = location.get('LocationConstraint') or 'us-east-1'
    print(f"✓ Bucket region: {region}")
    
    # Try to list objects
    response = s3_client.list_objects_v2(Bucket='spark.demo.data', MaxKeys=5)
    if 'Contents' in response:
        print(f"✓ Can list objects: Found {len(response['Contents'])} objects")
        for obj in response['Contents'][:3]:
            print(f"  - {obj['Key']} ({obj['Size']} bytes)")
    else:
        print("✓ Bucket is accessible but empty")
        
except ClientError as e:
    print(f"✗ Cannot access bucket: {e}")
    print(f"Error code: {e.response['Error']['Code']}")
    print(f"Error message: {e.response['Error']['Message']}")

# Test 4: Test writing to bucket
print("\n=== Write Access Test ===")
try:
    test_key = 'glue-test-file.txt'
    s3_client.put_object(
        Bucket='spark.demo.data',
        Key=test_key,
        Body=b'Test from Glue notebook'
    )
    print(f"✓ Can write to bucket: Created {test_key}")
    
    # Clean up
    s3_client.delete_object(Bucket='spark.demo.data', Key=test_key)
    print(f"✓ Can delete from bucket: Removed {test_key}")
    
except ClientError as e:
    print(f"✗ Cannot write to bucket: {e}")
    print(f"Error code: {e.response['Error']['Code']}")
    print(f"Error message: {e.response['Error']['Message']}")
