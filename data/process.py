# -*- coding: UTF-8 -*-

import csv

results = csv.reader(open('scrum_surveyresponse_src.csv', 'rb'), delimiter=',', quotechar='"')

bucket = []
i = 0
for row in results:
  i += 1
  if i < 3:
    continue
    
  # Parse date
  tmp = row[1].split(' ')
  date = tmp[0].split('/')
  end2 = date[2]+'-'+date[0]+'-'+date[1]+' '+tmp[1]
  row[1] = end2
  
  # Translate string
  if row[4] == 'več kot 5':
    row[4] = 'more than 5'
  bucket.append(row)

#print bucket
spamWriter = csv.writer(open('scrum_surveyresponse.csv', 'wb'), delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
for row in bucket:
    spamWriter.writerow(row)

