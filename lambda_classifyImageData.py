
import boto3
import json
import base64
 


# Fill this in with the name of your deployed model
endpoint = "image-classification-2023-10-26-20-15-10-544" #"image-classification-2023-10-23-23-23-04-042" #"image-classification-2023-10-25-17-46-23-762" ## TODO: fill in

def lambda_handler(event, context):

    # Decode the image data
    body = event['body']

    #image_data = body['image_data']
    
    image = base64.b64decode(body["image_data"]) #(## TODO: fill in)
    
    
    runtime = boto3.Session().client('sagemaker-runtime')
    response = runtime.invoke_endpoint(EndpointName=endpoint, ContentType = 'image/png',Body = image)
    predictions = json.loads(response['Body'].read().decode())
    event["inferences"] = predictions    
    print(event)
    
    return {
        'statusCode': 200,
        'body': event #json.dumps(event)
    }
