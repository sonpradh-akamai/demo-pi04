from azure.keyvault.secrets import SecretClient
from azure.identity import DefaultAzureCredential
import time
def set_secret(client):
    secretName = "jsonkey"
    secretValue = "{'additional_properties': {}, 'id': None}"
    client.set_secret(secretName, secretValue)
    print(" done.")

def get_secret(client):
    secretName = "jsonkey"
    print(f"Retrieving your secret from testeastuskeyvault.")
    retrieved_secret = client.get_secret(secretName)
    print(f"Your secret is '{retrieved_secret.value}'.")

KVUri = f"https://accounting-keyvault-1.vault.azure.net/"

try:
    credential=DefaultAzureCredential(managed_identity_client_id = "88048b88-17e6-4060-a8ba-353181118ae6")

    while(True):
        client = SecretClient(vault_url=KVUri, credential=credential)
        set_secret(client)
        for i in range(10):
            get_secret(client)
        time.sleep(10)
except Exception as err:
    print(err)