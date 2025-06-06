import os
from datetime import datetime
import json
from pathlib import Path

import snowflake.connector
from airflow.decorators import dag, task
from airflow.models import Variable
from airflow.providers.snowflake.hooks.snowflake import SnowflakeHook
from airflow.sensors.base import PokeReturnValue

NAME = 'sumit'  # TODO 0: input your name to differentiate your table from others'
TABLE_NAME = f'airflow_lab_{NAME}'


def get_snowflake_connection():
    # TODO 1: Specify Airflow variables. Import them here.
    return snowflake.connector.connect(
        user=Variable.get('sf_user'),
        password=Variable.get('sf_password'),
        account=Variable.get('sf_account'),
        database=Variable.get('sf_database'),
        schema=Variable.get('sf_schema'),
    )

def get_snowflake_hook():
    # TODO 2: specify Snowflake connection - done
    return SnowflakeHook(snowflake_conn_id='snowflake_academy')

@task()
def create_table():
    conn = get_snowflake_connection()
    cur = conn.cursor()
    cur.execute(f"CREATE OR REPLACE TABLE {TABLE_NAME} (id STRING, data INT)")
    conn.commit()
    cur.close()
    conn.close()

@task.sensor(poke_interval=15, timeout=120)
def check_for_json_data() -> list[str]:
    '''
    TODO 3: implement sensor logic

    This sensor should scan for files with format ('data*.json') every 15 seconds,
    timeout after 2 minutes until at least 1 file is found. Also return the files for the next task

    Therefore, the output of this task, should this sensor passes, is a list[str]
    Hint: use Path().rglob()
    '''
    files = list(Path('.').rglob('data*.json'))

    if files:
        condition = True
        value = [str(p) for p in files]
    else:
        condition = False
        value = []

    return PokeReturnValue(is_done=condition, xcom_value=value)

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

Also since there are multiple students using the same Discord webhook, it's a good idea to
include your name in the message to distinguise from others.
'''


@task
def dag_success_notification():
    webhook = Variable.get("discord_webhook")
    message = f"✅ DAG airflow_lab succeeded for {NAME}"
    curl_cmd = (
        f"curl -H 'Content-Type: application/json' "
        f"-X POST -d '{{\"content\": \"{message}\"}}' {webhook}"
    )
    os.system(curl_cmd)

def discord_on_dag_failure_callback(context):
    webhook = Variable.get("discord_webhook")
    dag_id = context['dag_run'].dag_id
    exec_date = context['execution_date']
    message = f"❌ DAG {dag_id} failed on {exec_date} for {NAME}"
    os.system(
        f"curl -H 'Content-Type: application/json' "
        f"-X POST -d '{{\"content\": \"{message}\"}}' {webhook}"
    )

@dag(
    dag_id="airflow_lab",
    schedule_interval=None,
    start_date=datetime(2025, 3, 1),
    catchup=False,
    # TODO 5: failure_callback
    on_failure_callback=discord_on_dag_failure_callback
)

def airflow_lab():
    '''
    TODO 5: Connect all the tasks

    Think of the most appropriate task orders to build your dag and declare the dependencies here
    Some of the tasks are dynamics

    Remember to place dag_success_notification() at the end of the dag, and use the failure_callback() function for dag.
    '''

    # 1. Create the table
    create = create_table()

    # 2. Sensor to wait for JSON files
    files = check_for_json_data()

    # 3. Parse + insert each file dynamically
    rows = parse_json_data.expand(path=files)
    insert = insert_data.expand(row=rows)

    # 4. Success notification
    notify = dag_success_notification()

    # 5. Define dependencies
    create >> files
    files >> rows >> insert
    insert >> notify

airflow_lab()
