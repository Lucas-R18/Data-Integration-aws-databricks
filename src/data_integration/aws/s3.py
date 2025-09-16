# COMMAND ----------
import boto3
import os 
from dotenv import load_dotenv

# COMMAND ----------
load_dotenv(dotenv_path=fr'..\env\aws_lrodrigues_developer.env')

aws_key_id      = os.getenv('aws_key_id')      
aws_secret_key  = os.getenv('aws_secret_key')      
aws_region_name = os.getenv('aws_region_name')  

# COMMAND ----------

def s3_Session():
    boto3.setup_default_session(
        aws_access_key_id     = aws_key_id,
        aws_secret_access_key = aws_secret_key,
        region_name           = aws_region_name
    )    

    s3 = boto3.client("s3")

    return s3