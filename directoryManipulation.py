#List all .txt files in a specified directory + subdirectories.

import os

path = 'c:\\TestProjects\\'

files = []
# r=root, d=directories, f = files
for r, d, f in os.walk(path):
    for file in f:
        if '.py' in file:
            files.append(os.path.join(r, file))

for f in files:
    print(f)

#List all directories in a specified directory + subdirectories.

import os

path = 'c:\\TestProjects\\'

folders = []

# r=root, d=directories, f = files
for r, d, f in os.walk(path):
    for folder in d:
        folders.append(os.path.join(r, folder))

for f in folders:
    print(f)

#List all .txt files in a specified directory + subdirectories (**).

import glob

path = 'c:\\projects\\hc2\\'

files = [f for f in glob.glob(path + "**/*.txt", recursive=True)]

for f in files:
    print(f)

#List all directories in a specified directory + subdirectories (**).

folders = [f for f in glob.glob(path + "**/", recursive=True)]

for f in folders:
    print(f)





