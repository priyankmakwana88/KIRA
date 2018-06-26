#!/usr/bin/python3

import os

#pos = input('Enter the location')

total_dirs = 0
total_files = 0


for root,dirs,files in os.walk('/home/priyank/Desktop/',topdown=True):
	
# to find all the number of directories		
	for all in range(0,len(dirs)):
		total_dirs = total_dirs + len(dirs[all])
# to find all the number of files

	for all in range(0,len(files)):
		total_files = total_files + len(files[all])

# print result
print(total_dirs)
print(total_files)

