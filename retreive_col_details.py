import requests
import json

connector_id = "fraction_garrison"
schema = "go_af7a075e49c0486c853ebccd1f885121"
table = "ad_stats_custom"
url = "https://api.fivetran.com/v1/connectors/fraction_garrison/schemas/go_af7a075e49c0486c853ebccd1f885121/tables/ad_stats_custom/columns/active_view_impressions"
auth = ()
headers = {
    "Content-Type": "application/json",
    "Accept": "application/json;version=1"
}
payload = {
    "enabled": True,
    "hashed": False
}


resp = requests.patch(url=url, headers=headers, auth=auth, data=json.dumps(payload))
print(resp.json())