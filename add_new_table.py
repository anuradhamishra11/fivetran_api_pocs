import requests

headers = {
    "Content-Type": "application/json",
    "Accept": "application/json;version=1"
}
connector_id = 'save_zoom'

api_url = f'https://api.fivetran.com/v1/connectors/{connector_id}/custom_tables'

new_custom_table = {
    "table": "age_range_view_breakdown",
    "config_type": "Custom",
    "report_type": "age_range_view",
    "fields": [
        # Age-related fields
        "campaign.id",
        "ad_group.id",
        "ad_group_ad.age_range",
        "ad.id",
        "ad_group_criterion.criterion_id",
        "age_range_view.resource_name",
        "segments.date",
        "ad_account.ad_account_name",
        "ad_account.ad_account_timezone",
        "ad_account.ad_account_tracking_url_template",
        "ad_group.ad_group_final_url_suffix",
        "ad_group.ad_group_id",
        "ad_group.ad_group_name",
        "ad_group.ad_group_tracking_url_template",
        "ad_group.ad_group_type",
        "ad_group.advertising_sub_channel",
        "ad_group.age_range",
        "campaign.campaign_final_url_suffix",
        "campaign.campaign_id",
        "campaign.campaign_tracking_url_template",
        "campaign.campaign_type",
        "Campaign.campaign_url_custom_parameters",
    ]
}

response = requests.post(api_url, json=new_custom_table, headers=headers)
print(response.json())
