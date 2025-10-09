# Define a second operator to run the `consolidate_data.sh` script
consolidate = BashOperator(
    task_id='consolidate_task',
    bash_command='consolidate_data.sh'
    )

# Define a final operator to execute the `push_data.sh` script
push_data = BashOperator(
    task_id='pushdata_task',
    bash_command='push_data.sh'
    )

# Define a BashOperator called pull_sales with a bash command of wget https://salestracking/latestinfo?json.
# Set the pull_sales operator to run before the cleanup task.
# Configure consolidate to run next, using the downstream operator.
# Set push_data to run last using either bitshift operator.
# Define a new pull_sales task
pull_sales = BashOperator(
    task_id='pullsales_task',
    bash_command='wget https://salestracking/latestinfo?json'
)

# Set pull_sales to run prior to cleanup
pull_sales >> cleanup

# Configure consolidate to run after cleanup
cleanup >> consolidate

# Set push_data to run last
consolidate >> push_data
############# Sample dag for ref
from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

default_args = {
  'owner': 'dsmith',
  'start_date': datetime(2023, 2, 12),
  'retries': 1
}

with DAG('codependency', default_args=default_args) as codependency_dag:

  task1 = BashOperator(task_id='first_task',
                     bash_command='echo 1',
                     dag=codependency_dag)

  task2 = BashOperator(task_id='second_task',
                     bash_command='echo 2',
                     dag=codependency_dag)

  task3 = BashOperator(task_id='third_task',
                     bash_command='echo 3',
                     dag=codependency_dag)

  # task1 must run before task2 which must run before task3
  task1 >> task2
  task2 >> task3
  task3 >> task1

######=======================
  def pull_file(URL, savepath):
    r = requests.get(URL)
    with open(savepath, 'wb') as f:
        f.write(r.content)   
    # Use the print method for logging
    print(f"File pulled from {URL} and saved to {savepath}")

from airflow.operators.python import PythonOperator

# Create the task
pull_file_task = PythonOperator(
    task_id='pull_file',
    # Add the callable
    python_callable=pull_file,
    # Define the arguments
    op_kwargs={'URL':'http://dataserver/sales.json', 'savepath':'latestsales.json'}
)

########
default_args = {
  'owner': 'Engineering',
  'start_date': datetime(2023,11,1),
  'email': ['airflowresults@datacamp.com'],
  'email_on_failure': False,
  'email_on_retry': False,
  'retries': 3,
  'retry_delay': timedelta(minutes=20)
}

dag = DAG('update_dataflows', default_args=default_args, schedule_interval='30 12 * * 3')

####

from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator
from airflow.providers.http.operators.http import SimpleHttpOperator
from airflow.sensors.filesystem import FileSensor

dag = DAG(
   dag_id = 'update_state',
   default_args={"start_date": "2023-10-01"}
)

precheck = FileSensor(
   task_id='check_for_datafile',
   filepath='salesdata_ready.csv',
   dag=dag)

part1 = BashOperator(
   task_id='generate_random_number',
   bash_command='echo $RANDOM',
   dag=dag
)

import sys
def python_version():
   return sys.version

part2 = PythonOperator(
   task_id='get_python_version',
   python_callable=python_version,
   dag=dag)
   
part3 = SimpleHttpOperator(
   task_id='query_server_for_external_ip',
   endpoint='https://api.ipify.org',
   method='GET',
   dag=dag)
   
precheck >> part3 >> part2

##############

from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.sensors.filesystem import FileSensor
from datetime import datetime

report_dag = DAG(
    dag_id = 'execute_report',
    schedule_interval = "0 0 * * *"
)

precheck = FileSensor(
    task_id='check_for_datafile',
    filepath='salesdata_ready.csv',
    start_date=datetime(2023,2,20),
    mode='poke',
    dag=report_dag)

generate_report_task = BashOperator(
    task_id='generate_report',
    bash_command='generate_report.sh',
    start_date=datetime(2023,2,20),
    dag=report_dag
)

precheck >> generate_report_task
########


# Import the timedelta object
from datetime import timedelta

# Create the dictionary entry
default_args = {
  'start_date': datetime(2024, 1, 20),
  'sla': timedelta(minutes=30)
}

# Add to the DAG
test_dag = DAG('test_workflow', default_args=default_args, schedule_interval=None)

####
# Import the timedelta object
from datetime import timedelta

test_dag = DAG('test_workflow', start_date=datetime(2024,1,20), schedule_interval=None)

# Create the task with the SLA
task1 = BashOperator(task_id='first_task',
                     sla=timedelta(hours=3),
                     bash_command='initialize_data.sh',
                     dag=test_dag)


# Define the email task
email_report = EmailOperator(
        task_id='email_report',
        to='airflow@datacamp.com',
        subject='Airflow Monthly Report',
        html_content="""Attached is your monthly workflow report - please refer to it for more detail""",
        files=['monthly_report.pdf'],
        dag=report_dag
)

# Set the email task to run after the report is generated
email_report << generate_report
#########
from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.sensors.filesystem import FileSensor
from datetime import datetime

default_args={
    'email': ['airflowalerts@datacamp.com','airflowadmin@datacamp.com'],
    'email_on_failure': True,
    'email_on_success': True
}

report_dag = DAG(
    dag_id = 'execute_report',
    schedule_interval = "0 0 * * *",
    default_args=default_args
)

precheck = FileSensor(
    task_id='check_for_datafile',
    filepath='salesdata_ready.csv',
    start_date=datetime(2023,2,20),
    mode='reschedule',
    dag=report_dag)

generate_report_task = BashOperator(
    task_id='generate_report',
    bash_command='generate_report.sh',
    start_date=datetime(2023,2,20),
    dag=report_dag
)

precheck >> generate_report_task
##########

from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

default_args = {
  'start_date': datetime(2023, 4, 15),
}

cleandata_dag = DAG('cleandata',
                    default_args=default_args,
                    schedule_interval='@daily')

# Create a templated command to execute
# 'bash cleandata.sh datestring'
templated_command="""bash cleandata.sh {{ ds_nodash }} """

# Modify clean_task to use the templated command
clean_task = BashOperator(task_id='cleandata_task',
                          bash_command=templated_command,
                          dag=cleandata_dag)
#####

from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

default_args = {
  'start_date': datetime(2023, 4, 15),
}

cleandata_dag = DAG('cleandata',
                    default_args=default_args,
                    schedule_interval='@daily')

# Modify the templated command to handle a
# second argument called filename.
templated_command = """
  bash cleandata.sh {{ ds_nodash }} {{ params.filename }}
"""

# Modify clean_task to pass the new argument
clean_task = BashOperator(task_id='cleandata_task',
                          bash_command=templated_command,
                          params={'filename': 'salesdata.txt'},
                          dag=cleandata_dag)

# Create a new BashOperator clean_task2
clean_task2 = BashOperator(task_id='cleandata_task2',
                           bash_command=templated_command,
                          params={'filename': 'supportdata.txt'},
                          dag=cleandata_dag)
                           
# Set the operator dependencies
clean_task >> clean_task2

##
from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

filelist = [f'file{x}.txt' for x in range(30)]

default_args = {
  'start_date': datetime(2020, 4, 15),
}

cleandata_dag = DAG('cleandata',
                    default_args=default_args,
                    schedule_interval='@daily')

# Modify the template to handle multiple files in a 
# single run.
templated_command = """
  <% for filename in params.filenames %>
  bash cleandata.sh {{ ds_nodash }} {{ filename }};
  <% endfor %>
"""

# Modify clean_task to use the templated command
clean_task = BashOperator(task_id='cleandata_task',
                          bash_command=templated_command,
                          params={'filenames': filelist},
                          dag=cleandata_dag)

##########
from airflow import DAG
from airflow.operators.email import EmailOperator
from datetime import datetime

# Create the string representing the html email content
html_email_str = """
Date: {{ ds }}
Username: {{ params.username }}
"""

email_dag = DAG('template_email_test',
                default_args={'start_date': datetime(2023, 4, 15)},
                schedule_interval='@weekly')
                
email_task = EmailOperator(task_id='email_task',
                           to='testuser@datacamp.com',
                           subject="{{ macros.uuid.uuid4() }}",
                           html_content=html_email_str,
                           params={'username': 'testemailuser'},
                           dag=email_dag)
