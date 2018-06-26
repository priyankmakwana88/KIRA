#!/usr/bin/python3

import os
import subprocess as sub 
import speech_recognition as sr

r=sr.Recognizer()

with sr.Microphone() as source:
	r.adjust_for_ambient_noise(source)
	print("speak: ")
	audio=r.listen(source)
	print("done")


#synonym={'1':'create','2':'make','3':'produce','4':'build','5':'construct'}
#di={'key':'synonym'}
#d=synonym.has_key(keys)
#print(d)
try:
	audio_txt=r.recognize_google(audio)
	print(audio_txt)
	strip_txt=audio_txt.strip()
	final_txt=strip_txt.split()
	#x=dict[find.all('key:')]
	#if synonym in final_txt:
	if 'create' or 'make' or 'construct' or 'produce' or 'build' in final_txt:
		for i in range(0,len(final_txt)):
			if final_txt[i]=='directory':			
				dir_name=final_txt[i+1]
				break

	if dir_name:
		os.system('mkdir '+dir_name)
	else:
		print("try again !")
	

except:
	print("could not understand !")
	pass
