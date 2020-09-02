import csv
import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'fedgehundapi.settings')
django.setup()
from edgar.models import CIK_CUSIP_MAPPING



with open('CIK_CUSIP.csv','rt')as f:
    data = csv.reader(f)

    try:

            Objects = [
                CIK_CUSIP_MAPPING(
                    year=row[0], cik=row[1], sec_name=row[2], cusip=row[3], cusip6=row[4]
                )
                for row in data
            ]

            CIK_CUSIP_MAPPING.objects.bulk_create(Objects)

    except:
        print("Failed To Store")
