import csv
import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'fedgehundapi.settings')
django.setup()
from edgar.models import FailsToDeliver



with open('static/admin/csv_files/Unique_Mappings.csv','rt')as f:
    data = csv.reader(f)

    try:
            print('Start')
            Objects = [
                FailsToDeliver(
                    settlementDate=row[0], cusip=row[1], ticker=row[2], description=row[3]
                )
                for row in data
            ]

            FailsToDeliver.objects.bulk_create(Objects, batch_size=1000)
            print('End')

    except:
        print("Failed To Store")
