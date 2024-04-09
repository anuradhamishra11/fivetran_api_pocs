# # Delete a Connector
# # https://fivetran.com/docs/rest-api/connectors#deleteaconnector


import requests
import json

headers = {
    "Content-Type": "application/json",
    "Accept": "application/json;version=1"
}
# # # connctor_id = ""
auth = ()
# url = "https://api.fivetran.com/v1/connectors/passover_epidermis"

# response = requests.delete(url=url, headers= headers, auth= auth)
# print(response.text)
# # headers = {
#     'Authorization': f'Bearer AEZuU6uYqAwEson7',
#     'Content-Type': 'application/json'
# }

# data = {'status': 'off'}
    
# response = requests.patch(url, headers=headers, data=json.dumps(data), auth= auth_annu)
# print(response.text)

# # {"code":"Success","message":"Connector with id 'kin_user' has been deleted"}



# pause connector
# 
payload = {"paused": False}
url = "https://api.fivetran.com/v1/connectors/spray_accept"
response = requests.patch(url=url, headers=headers, data=json.dumps(payload), auth=auth)
print(response.json())


# {"code":"Success","message":"Connector has been updated","data":{"id":"revision_season","group_id":"recliner_warned","service":"s3","service_version":1,"schema":"testing_for_athena.crt_athena_table","connected_by":"outspoken_craftsmen","created_at":"2023-07-07T10:59:07.852239Z","succeeded_at":"2023-07-19T08:47:44.042Z","failed_at":null,"paused":false,"pause_after_trial":false,"sync_frequency":360,"schedule_type":"auto","status":{"setup_state":"connected","schema_status":"ready","sync_state":"scheduled","update_state":"on_schedule","is_historical_sync":false,"tasks":[],"warnings":[{"code":"faulty_row","message":"Skipped Improperly Formatted Data, Fix Faulty Rows in File"}]}}}

# {"code":"Success","message":"Connector has been created","data":{"id":"opacity_untapped","group_id":"pith_squire","service":"google_ads","service_version":1,"schema":"test_imp_google_ads2","connected_by":"directly_foyer","created_at":"2023-12-04T10:55:09.477813Z","succeeded_at":null,"failed_at":null,"paused":true,"pause_after_trial":false,"sync_frequency":360,"data_delay_threshold":0,"data_delay_sensitivity":"NORMAL","schedule_type":"auto","status":{"setup_state":"incomplete","schema_status":"ready","sync_state":"paused","update_state":"on_schedule","is_historical_sync":true,"tasks":[],"warnings":[]},"setup_tests":[{"title":"Checking access to selected accounts","status":"FAILED","message":"No client accounts found for the connected user"}],"config":{"sync_mode":"Selected Accounts","reports":"13","accounts":"1151679672","customer_id":"115-167-9672","conversion_window_size":30,"historical_sync_timeframe":"ALL TIME"}}}