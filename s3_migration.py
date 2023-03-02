import os
import sys
import time
from dotenv import load_dotenv
from pathlib import Path
from spaces import Client

# Get the access key and secret key from the environment variables

access_key = os.environ['ACCESS_KEY']
secret_key = os.environ['SECRET_KEY']
region_name = os.environ['REGION_NAME']
endpoint_url = os.environ['ENDPOINT_URL']
space_name = os.environ['SPACE_NAME']

# Create a client object

client = Client (access_key, secret_key, region_name, endpoint_url, space_name)

client.list_spaces()

print(
    client.list_spaces(
    string=True
    )
)

# List all the files in the bucket

print(
    client.list_files(
    string=True
    )
)

