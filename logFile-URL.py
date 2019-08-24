for ip, count in heapq.nlargest(k, sourceip.iteritems(), key=itemgetter(1)): top = "%d %s" % (count, ip) v = open("C:/Users/guest/Desktop/Log analysis/urls.txt", "w")
print >>v, top