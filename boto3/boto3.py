import os
import boto3
import shutil


s3_conn = boto3.Session(aws_access_key_id="aws_access_key_id",
                        aws_secret_access_key="aws_secret_access_key")

s3 = s3_conn.resource('s3')

bucket_name = s3.Bucket("bucket")

working_directory = r"С:\Downloads"
#shutil.rmtree(working_directory)



for file in bucket_name.objects.filter(Prefix="production/tiles/"):
    if file.key.endswith(".png"):

        local_file_name = os.path.join(working_directory, file.key.split("//")[-1].replace("/", "_"))

        print(f"Downloading {file.key} to {local_file_name}")
        bucket_name.download_file(file.key, local_file_name)
        print(f"Finished downloading {local_file_name}\n")
