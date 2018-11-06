import boto3
import argparse
import pprint
import pyperclip


def generate():

    parser = argparse.ArgumentParser(description='Generate presigned download link and copies to clipboard. Default expiry 1 hour')

    parser.add_argument('--bucket', '-b', required=True, type=str)
    parser.add_argument('--key', '-k', required=True, type=str)
    parser.add_argument('--expiry', '-e', required=False, type=int)

    args = parser.parse_args()

    expiry = args.expiry if args.expiry else 60*60

    client = boto3.client('s3')

    response = client.generate_presigned_url(
        'get_object', 
        Params={
            'Bucket': args.bucket, 
            'Key': args.key,   
        },
        ExpiresIn=expiry
    )
    pyperclip.copy(str(response))
    print("URL copied to clipboard")
