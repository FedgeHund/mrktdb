from edgar.models import FailsToDeliver
import csv
import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'fedgehundapi.settings')
django.setup()


with open('static/admin/csv_files/Unique_Mappings.csv', 'rt', encoding='utf8')as f:
    data = csv.reader(f)

    print('Start')
    Objects = [
        FailsToDeliver(
            cusip=row[0], description=row[1], settlementDate=row[2], ticker=row[3]
        )
        for row in data
    ]

    FailsToDeliver.objects.bulk_create(Objects, batch_size=1000)
    print('End')
