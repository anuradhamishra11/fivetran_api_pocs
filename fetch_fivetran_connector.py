import requests
import json

auth = ()
# url = "https://api.fivetran.com/v1/connectors/None/schemas"
url = "https://api.fivetran.com/v1/groups/pith_squire/connectors"
headers = {
    "Content-Type": "application/json",
    "Accept": "application/json;version=1"
}
resp = requests.get(url=url, headers=headers, auth=auth)
print(resp.json())
# resp = resp.json()
# tables = (
#             resp.get("data", {})
#             .get("schemas", {})
#             .get("go_09410711983140f1b68470806b859acb", {})
#             .get("tables", {})
#         )
# print(tables)
# print(list_of[0]["data"]["items"][0])

# for i in list_of[0]["data"]["items"]:
#     print(i["id"])