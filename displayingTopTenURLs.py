from collections import defaultdict
from operator import itemgetter

access = defaultdict(int)

#f = open('test.txt', 'r')
#fillines=fl.readlines()
#fl.close()

#for i in fillines:
#with open("test.txt", "wb") as f:
f = open('test.txt', 'r')
for line in f:
     parts = line.split() # split at whitespace
     access[parts[11] + parts[13]] += 1 # adapt indices here

# print all URLs in descending order
for url, count in sorted(access.iteritems(), key=lambda  c: -c):
  print ("%d %s" , count, url)

# if you only want to see the top k entries:
import heapq
k = 10
for url, count in heapq.nlargest(k, access.iteritems(), key=itemgetter(1)):
  print ("%d %s", count, url)