import os, uuid
from azure.identity import DefaultAzureCredential
from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient
import time

try:
    print("Azure Blob Storage Python quickstart sample")
    account_url = "https://accountingstorage1.blob.core.windows.net/"
    credential=DefaultAzureCredential(managed_identity_client_id = "be4e963d-7cbd-4f5f-9a42-4bceb00d9ebf")

    # Create the BlobServiceClient object
    while(True):
        blob_service_client = BlobServiceClient(account_url, credential=credential)
        container_name = str(uuid.uuid4())
        container_client = blob_service_client.create_container(container_name)
        print("Storage container created")
        time.sleep(10)
        blob_service_client.delete_container(container_name)
        print("Storage container deleted")
        blob_service_client.close()
    # Quickstart code goes here

except Exception as ex:
    print('Exception:')
    print(ex)