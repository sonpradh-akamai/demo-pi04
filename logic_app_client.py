import requests

def send_get_request(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            print(f"Request {response.url} successful. Response:")
            print(response.text)
        else:
            print(f"Request {response.url} failed with status code {response.status_code}")
    except requests.RequestException as e:
        print(f"Error making the request: {e}")

def main():
    target_url = "https://priv-ep-test-logic-app.azurewebsites.net:443/api/priv-ep-test-wrokflow/triggers/When_a_HTTP_request_is_received/invoke?api-version=2022-05-01&sp=%2Ftriggers%2FWhen_a_HTTP_request_is_received%2Frun&sv=1.0&sig=WQoU5TJIZorQEaPCSbTajQlxvdS-LS3qCHcmnOMNP68"

    # Send GET request 10 times
    for i in range(10):
        print(f"\nSending GET request #{i+1}")
        send_get_request(target_url)

if __name__ == "__main__":
    main()