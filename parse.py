from bs4 import BeautifulSoup
import collections as cc
import pandas as pd
import sys
import csv
import re
import os


HEADERS = ["id", "parsed_data"]

FILENAME = 'flip_oc_0.json'

try:
  FILENAME = sys.argv[1]
except Exception:
  pass


print(FILENAME)

json_mail = pd.read_json(FILENAME)


data = []
redundent_data = 0
for i in range(0,len(json_mail._source)):
  html_doc = json_mail._source[i]['rawHtml']
  soup = BeautifulSoup(html_doc, 'html.parser')
  parsed_text = ""

  try :
    parsed_text = soup.body.text
  except Exception:
    redundent_data += 1 
    continue
  
  obj = {
    "id": json_mail._id[i],
    "parsed_data": parsed_text
  }
  data.append(obj)


with open(FILENAME.split('.')[0] + '_parseddata.csv', mode='w') as wfile:

    writer = csv.DictWriter(wfile, fieldnames=HEADERS)
    writer.writeheader()
    
    for parsed__data in data:
      writer.writerow(parsed__data)

print(redundent_data, " No of mails cannot be parsed because of absence of <body></body> tag")


os.system(f'python3 clean.py {FILENAME}')