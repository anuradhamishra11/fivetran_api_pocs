# import boto3

# def extract_data_from_s3():
#     # Code to extract data from S3
#     s3 = boto3.resource('s3')
#     bucket_name = 'annu-bucket-for-fivetran-1'
#     key = '2023-07-06T05-12-51Z_e16b87dd-06f1-4734-87e6-8cc4f4bb9017.parquet'
#     obj = s3.Object(bucket_name, key)
#     data = obj.get()['Body'].read()
#     return data

# a = extract_data_from_s3()
# print(a)

import abc


class Animal:
    def __init__(self, name):
        self.name = name


a = Animal("Anuradha")
print(a)

