##airtable csv 파일에서 사진url만 가져와서 다운

import csv, codecs
import urllib.request

filename = "list.csv"
fp = codecs.open(filename, "r", "utf-8")

reader = csv.reader(fp, delimiter=",", quotechar='"')

line = []
line2 = []
url = []
name = 0

for cells in reader:
  line = cells[1].split()
  line2 += line

for li in line2:
  if "(https://" in li:
    url.append(li[1:-1])

for i in url:
    savename = "test" + str(name) + ".png"
    name += 1
    urllib.request.urlretrieve(i, savename)
    print("저장" + str(name) )
