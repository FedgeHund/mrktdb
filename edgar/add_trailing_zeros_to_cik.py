import csv

old_file = open("../static/admin/csv_files/cik_cusip_mapping.csv", 'r')
reader = csv.reader(old_file)

print("Chaliye suru karte hn!")
new_rows = []
for row in reader:
    row[0] = str(row[0])
    row[0] = row[0].zfill(10)
    new_rows.append(row)

with open("../static/admin/csv_files/final_cik_cusip_mapping.csv", 'a+', newline='') as write_obj:
    writer = csv.writer(write_obj)
    writer.writerows(new_rows)

print("Ho gya bhai! Check Krle")
