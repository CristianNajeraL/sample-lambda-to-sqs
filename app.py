"""
AWS lambda handler to populate SQS
"""
import os
import random
import boto3
import pandas as pd
from sqlalchemy import create_engine


SECRETS_ARN = os.environ["SECRETS_ARN"]
client = boto3.client('secretsmanager')
secrets = eval(client.get_secret_value(SecretId=SECRETS_ARN)["SecretString"])
user = secrets["db_username"]
password = secrets["db_password"]
host = secrets["db_host"]
port = secrets["db_port"]
db_name = secrets["db_database"]
query = """SELECT usename AS role_name,
 CASE
  WHEN usesuper AND usecreatedb THEN
    CAST('superuser, create database' AS pg_catalog.text)
  WHEN usesuper THEN
    CAST('superuser' AS pg_catalog.text)
  WHEN usecreatedb THEN
    CAST('create database' AS pg_catalog.text)
  ELSE
    CAST('' AS pg_catalog.text)
 END role_attributes
FROM pg_catalog.pg_user
ORDER BY role_name desc;"""


def lambda_handler(event, context):
    """
    Sample handler
    :return:
    """
    engine = create_engine(
        f'postgresql://{user}:{password}@{host}:{port}/{db_name}'
    )
    print(f'postgresql://{user}:{password}@{host}:{port}/{db_name}')
    df = pd.read_sql(
        query,
        con=engine
    )
    roles = list(df['role_name'].astype(str).values)
    roles = ', '.join(roles)
    return {
        "available_roles": roles,
        "random": f"This is master = {random.random()}."
    }
