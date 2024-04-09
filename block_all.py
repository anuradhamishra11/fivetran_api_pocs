import requests
import json

auth = ()
url = "https://api.fivetran.com/v1/connectors/leader_dominoes/schemas"
headers = {
    "Content-Type": "application/json",
    "Accept": "application/json;version=1"
}
payload={
            "schemas": {"go_09410711983140f1b68470806b859acb": {"enabled": True}},
            "schema_change_handling": "BLOCK_ALL",
        }
resp = requests.patch(url=url, headers=headers, auth=auth, data=json.dumps(payload))
print(resp.json())