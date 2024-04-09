# import requests
# import json

# id ="fireside_cricket"
# group_id="pith_squire"
# url = "https://api.fivetran.com/v1/groups/{group_id}/connectors/{id}/force"

# headers = {
#     "Content-Type": "application/json",
#     "Accept": "application/json;version=1"
# }

# response = requests.post(url, headers=headers, auth=auth)
# print(response.json())


# Webhook

import requests

connector_id = "maid_commonplace"
url = "https://api.fivetran.com/v1/connectors/{connector_id}/schemas"

auth = ('api_key','secret_key')
headers = {
    "Content-Type": "application/json",
    "Accept": "application/json;version=1"
}
response = requests.get(url, auth=auth)

print(response.json())