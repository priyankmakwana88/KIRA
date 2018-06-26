#!/usr/bin/python3

import os
import subprocess as sub 
import speech_recognition as sr
from os import path
r=sr.Recognizer()

with sr.Microphone() as source:
	r.adjust_for_ambient_noise(source)	
	print("speak: ")
	audio=r.listen(source)
	print("done")


try:
	audio_txt=r.recognize_google(audio)
	print(audio_txt)
	strip_txt=audio_txt.strip()
	final_txt=strip_txt.split()
	print(strip_txt)
	if 'place' in final_txt:
		for i in range(0,len(final_txt)):
			if final_txt[i]=='place':
				dir_name1=final_txt[i+1]
			if final_txt[i]=='directory':
				dir_name=final_txt[i+1]
				break



	new_place=dir_name + '/' +dir_name1
	os.rename(dir_name1, new_place)

except:
	print("not good!")
	pass




'''
	move(src,dest)
	def move(src,dest):
		src="/home/deepu/Desktop/."
		dest="/home/deepu/Desktop/machinelearning"
		listofFiles=os.listdir(src)
		for f in listofFiles:
			fullPath = src + "/" + f
			sub.Popen("mv" + " " + fullPath + " " + dest ,shell=True)

'''

