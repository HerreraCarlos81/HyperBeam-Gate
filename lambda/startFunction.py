import json
import requests

def lambda_handler(event, context):
    input_value = event['queryStringParameters']['value']

    # Modify this part with actual Hyperbeam API details
    hyperbeam_url = 'https://engine.hyperbeam.com/v0/vm'
    headers = {
        'Bearer': '<bearer>'
    }
    data = {
        'input': input_value
    }

    response = requests.post(hyperbeam_url, headers=headers, data=data)

    if response.status_code == 200:
        json_response = response.json()
        embed_url = json_response.get('embed_url', '')
        session_id = json_response.get('session_id', '')
        
        return {
            'statusCode': 200,
            'body': json.dumps({
                'embed_url': embed_url,
                'session_id': session_id
            })
        }
    else:
        return {
            'statusCode': response.status_code,
            'body': 'Error fetching URL'
        }