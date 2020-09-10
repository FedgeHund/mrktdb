import csv
import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'fedgehundapi.settings')
django.setup()
from edgar.models import CikCusipMapping



with open('static/admin/csv_files/CIK_CUSIP.csv','rt')as f:
    data = csv.reader(f)

    try:

            Objects = [
                CikCusipMapping(
                    year=row[0], cik=row[1], sec_name=row[2], cusip=row[3], cusip6=row[4]
                )
                for row in data
            ]

            CikCusipMapping.objects.bulk_create(Objects)

    except:
        print("Failed To Store")
