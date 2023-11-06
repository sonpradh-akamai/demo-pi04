import azure.functions as func
import logging
import requests
import os


app = func.FunctionApp(http_auth_level=func.AuthLevel.ANONYMOUS)

@app.route(route="send_http_Req")
def send_http_Req(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    x = requests.get(os.environ["TARGET_URL"])
    res= x.text
    return func.HttpResponse(
             res,
             status_code=200
        )
