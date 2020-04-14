"""
Simple DAG for using Airflow
"""
import datetime
import logging
from airflow import models
from airflow.operators import bash_operator
from airflow.operators import python_operator


DEFAULT_DAG_ARGS = {
    'start_date': datetime.datetime(2018, 1, 1)
}

with models.DAG(
        'composer_sample_greeting',
        schedule_interval=datetime.timedelta(days=1),
        default_args=DEFAULT_DAG_ARGS) as dag:
    def _hello_python():
        """
        A method here
        """
        logging.info('Hello World!')


    HELLO_PYTHON = python_operator.PythonOperator(
        task_id='HELLO_PYTHON',
        python_callable=_hello_python)

    GOODBYE_BASH = bash_operator.BashOperator(
        task_id='GOODBYE_BASH',
        bash_command='echo Goodbye')

    HELLO_PYTHON >> GOODBYE_BASH
