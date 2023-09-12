import os, uuid
from azure.identity import DefaultAzureCredential
from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient

try:
    print("Azure Blob Storage Python quickstart sample")
    account_url = "https://serviceepgccstorage.blob.core.windows.net"
    credential=DefaultAzureCredential(managed_identity_client_id = "be4e963d-7cbd-4f5f-9a42-4bceb00d9ebf")

    # Create the BlobServiceClient object
    blob_service_client = BlobServiceClient(account_url, credential=credential)

    # Create a unique name for the container
    container_name = str(uuid.uuid4())

    # Create the container
    container_client = blob_service_client.create_container(container_name)
    # Quickstart code goes here

except Exception as ex:
    print('Exception:')
    print(ex)