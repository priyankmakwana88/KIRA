#!/usr/bin/python3

import os 
#import shutil
import subprocess as sub 
import speech_recognition as sr
from os import path

r=sr.Recognizer()

with sr.Microphone() as source:
	r.adjust_for_ambient_noise(source)	
	print("speak: ")
	path_audio=r.listen(source)
	print("done")




def delete_files(dir_name):
	mydir=dir_name
	filelist=[f for f in os.listdir(mydir)]
	for f in filelist:
		os.remove(os.path.join(mydir, f))


try:
	input_data=r.recognize_google(path_audio)
	print(input_data)
	strip_path=input_data.strip()   #remove extra space
	final_data=strip_path.split()    #split the data

	print(final_data)
	
	if 'remove' in final_data:
		for i in range(0,len(input_data)):
			if final_data[i]=='directory':
				dir_name=final_data[i+1]
				break


	
	
	delete_files(dir_name)

except:
	print("hr kuch")
	pass









