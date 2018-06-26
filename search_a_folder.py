#!/usr/bin/python3

import os

folder_to_be_searched = 'adhcsummer'
location_to_be_searched = '/home/pranav/'

#_______to find the  file_____
def find_all(filename,path):
    result = []
    for root,dirs,files in os.walk(path):
        if filename in dirs:
            result.append(os.path.join(root,filename))
    return result


answer = find_all(folder_to_be_searched,location_to_be_searched)		#_________________Function called

for i in range(0,len(answer)):
	print(answer[i])

