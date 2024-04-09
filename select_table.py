import requests

CONNECTOR_ID = "save_zoom"
SCHEMA_ID = "imp_go_83420d17765948799b6b0429bd073af321"
TABLE_ID = "age_range_view_breakdown"
auth = ('api_key','secret_key')

api_url = f"https://api.fivetran.com/v1/connectors/{CONNECTOR_ID}/schemas/{SCHEMA_ID}/tables/{TABLE_ID}"

headers = {
    "Content-Type": "application/json",
    "Accept": "application/json;version=1"
}

columns_to_select = [
        "campaign.id",
        "ad_group.id",
        "ad_group_criterion.criterion_id",
        "age_range_view.resource_name",
        "segments.date",
    ]

payload = {
    "overrides": {
        "column_settings": {
            "columns": {
                "include": columns_to_select
            }
        }
    }
}

response = requests.patch(api_url, json=payload, headers=headers, auth=auth)

print(response.json())
