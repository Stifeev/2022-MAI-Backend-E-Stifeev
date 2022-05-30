# -*- coding: utf-8 -*-

import os
import boto3
from filmapp_main.settings import AWS_ACCESS_KEY_ID,         \
                                  AWS_SECRET_ACCESS_KEY,     \
                                  AWS_STORAGE_BUCKET_NAME,   \
                                  AWS_S3_ENDPOINT_URL

session = boto3.session.Session()
s3_client = session.client(service_name="s3", 
                            aws_access_key_id=AWS_ACCESS_KEY_ID,
                            aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
                            endpoint_url=AWS_S3_ENDPOINT_URL)

content = open("../Обложки/" + os.listdir("../Обложки/")[0], "rb").read()
key = "mai/pic.jpg"
s3_client.put_object(Bucket=AWS_STORAGE_BUCKET_NAME, Key=key, Body=content)
url = s3_client.generate_presigned_url("get_object",
                                        Params={
                                            "Bucket": AWS_STORAGE_BUCKET_NAME,
                                            "Key": key
                                        },
                                        ExpiresIn=3600)
print(url)
