import requests
import json

headers = {
    "Content-Type": "application/json",
    "Accept": "application/json;version=1"
}

auth = ()

url = "https://api.fivetran.com/v1/connectors/maid_commonplace/schemas/tables/resync"

payload = {
"test_imp_google_ads8": ["campaign_stats_custom"]
}

response = requests.post(url, headers=headers, data=json.dumps(payload), auth=auth)
print(response.text)

# {"code":"Success","message":"Re-sync has been triggered successfully"}