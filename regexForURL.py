# Python code to find the URL from an input string
# Using the regular expression
import re

#search a URL from an input string

def Find(string):
    # findall() has been used
    # with valid conditions for urls in string
    url = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]| [! * \(\),] | (?: %[0-9a-fA-F][0-9a-fA-F]))+', string)
    return url


# Driver Code
string = 'My Profile: https://auth.geeksforgeeks.org/ user / Chinmoy % 20Lenka / articles in the portal of http: // www.geeksforgeeks.org / '
print("Urls: ", Find(string))

#search a given URL and its count in a log file

count=0
fl = open('test.txt', 'r')
fillines=fl.readlines()
fl.close()
for i in fillines:
  if re.search(r'geeks', i):
    count+=1

print(re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]| [! * \(\),] | (?: %[0-9a-fA-F][0-9a-fA-F]))+', 'https://auth.geeksforgeeks.org/'))

print(count)