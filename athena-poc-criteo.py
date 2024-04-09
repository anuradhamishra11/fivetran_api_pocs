import pandas as pd
from pyathena import connect

output = "s3://test-impressico/athena-test/"
athena_query =  """SELECT DISTINCT "advertiser"."advertiser_id",
        "advertiser_name",
        "adset_statistics_report"."currency"
        FROM "criteo_vm_2"."advertiser"
        LEFT JOIN
        "criteo_vm_2"."adset_statistics_report"
        ON "advertiser"."advertiser_id" = "adset_statistics_report"."advertiser_id"
        WHERE "advertiser"."_fivetran_synced" >= CAST('2023-09-11 17:58:52.069713' as TIMESTAMP)"""


conn = connect(s3_staging_dir=output,
               region_name='us-east-1')

df = pd.read_sql(athena_query, conn)

print(df)
