from botocore.exceptions import ClientError
import logging
import uuid
import boto3

random_string = str(uuid.uuid4())


def create_bucket(bucket_name, region_name=None):
    print('Creating bucket: ...')
    """Create an S3 bucket in a specified region
    If a region is not specified, the bucket is created in the S3 default
    region (us-east-1).
    :param bucket_name: Bucket to create
    :param region: String region to create bucket in, e.g., 'us-west-2'
    :return: True if bucket created, else False
    """

    # Create bucket
    try:
        if region_name is None:
            s3_client = boto3.client('s3')
            response = s3_client.create_bucket(Bucket=bucket_name)
            print(response)
        else:
            s3_client = boto3.client('s3', region_name=region_name)
            location = {'LocationConstraint': region_name}
            response = s3_client.create_bucket(Bucket=bucket_name,
                                               CreateBucketConfiguration=location)
            print(response)

    except ClientError as e:
        logging.error(e)
        return False
    return True


# Delete a bucket from existing buckets
def delete_bucket(bucket_name, region_name=None):
    print('Deleting bucket: ...')
    try:
        if region_name is None:
            client = boto3.client('s3')
            response = client.delete_bucket(
                Bucket=bucket_name
            )
            print(response)
        else:
            client = boto3.client('s3', region_name=region_name)
            response = client.delete_bucket(
                Bucket=bucket_name, region=region_name
            )
            print(response)
    except ClientError as e:
        logging.error(e)
        return False
    return True


# Retrieve the list of existing buckets
def list_bucket():
    print('List existing buckets: ...')
    client = boto3.client('s3')
    response = client.list_buckets()

    # Output the bucket names
    print('Existing buckets:')
    for bucket in response['Buckets']:
        print(f'  {bucket["Name"]}')


def main():
    bucket_name = 'my-bucket-' + random_string[:13]
    print(bucket_name)

    # create_bucket(bucket_name, "us-west-2")

    # delete_bucket("my-bucket-17a5d733-21ad")

    list_bucket()


if __name__ == '__main__':
    main()
