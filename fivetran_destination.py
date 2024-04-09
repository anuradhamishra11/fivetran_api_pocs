import requests
import json

api_key = 'AwUgo4QhrESaMlvW'
base_url = 'https://api.fivetran.com/v1'

headers = {
    "Content-Type": "application/json",
    "Accept": "application/json;version=1"
}

auth_annu = ('AEZuU6uYqAwEson7','daRHWfAGKOB1KDxOk9wvQmb7uYI2R12v')

def create_fivetran_s3_destination():
    url = f'{base_url}/destinations'
    
    payload = {
        "group_id":  "surest_colonel",
        "service": "new_s3_datalake",
        "region": "AWS_US_EAST_1",
        "time_zone_offset": "-5",
        "config" :
            {
            "bucket": "",
            "fivetran_role_arn": "arn:aws:iam::771740779609:role/fivtran_admin",
            "prefix_path": "dev01",
            "region": "us-east-1"
            }
    }
    
    response = requests.post(url, headers=headers, data=json.dumps(payload), auth=('AwUgo4QhrESaMlvW','WeGK6Gw4GueHybbaxgO2xn9cpgObzcNU'))
    print(response.text)


# create_fivetran_s3_destination()

def create_group():
    base_url = "https://api.fivetran.com/v1/groups"
    payload = {"name" : "New_Destination_Demo"}
    response = requests.post(base_url, headers=headers, data=json.dumps(payload), auth=auth_annu).text
    response = json.loads(response)
    print(response, "response")
    print(type(response), "type of response")
    group_id = response['data']['id']
    print(group_id, "group_id")

    # set environment variable
    with open('.env', 'a') as file:
        file.write(f'FIVETRAN_DESTINATION_ID=f{group_id}\n')
        file.close()


create_group()