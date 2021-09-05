import csv
import re
import sys

HEADERS = ["id", "clean_data"]

FILENAME = 'flip_oc_0.json'

try:
    FILENAME = sys.argv[1]
except Exception:
    pass


def remove_unicodes(parsed_text):   
    string = parsed_text
    string_unicode = string.replace("�", "")
    return string_unicode

def clean_parsed_data(parsed_text):
    parsed_text = remove_unicodes(parsed_text)
    parsed_text = " ".join(item for item in parsed_text.split(' ') if item) 
    parsed_text = "\n".join(item for item in parsed_text.split('\n') if item)
    return parsed_text


data = []

print(FILENAME.split('.')[0])

with open(FILENAME.split('.')[0] + '_parseddata.csv', mode='r') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader: 
        parsed_text = row["parsed_data"]
        clean_text = clean_parsed_data(parsed_text)
        obj = {
            "id": row["id"],
            "clean_data": clean_text
        }
        data.append(obj)


with open(FILENAME.split('.')[0] + '_cleandata.csv', mode='w') as wfile:

    writer = csv.DictWriter(wfile, fieldnames=HEADERS)
    writer.writeheader()
    
    for clean__data in data:
      writer.writerow(clean__data)
