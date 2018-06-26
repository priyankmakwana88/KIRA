#!/usr/bin/python3

import os
path=input("enter the path")
for dirname, dirnames, filenames in os.walk(path):
	# print path to all subdirectories first.
	for subdirname in dirnames:
		print(os.path.join(dirname, subdirname))

	# print path to all filenames.
	for filename in filenames:
		print(os.path.join(dirname, filename))
