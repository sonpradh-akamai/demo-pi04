from azure.keyvault.secrets import SecretClient
from azure.identity import DefaultAzureCredential

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

KVUri = f"https://keyvault-private-ep.vault.azure.net/"

try:
    credential=DefaultAzureCredential(managed_identity_client_id = "be4e963d-7cbd-4f5f-9a42-4bceb00d9ebf")
    client = SecretClient(vault_url=KVUri, credential=credential)

    #set_secret(client)
    for i in range(100):
        get_secret(client)
except Exception as err:
    print(err)

