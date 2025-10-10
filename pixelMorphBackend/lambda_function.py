import json
import boto3
from PIL import Image
import io

s3 = boto3.client('s3')

def lambda_handler(event, context):
    bucket = event['Records'][0]['s3']['bucket']['name']
    key = event['Records'][0]['s3']['object']['key']

    img_object = s3.get_object(Bucket=bucket, Key=key)
    img_data = img_object['Body'].read()
    image = Image.open(io.BytesIO(img_data))
    
    gray_image = image.convert("L")
    
    out_buffer = io.BytesIO()
    gray_image.save(out_buffer, format='JPEG')
    out_buffer.seek(0)
    
    new_key = f"processed/{key}"
    s3.put_object(Body=out_buffer, Bucket=bucket, Key=new_key, ContentType='image/jpeg')
    
    return {
        'statusCode': 200,
        'body': json.dumps({'message': 'Image processed', 'processed_key': new_key})
    }
