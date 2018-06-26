#!/usr/bin/python3

import os

for root,dirs,files in os.walk('/home/priyank/Desktop/',topdown=True):
	#print('FILES ARE:-  ')
	for i in files:
		print(os.path.join(root,i))
	#print('DIRECTORIES ARE:-  ')
	for i in dirs:
		print(os.path.join(root,i))
