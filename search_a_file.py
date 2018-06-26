#!/usr/bin/python3

import os

file_to_be_searched = 'menu.py'
location_to_be_searched = '/home/pranav/Desktop/adhcsummer'

#_______to find the  file_____
def find_all(filename,path):
    result = []
    for root,dirs,files in os.walk(path):
        if filename in files:
            result.append(os.path.join(root,filename))
    return result


answer = find_all(file_to_be_searched,location_to_be_searched)		#_________________Function called

for i in range(0,len(answer)):
	print(answer[i])

os.system('gedit '+answer[0])
