import os
from datetime import datetime
import json
from pathlib import Path

import snowflake.connector
from airflow.decorators import dag, task
from airflow.models import Variable
from airflow.providers.snowflake.hooks.snowflake import SnowflakeHook
from airflow.sensors.base import PokeReturnValue

NAME = 'light'  # TODO 0: input your name to differentiate your table from others'
TABLE_NAME = f'airflow_lab_{NAME}'


def get_snowflake_connection():
    # TODO 1: Specify Airflow variables. Import them here.
    return snowflake.connector.connect(
        user='user',
        password='password',
        account='account',
        database='DB_LAB_M1W4',
        schema='SC_LAB_M1W4_DEMO',
    )

def get_snowflake_hook():
    # TODO 2: specify Snowflake connection
    return SnowflakeHook(snowflake_conn_id='snowflake_academy')

@task()
def create_table():
    conn = get_snowflake_connection()
    cur = conn.cursor()
    cur.execute(f"CREATE OR REPLACE TABLE {TABLE_NAME} (id STRING, data INT)")
    conn.commit()
    cur.close()
    conn.close()
    
@task.sensor()
def check_for_json_data() -> list[str]:
    '''
    TODO 3: implement sensor logic
    
    This sensor should scan for files with format ('data*.json') every 15 seconds,
    timeout after 2 minutes until at least 1 file is found. Also return the files for the next task
    
    Therefore, the output of this task, should this sensor passes, is a list[str]
    Hint: use Path().rglob()
    '''

@task
def parse_json_data(path: str) -> tuple:
    row_data = json.loads(Path(path).read_text())
    return (row_data['id'], row_data['data'])

@task
def insert_data(row: tuple):
    '''
    DO NOT modify this task
    '''
    id, data = row
    hook = get_snowflake_hook()
    hook.run(f"INSERT INTO {TABLE_NAME} values ('{id}', {data})")

'''
TODO 4: Notification
Complete the folllowing 2 functions.

The first one is a task, which is to be placed at the end of dag to signal successful run
The second one is a callback function, which will be placed in DAG config

hint: the bash command to send notification to discord server is
curl -H 'Content-Type: application/json' -X POST -d '{"content": "This string will be sent to discord channel"} $discord_webwooh
'''


@task
def dag_success_notification():
    ...

def discord_on_dag_failure_callback(context):
    ...

@dag(
    dag_id="airflow_lab",
    schedule_interval=None,
    start_date=datetime(2025, 3, 1),
    catchup=False,
    # TODO 5
)
def airflow_lab():
    '''
    TODO 5: Connect all the tasks
    
    Think of the most appropriate task orders to build your dag and declare the dependencies here
    Some of the tasks are dynamics
    
    Remember to place dag_success_notification() at the end of the dag, and use the failure_callback() function for dag.
    '''

airflow_lab()