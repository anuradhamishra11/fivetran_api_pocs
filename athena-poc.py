import pandas as pd
import boto3


def get_var_char_values(d):
    return [obj['VarCharValue'] for obj in d['Data']]


def get_athena_query_using_boto():
    query = """SELECT DISTINCT "advertiser"."advertiser_id",
            "advertiser_name",
            "adset_statistics_report"."currency"
            FROM "criteo_vm_2"."advertiser"
            LEFT JOIN
            "criteo_vm_2"."adset_statistics_report"
            ON "advertiser"."advertiser_id" = "adset_statistics_report"."advertiser_id"
            WHERE "advertiser"."_fivetran_synced" >= CAST('2023-09-11 17:58:52.069713' as TIMESTAMP)"""

    athena_database = "criteo_vm_2"
    output = "s3://test-impressico/athena-test/"

    client = boto3.client('athena')
    response = client.start_query_execution(
        QueryString = query,
        QueryExecutionContext={
                'Database': athena_database},
        ResultConfiguration={
                'OutputLocation': output,
                }
    )

    while True:
        response_query_details = client.get_query_execution(QueryExecutionId=response["QueryExecutionId"])
        status = response_query_details['QueryExecution']['Status']['State']
        if status == "SUCCEEDED":
            break

    response_query_result = client.get_query_results(
        QueryExecutionId=response['QueryExecutionId']
    )

    header = response_query_result['ResultSet']['Rows'][0]
    rows = response_query_result['ResultSet']['Rows'][1:]

    header = [obj['VarCharValue'] for obj in header['Data']]
    result = [dict(zip(header, get_var_char_values(row))) for row in rows]

    df = pd.DataFrame(result)
    return df 
