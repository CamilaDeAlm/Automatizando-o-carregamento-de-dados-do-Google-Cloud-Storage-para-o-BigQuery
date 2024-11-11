from googleapiclient.discovery import build


def trigger_df_job(cloud_event,environment):   
 
    service = build('dataflow', 'v1b3')
    project = "prj-poc-001"

    template_path = "gs://dataflow-templates-us-central1/latest/GCS_Text_to_BigQuery"

    template_body = {
    "jobName": "bq-load",  
    "parameters": {
        "inputFilePattern": "gs://bkt-carregamento/employee.csv",
        "JSONPath": "gs://bkt-df/bq.json",
        "outputTable": "rare-terminal-440318-r9:employee.employee",
        "bigQueryLoadingTemporaryDirectory": "gs://bkt-carregamento/employee.csv",
        "javascriptTextTransformGcsPath": "gs://bkt-df/dataflow.js",
        "javascriptTextTransformFunctionName": "transform"
    }
    }

    request = service.projects().templates().launch(projectId=project,gcsPath=template_path, body=template_body)
    response = request.execute()
    print(response)