import requests


connector_id = "maid_commonplace"
api_url = f'https://api.fivetran.com/v1/connectors/{connector_id}'

new_config = {
    "schemaStatus": "BLOCK_ALL"
}

headers = {
    "Content-Type": "application/json",
    "Accept": "application/json;version=1"
}

auth = ("LJMKmiGdxry2v5B4", "Zp8wm8hziZuvycvPjEJGWNfXXy2nihQJ")

response = requests.patch(api_url, json=new_config, headers=headers, auth= auth)

print("Response:", response.json())
