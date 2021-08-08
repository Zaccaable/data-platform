from datetime import date, timedelta
import io
import os

import requests
from minio import Minio
from dotenv import load_dotenv

load_dotenv()

client = Minio(
        endpoint="192.168.86.192:9000",
        access_key=os.getenv("MINIO_ACCESS_KEY"),
        secret_key=os.getenv("MINIO_SECRET_KEY"),
        secure=False,
    )


def load_knmi_to_landing(base_url, source, load_date=None):

    if not client.bucket_exists("landing-knmi"):
        client.make_bucket("landing-knmi")
    else:
        print('Bucket landing-knmi already exists')
    
    
    # If no date is supplied, get all data
    if not load_date:
        print('No date was passed')
        #response = requests.get(url)
    else:
        # if load date available, only retrieve delta
        
        start_date = load_date - timedelta(days=1)
        start_date_formatted = start_date.strftime('%Y%m%d')
        end_date = date.today()
        end_date_formatted = end_date.strftime('%Y%m%d')
        url = f'{base_url}?start={start_date_formatted}&end={end_date_formatted}'
        print(f'Cailling {url}')
        response = requests.get(url)
        #print(response.status_code, response.content)
        
        
        result = client.put_object(
        "landing-knmi", f"{source}/{start_date}.csv", io.BytesIO(response.content), -1,
        content_type="application/csv", part_size=10*1024*1024,
        )
        print(
            "created {0} object; etag: {1}, version-id: {2}".format(
                result.object_name, result.etag, result.version_id,
            ),
        )
        
if __name__ == '__main__':
    load_knmi_to_landing('https://www.daggegevens.knmi.nl/klimatologie/daggegevens', 'daggegevens', date.today())
