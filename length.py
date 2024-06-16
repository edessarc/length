import os

#directory = input('Please type the directory you want to check for the longest name: \n')

import sys

directory = sys.argv[1]

#print(directory)
index = ""
for root, dirs, files in os.walk(directory):
    for directory_name in dirs:
         if len(directory_name) > len(index):
                index = directory_name
                #print(index)

print('The folder in the given directory with the longest name is:', index)
