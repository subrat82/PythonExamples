print("Hello, World!")

# sample code to read lines from text file
def file_read_from_head(fname, nlines):
    from itertools import islice
    with open(fname) as f:
        for line in islice(f, nlines):
            print(line)


file_read_from_head('test.txt', 2)

# WORKING CODE FOR PATTERN 404 IN LOGS UING REGEXS

import re

count=0
fl = open('test.txt', 'r')
fillines=fl.readlines()
fl.close()
for i in fillines:
  if re.search(r'status=404', i):
    count+=1

print(count)