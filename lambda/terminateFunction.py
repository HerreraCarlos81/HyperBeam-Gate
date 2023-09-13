import json
import requests

def lambda_handler(event, context):
    session_id = event['queryStringParameters']['session_id']

    # Modify this part with actual Hyperbeam API details for terminating sessions
    hyperbeam_terminate_url = 'https://engine.hyperbeam.com/v0/vm/terminate'
    headers = {
        'Bearer': '<bearer>',
        'Session-Id': session_id
    }

    response = requests.post(hyperbeam_terminate_url, headers=headers)

    if response.status_code == 200:
        return {
            'statusCode': 200,
            'body': 'Session terminated successfully'
        }
    else:
        return {
            'statusCode': response.status_code,
            'body': 'Error terminating session'
        }
