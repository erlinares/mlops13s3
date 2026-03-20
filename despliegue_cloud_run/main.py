import os
from google.cloud import aiplatform

def run_pipeline():
    
    project = os.environ.get("PROJECT_ID")
    location = os.environ.get("LOCATION")
    
    
    pipeline_path = os.environ.get("PIPELINE_PATH")
    service_account = os.environ.get("SERVICE_ACCOUNT")
    validate_table = os.environ.get("VALIDA_TABLE")
    input_age = os.environ.get("INPUT_AGE")


    aiplatform.init(project=project, location=location)

    job = aiplatform.PipelineJob(
        display_name="bigquery test pipeline",
        template_path=pipeline_path,
        enable_caching=False,
        project=project,
        location=location,
        parameter_values={
            "project": project,
            "validate_table": validate_table,
            "input_age": input_age
        }
    )

    print('submit pipeline job ...')
    job.submit(service_account=service_account)

if __name__ == "__main__":
    run_pipeline()
