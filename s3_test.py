import boto3

# Let's use Amazon S3
s3 = boto3.resource('s3')

# Print out bucket names
for bucket in s3.buckets.all():
    print(bucket.name)

# Upload a new file
data = open('test.png', 'rb')
s3.Bucket('gem.test.gsheets').put_object(Key='test.png', Body=data)
