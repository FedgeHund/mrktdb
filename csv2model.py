import csv
import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'fedgehundapi.settings')
django.setup()
from edgar.models import FailsToDeliver



with open('static/admin/csv_files/temp_fails.csv','rt')as f:
    data = csv.reader(f)

    try:

            Objects = [
                FailsToDeliver(
                    settlementDate=row[0], cusip=row[1], ticker=row[2], quantity=row[3], description=row[4]
                )
                for row in data
            ]

            FailsToDeliver.objects.bulk_create(Objects)

    except:
        print("Failed To Store")
