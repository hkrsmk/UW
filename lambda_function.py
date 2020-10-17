import json
from botocore.vendored import requests
import socket

hostname = socket.gethostname()
iPAddr = socket.gethostbyname(hostname)

def lambda_handler(event, context):
    ip = requests.get('https://api.ipify.org').text
    
    if event['queryStringParameters'] is not None:
        name = event['queryStringParameters']['name']
        
        return {
            'statusCode': 200,
            'headers': { 'Content-Type': 'application/json',
                'x-hello-world': 'LJY'
            },
            'body': json.dumps({
            # "AWS_ip": ip,
            "ip": iPAddr,
            "greeting": "Hello " + name + "!",
            # "event": event,
            # "context": context
            # "flask": request.remote_addr
        })
        }

    return {
        'statusCode': 200,
        'headers': { 'Content-Type': 'application/json',
            'x-hello-world': 'LJY'
        },
        'body': json.dumps({
        # "AWS_ip": ip,
        "ip": iPAddr,
        # "event": event,
        # "context": context
        # "flask": request.remote_addr
    })
    }
