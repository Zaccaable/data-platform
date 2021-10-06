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


def load_knmi_to_landing(base_url, source, load_date=date(1900, 1, 1)):

    if not client.bucket_exists("landing-knmi"):
        client.make_bucket("landing-knmi")
    else:
        print('Bucket landing-knmi already exists')
    

    # load in batches of a year when running a full load
    if load_date == date(1900, 1, 1):
        batch_size = 30
    else:
        batch_size = 1

    for day in range(0, (date.today() - load_date).days, batch_size):
        start_date = load_date + timedelta(days=day)
        start_date_formatted = start_date.strftime('%Y%m%d')

        # Make sure we don't miss any days because of the range step
        end_date = load_date + timedelta(days=day + batch_size) if load_date + timedelta(days=day + batch_size) < date.today() else date.today()
        end_date_formatted = end_date.strftime('%Y%m%d')
        
        url = f'{base_url}?start={start_date_formatted}&end={end_date_formatted}'
        print(f'Cailling {url}')
        response = requests.get(url)
        
        
        result = client.put_object(
        "landing-knmi", f"{source}/{start_date}/{source}_{start_date}.csv", io.BytesIO(response.content), -1,
        content_type="application/csv", part_size=10*1024*1024,
        )
        print(
            "created {0} object; etag: {1}, version-id: {2}".format(
                result.object_name, result.etag, result.version_id,
            ),
        )

        
if __name__ == '__main__':
    load_knmi_to_landing('https://www.daggegevens.knmi.nl/klimatologie/daggegevens', 'daggegevens', date.today())
