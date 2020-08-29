import csv
import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'fedgehundapi.settings')
django.setup()
from edgar.models import CIK_CUSIP_MAPPING



with open('CIK_CUSIP.csv','rt')as f:
    data = csv.reader(f)

    for row in data:
        CIK_CUSIP_MAPPING.objects.get_or_create(year=row[0], cik=row[1], sec_name=row[2], cusip=row[3], cusip6=row[4])
        print(row)


    # For Bulk Create
    # Object_list = []
    # for row in data:
    #     Object_list.append(CIK_CUSIP_MAPPING(year=row[0], cik=row[1], sec_name=row[2], cusip=row[3], cusip6=row[4]))
    #
    # CIK_CUSIP_MAPPING.objects.bulk_create(Object_list)
    # print("Successfully Stored !!!")
