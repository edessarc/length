import os

import sys

directory = sys.argv[1]

index = ""
for root, dirs, files in os.walk(directory):
    for directory_name in dirs:
         if len(directory_name) > len(index):
                index = directory_name

print('The folder in the given directory with the longest name is:', index)
