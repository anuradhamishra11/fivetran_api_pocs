import requests
import json

headers = {
    "Content-Type": "application/json",
    "Accept": "application/json;version=1"
}

auth = ()

def create_fivetran_s3_connector():
    url = "https://api.fivetran.com/v1/connectors"

    # payload =  {
    #     "service": "s3",
    #     "group_id": "recliner_warned",
    #     "config": {
    #         "schema": "testing_for_athena",
    #         "table": "crt_athena_table",
    #         "external_id": "recliner_warned",
    #         "is_public": "false",
    #         "role_arn": "arn:aws:iam::582697339087:role/annu-bucket-for-fivetran-1-role",
    #         "bucket": "source-annu-bucket",
    #         "compression": "infer",
    #         "on_error": "skip",
    #         "append_file_option": "upsert_file",
    #         "archive_pattern": "regex_pattern",
    #         "null_sequence": "",
    #         "delimiter": ",",
    #         "escape_char": "",
    #         "skip_before": "0",
    #         "skip_after": "0",
    #         "empty_header": "false",
    #         "list_strategy": "complete_listing",
    #         "use_pgp_encryption_options": "false"
    #     }
    # }
    _common_metrics_fields = [
        "metrics.cost_micros",
        "metrics.impressions",
        "metrics.clicks",
        "metrics.video_views",
        "metrics.engagements",
        "metrics.conversions",
        "metrics.conversions_value",
        "metrics.all_conversions",
        "metrics.all_conversions_value",
        "metrics.view_through_conversions",
        "metrics.gmail_secondary_clicks",
        "metrics.value_per_conversion",
        "metrics.video_quartile_p100_rate",
        "metrics.video_quartile_p75_rate",
        "metrics.video_quartile_p50_rate",
        "metrics.video_quartile_p25_rate",
        "metrics.interactions",
    ]
    payload = {
    "service": "google_ads",
    "group_id": "pith_squire",
    "config": {
        "schema": "test_imp_google_ads2",
        "customer_id": "115-167-9672",
        "sync_mode": "SpecificAccounts",
        "timeframe_months": "ALL_TIME",
        "accounts": ["1151679672"],
        "manager_accounts": [],
        "reports": [
    {
        "table": "campaign_stats_custom",
        "config_type": "Custom",
        "report_type": "campaign",
        "fields": [
            "campaign.id",
            "campaign.name",
            "campaign.start_date",
            "campaign.end_date",
            "segments.date",
            "campaign.advertising_channel_sub_type",
            "campaign.advertising_channel_type",
            "campaign.bidding_strategy_type",
            "campaign.final_url_suffix",
            "campaign.labels",
            "campaign.serving_status",
            "campaign.status",
            "campaign.tracking_url_template",
            "campaign.url_custom_parameters",
            "campaign_budget.amount_micros",
            "campaign_budget.period",
            # stats related fields for campaigns without ad_groups or ads.
            *_common_metrics_fields,
        ],
    },
    {
        "table": "ad_group_info",
        "config_type": "Custom",
        "report_type": "ad_group",
        "fields": [
            "ad_group.campaign",
            "ad_group.final_url_suffix",
            "ad_group.id",
            "ad_group.labels",
            "ad_group.name",
            "ad_group.status",
            "ad_group.tracking_url_template",
            "ad_group.type",
            "ad_group.url_custom_parameters",
            "bidding_strategy.name",
            "bidding_strategy.type",
            "campaign.id",
            "segments.date",
        ],
    },
    {
        "table": "ad_info",
        "config_type": "Custom",
        "report_type": "ad_group_ad",
        "fields": [
            "campaign.id",
            "segments.date",
            "ad_group_ad.ad.text_ad.headline",
            "ad_group_ad.ad.id",
            "ad_group_ad.ad.name",
            "ad_group.id",
            "ad_group_ad.ad.expanded_text_ad.headline_part1",
            "ad_group_ad.ad.expanded_text_ad.headline_part2",
            "segments.ad_network_type",
            "ad_group_ad.ad.legacy_responsive_display_ad.description",
            "ad_group_ad.ad.legacy_responsive_display_ad.short_headline",
            "ad_group_ad.ad.legacy_responsive_display_ad.long_headline",
            "ad_group_ad.ad.legacy_responsive_display_ad.call_to_action_text",
            "ad_group_ad.status",
            "ad_group_ad.ad.type",
            "ad_group_ad.ad.display_url",
            "ad_group_ad.labels",
            "ad_group_ad.ad.image_ad.pixel_height",
            "ad_group_ad.ad.image_ad.pixel_width",
            "ad_group_ad.ad.image_ad.name",
            "ad_group_ad.ad.tracking_url_template",
            "ad_group_ad.ad.url_custom_parameters",
            "ad_group_ad.ad.final_url_suffix",
            "ad_group_ad.ad.final_urls",
            "ad_group_ad.ad.final_mobile_urls",
            "ad_group_ad.ad.legacy_responsive_display_ad.main_color",
            "ad_group_ad.ad.added_by_google_ads",
        ],
    },
    {
        "table": "ad_stats_custom",
        "config_type": "Custom",
        "report_type": "ad_group_ad",
        "fields": [
            "campaign.id",
            "ad_group_ad.ad.id",
            "ad_group.id",
            "segments.date",
            *_common_metrics_fields,
        ],
    },
    {
        "table": "keyword_search_info",
        "config_type": "Custom",
        "report_type": "keyword_view",
        "fields": [
            "segments.date",
            "campaign.bidding_strategy",
            "campaign.bidding_strategy_type",
            "campaign.id",
            "ad_group.id",
            "ad_group_criterion.keyword.text",
            "ad_group_criterion.criterion_id",
            "ad_group_criterion.status",
            "ad_group_criterion.keyword.match_type",
            "ad_group_criterion.quality_info.creative_quality_score",
            "ad_group_criterion.quality_info.quality_score",
            "ad_group_criterion.effective_cpm_bid_micros",
            "ad_group_criterion.effective_cpc_bid_micros",
            "ad_group_criterion.topic.topic_constant",
            "ad_group_criterion.final_urls",
            "ad_group_criterion.tracking_url_template",
            "ad_group_criterion.final_url_suffix",
            "ad_group_criterion.url_custom_parameters",
        ],
    },
    {
        "table": "keyword_search_stats",
        "config_type": "Custom",
        "report_type": "keyword_view",
        "fields": [
            "segments.date",
            "ad_group_criterion.criterion_id",
            "campaign.id",
            "ad_group.id",
            "ad_group_criterion.keyword.text",
            *_common_metrics_fields,
        ],
    },
    {
        "table": "keyword_display_info",
        "config_type": "Custom",
        "report_type": "display_keyword_view",
        "fields": [
            "segments.date",
            "campaign.bidding_strategy",
            "campaign.bidding_strategy_type",
            "campaign.id",
            "ad_group.id",
            "ad_group_criterion.keyword.text",
            "ad_group_criterion.criterion_id",
            "ad_group_criterion.status",
            "ad_group_criterion.effective_cpm_bid_micros",
            "ad_group_criterion.effective_cpc_bid_micros",
            "ad_group_criterion.effective_cpv_bid_micros",
            "ad_group_criterion.final_urls",
            "ad_group_criterion.final_mobile_urls",
            "ad_group_criterion.tracking_url_template",
            "ad_group_criterion.url_custom_parameters",
        ],
    },
    {
        "table": "keyword_display_stats",
        "config_type": "Custom",
        "report_type": "display_keyword_view",
        "fields": [
            "segments.date",
            "campaign.id",
            "ad_group_criterion.criterion_id",
            "ad_group.id",
            "ad_group_criterion.keyword.text",
            *_common_metrics_fields,
        ],
    },
    {
        "table": "breakdown_device",
        "config_type": "Custom",
        "report_type": "ad_group_ad",
        "fields": [
            "campaign.id",
            "ad_group_ad.ad.id",
            "ad_group.id",
            "segments.date",
            "metrics.cost_micros",
            "metrics.impressions",
            "metrics.clicks",
            "metrics.video_views",
            "metrics.engagements",
            "metrics.conversions",
            "metrics.conversions_value",
            "metrics.all_conversions",
            "metrics.all_conversions_value",
            "metrics.view_through_conversions",
            "metrics.gmail_secondary_clicks",
            "metrics.value_per_conversion",
            "metrics.video_quartile_p100_rate",
            "metrics.video_quartile_p75_rate",
            "metrics.video_quartile_p50_rate",
            "metrics.video_quartile_p25_rate",
            "segments.device",
        ],
    },
    {
        "table": "breakdown_conversion_name",
        "config_type": "Custom",
        "report_type": "ad_group_ad",
        "fields": [
            "campaign.id",
            "ad_group_ad.ad.id",
            "ad_group.id",
            "segments.date",
            "segments.conversion_action_name",
            "metrics.conversions",
            "metrics.conversions_value",
            "metrics.all_conversions",
            "metrics.all_conversions_value",
        ],
    },
    {
    "table": "age_range_view_breakdown",
    "config_type": "Custom",
    "report_type": "age_range_view",
    "fields": [
        # Age-related fields
        "campaign.id",
        "ad_group.id",
        "ad_group_criterion.criterion_id",
        "age_range_view.resource_name",
        "segments.date",
    ]
},
    {
        "table": "campaign_breakdown_conversion_name",
        "config_type": "Custom",
        "report_type": "campaign",
        "fields": [
            "campaign.id",
            "campaign.advertising_channel_type",  # needed for CAMPAIGN_TYPES_WITHOUT_ADS filtering.
            "segments.date",
            "segments.conversion_action_name",
            "metrics.conversions",
            "metrics.conversions_value",
            "metrics.all_conversions",
            "metrics.all_conversions_value",
        ],
    },
    {
        "table": "video_info",
        "config_type": "Custom",
        "report_type": "video",
        "fields": [
            "campaign.id",
            "ad_group_ad.ad.id",
            "ad_group.id",
            "segments.date",
            "video.id",
            "video.title",
            "video.channel_id",
            "video.duration_millis",
        ],
    },
],
    },
    "auth":  {
            "client_access": {
                "client_id": "202821350369-av6kh75ts2k2umc1iv1ir29us82sm6u6.apps.googleusercontent.com",
                "client_secret": "7hAqWJB92y5hn-EpnS0Iu4h9",
                "user_agent": "tracer",
                "developer_token": "eKDY-l5v7dypoLq4cmwkQQ",
            },
            "refresh_token": "1//0dtLvio3fGi9hCgYIARAAGA0SNwF-L9IrggV5531-Lt6mzxfTY7v-w5YE3fh65OmRKEdul3rm8JIYDHtnS3reufrsC3_8z1PK2Vk",
        }
}



    response = requests.post(url, headers=headers, data=json.dumps(payload), auth=auth)
    print(response.text)

create_fivetran_s3_connector()
# output:
# {"code":"Success","message":"Connector has been created","data":{"id":"cork_franc","group_id":"kinetic_rectitude","service":"s3","service_version":1,"schema":"test_s3.test_table_s3","connected_by":"rudely_perfume","created_at":"2023-06-27T10:31:32.552922Z","succeeded_at":null,"failed_at":null,"paused":false,"pause_after_trial":false,"sync_frequency":360,"schedule_type":"auto","status":{"setup_state":"connected","schema_status":"ready","sync_state":"scheduled","update_state":"on_schedule","is_historical_sync":true,"tasks":[],"warnings":[]},"setup_tests":[{"title":"Validating archive pattern","status":"PASSED","message":""},{"title":"Finding matching files","status":"PASSED","message":"Here are some files we found matching the regex specified: <br />annual-enterprise-survey-2021-financial-year-provisional-size-bands-csv.csv"},{"title":"Validating escapeChar","status":"SKIPPED","message":""},{"title":"Connecting to bucket","status":"PASSED","message":""},{"title":"PGP Support Test","status":"SKIPPED","message":""},{"title":"Validating Bucket Name","status":"PASSED","message":""},{"title":"Validating ExternalID","status":"PASSED","message":""},{"title":"Validating file pattern regex","status":"SKIPPED","message":""},{"title":"PrivateLink Test","status":"SKIPPED","message":""}],"config":{"schema":"test_s3","require_privatelink":"false","file_reading_behavior":"Infer file type based on file extension","modified_file_merge":"Overwrite Rows","pattern":"","external_id":"kinetic_rectitude","error_handling":"Syncs only valid data from each file","folder_path":"","connection_method":"Directly","list_strategy":"Lists and retrieves every newly modified file each sync","bucket":"dump-region-east","null_sequence":"","role_arn":"arn:********","bucket_public_":false,"delimiter":",","headerless_csv_":"false","compression_behavior":"Infer file compression based on file extension","escape_character":"","table":"test_table_s3","archive_pattern":"regex_pattern"}}}

# {"code":"Success","message":"Connector has been created","data":{"id":"imprinted_tournament","group_id":"recliner_warned","service":"s3","service_version":1,"schema":"test_s3_2.test_table_s3_2","connected_by":"outspoken_craftsmen","created_at":"2023-07-06T05:12:09.035623Z","succeeded_at":null,"failed_at":null,"paused":false,"pause_after_trial":false,"sync_frequency":360,"schedule_type":"auto","status":{"setup_state":"connected","schema_status":"ready","sync_state":"scheduled","update_state":"on_schedule","is_historical_sync":true,"tasks":[],"warnings":[]},"setup_tests":[{"title":"Validating file pattern regex","status":"SKIPPED","message":""},{"title":"Validating archive pattern","status":"PASSED","message":""},{"title":"Validating ExternalID","status":"PASSED","message":""},{"title":"Finding matching files","status":"PASSED","message":"Here are some files we found matching the regex specified: <br />data_raw.csv"},{"title":"PrivateLink Test","status":"SKIPPED","message":""},{"title":"Validating escapeChar","status":"SKIPPED","message":""},{"title":"PGP Support Test","status":"SKIPPED","message":""},{"title":"Validating Bucket Name","status":"PASSED","message":""},{"title":"Connecting to bucket","status":"PASSED","message":""}],"config":{"schema":"test_s3_2","require_privatelink":"false","file_reading_behavior":"Infer file type based on file extension","modified_file_merge":"Overwrite Rows","pattern":"","external_id":"recliner_warned","error_handling":"Syncs only valid data from each file","folder_path":"","connection_method":"Directly","list_strategy":"Lists and retrieves every newly modified file each sync","bucket":"source-annu-bucket","null_sequence":"","role_arn":"arn:********","bucket_public_":false,"delimiter":",","headerless_csv_":"false","compression_behavior":"Infer file compression based on file extension","escape_character":"","table":"test_table_s3_2","archive_pattern":"regex_pattern"}}}



#  google ads connector output:
# {"code":"Success","message":"Connector has been created","data":{"id":"everywhere_husked","group_id":"pith_squire","service":"google_ads","service_version":1,"schema":"test_imp_google_ads","connected_by":"directly_foyer","created_at":"2023-07-12T09:43:25.015032Z","succeeded_at":null,"failed_at":null,"paused":true,"pause_after_trial":false,"sync_frequency":360,"schedule_type":"auto","status":{"setup_state":"incomplete","schema_status":"ready","sync_state":"paused","update_state":"on_schedule","is_historical_sync":true,"tasks":[],"warnings":[]},"setup_tests":[{"title":"Checking access to selected accounts","status":"FAILED","message":"Setup test failed with \"com.fivetran.integrations.google_ads.exceptions.GoogleAdsServiceException: java.lang.IllegalStateException: Either accessToken or refreshToken must not be null\""}],"config":{"sync_mode":"Selected Accounts","reports":"2","accounts":"","customer_id":"1151679672","conversion_window_size":30,"historical_sync_timeframe":"6 months"}}}

# 8
# {"code":"Success","message":"Connector has been created","data":{"id":"maid_commonplace","group_id":"pith_squire","service":"google_ads","service_version":1,"schema":"test_imp_google_ads8","connected_by":"directly_foyer","created_at":"2023-07-19T13:40:19.515976Z","succeeded_at":null,"failed_at":null,"paused":true,"pause_after_trial":false,"sync_frequency":360,"schedule_type":"auto","status":{"setup_state":"connected","schema_status":"ready","sync_state":"paused","update_state":"on_schedule","is_historical_sync":true,"tasks":[],"warnings":[]},"setup_tests":[{"title":"Checking access to selected accounts","status":"PASSED","message":""},{"title":"Validating reports","status":"PASSED","message":""},{"title":"Validating fields","status":"PASSED","message":""}],"config":{"sync_mode":"Selected Accounts","reports":"12","accounts":"1151679672","customer_id":"115-167-9672","conversion_window_size":30,"historical_sync_timeframe":"12 months"}}}

#9
# {"code":"Success","message":"Connector has been created","data":{"id":"june_until","group_id":"pith_squire","service":"google_ads","service_version":1,"schema":"test_imp_google_ads9","connected_by":"directly_foyer","created_at":"2023-07-27T15:27:15.321479Z","succeeded_at":null,"failed_at":null,"paused":true,"pause_after_trial":false,"sync_frequency":360,"schedule_type":"auto","status":{"setup_state":"connected","schema_status":"ready","sync_state":"paused","update_state":"on_schedule","is_historical_sync":true,"tasks":[],"warnings":[]},"setup_tests":[{"title":"Validating reports","status":"PASSED","message":""},{"title":"Checking access to selected accounts","status":"PASSED","message":""},{"title":"Validating fields","status":"PASSED","message":""}],"config":{"sync_mode":"Selected Accounts","reports":"12","accounts":"1151679672","customer_id":"115-167-9672","conversion_window_size":30,"historical_sync_timeframe":"ALL TIME"}}}