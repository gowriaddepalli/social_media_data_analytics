#!/usr/bin/python
#This only works with the business dataset, to use other datasets change the lines marked in the loop below

import sys
import json
import csv

ifilename = sys.argv[1]
try:
    ofilename = sys.argv[2]
except:
    ofilename = ifilename + ".csv"

# LOAD DATA
json_lines = [json.loads( l.strip() ) for l in open(ifilename).readlines() ]
OUT_FILE = open(ofilename, "w", encoding="utf8")
root = csv.writer(OUT_FILE)
root.writerow(["business_id","full_address","hours","open","categories","city","review_count","name","neighborhoods","longitude","state","stars","latitude","attributes","type"])
json_no = 0
for l in json_lines:
    root.writerow([l["business_id"],l["full_address"],l["hours"],l["open"],l["categories"],l["city"],l["review_count"],l["name"],l["neighborhoods"],l["longitude"],l["state"],l["stars"],l["latitude"],l["attributes"],l["type"]])
    json_no += 1

print('Finished {0} lines'.format(json_no))
OUT_FILE.close()
