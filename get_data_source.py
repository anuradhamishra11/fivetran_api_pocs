import requests
import json

auth = ()
url = "https://api.fivetran.com/v1/source/{source_id}/connectors"
headers = {
    "Content-Type": "application/json",
    "Accept": "application/json;version=1"
}
resp = requests.get(url=url, headers=headers, auth=auth)