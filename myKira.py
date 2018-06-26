#!/usr/bin/env python3


#IMPORT LIBRARIES
import speech_recognition as sr
import os


#CREATING SYNONYMS DICTIONARY
mk=['make','create','mk']		#DO THE INSERTIONS IN THE BEG. (CREATE SYNO.)
rm=['delete','remove','drop','rm']	#DO THE INSERTIONS IN THE BEG. (REMOVE SYNO.)
dir_type=['directory','folder','dir']
dictionary_op=[mk,rm]			#TO DETECT OPERATION


#RECOGNIZER DEFINED
r=sr.Recognizer()


	## CREATING FUNCTIONS ## ------------------------------------------------------------------------------------------------

#ASKS FOR THE FILE/FOLDER NAME IF REQUIRED ( --RETURNS NAME OF FILE-- )
def ask_name():
	with sr.Microphone() as  source:
		r.adjust_for_ambient_noise(source)
		print("Can you mention the name?")
		os.system("espeak -v female3 'can you please tell me the name of folder'")
		audio=r.listen(source)
	try:
		name=r.recognize_google(audio)
		return name
	except:
		print("Sorry, could Not Understand!!")
		os.system("espeak -v female3 'Sorry could not understand'")
		pass



#ASKS FOR THE LOCATION IF REQUIRED ( --RETURNS LOC. OF FILE-- )
def ask_path():
	with sr.Microphone() as  source:
		r.adjust_for_ambient_noise(source)
		print("Can you mention the path or location ?")
		os.system("espeak -v female3 'can you please tell me the location of folder'")
		audio=r.listen(source)
	try:
		raw_path=r.recognize_google(audio)
		strip_data=raw_path.strip()
		split_data=strip_data.split()
		print(split_data)
	
		## THINK FOR THE SOLUTION ##

	except:
		print("Sorry, could Not Understand!!")
		os.system("espeak -v female3 'sorry could not understand'")
		pass


#CONVERTING LIST TO LOWER CASE ( --RETURNS LIST AS ARGUMENT INTO LOWER CASE-- )
def tolower(ip_list):
	for i in range(0,len(ip_list)):
		ip_list[i]=ip_list[i].lower()
	return ip_list


#CREATING FOLDER ( --RETURNS OPERATION KEYWORD-- )
def check_dict(ip):
	for i in range(0,len(ip)):
		for j in range(0,len(dictionary_op)):
			if ip[i] in dictionary_op[j]:
				return dictionary_op[j][-1]
				break	
	#return ("\nI have been designed to perform directory operations, not to handle your BULLSHIT!!!")


#CREATING FOLDER ( --RETURNS NOTHING-- )
def create_dir():
	dir_name=ask_name()
	os.system('mkdir '+dir_name)

#REMOVING FOLDER ( --RETURNS NOTHING-- )	## NEED TO EMPTY THE FOLDER BEFOREHAND (INTEGRATE EMPTY_DIRECTORY FUNCTION AFTER DONE)
def remove_dir():
	dir_name=ask_name()
	os.system('rmdir '+dir_name)
	
#RENAMING FOLDER ( --RETURNS NOTHING-- )
def rename_dir():
	source_dir=ask_name()
	new_dir=ask_name()
	os.system('mv '+source_dir+' '+new_dir)


 	## MAIN PART ## -----------------------------------------------------------------------------------------------------------------


#INITIAL INTRACTION WITH USER
with sr.Microphone() as  source:
	r.adjust_for_ambient_noise(source)
	print ("Heyyy, Whatsup chief!!!")
	os.system("espeak -v female3 'Hello Sir'")
	print("How can i help you?")
	os.system("espeak -v female3 'How can i help you'")	
	audio=r.listen(source)

try:
	
	speech_ip=r.recognize_google(audio)	#speech_ip --> VOICE INPUT
	print(speech_ip)
	
	#VOICE DATA CLEANING
	stripped_data=speech_ip.strip()		#____Removing extra spaces
	data=stripped_data.split()		#____Fetching individual words spoken
	data=tolower(data)
	print(data)
	
	operation=check_dict(data)
	#print(operation)
	
	if operation=='mk':
		create_dir()
	elif operation=='rm':
		remove_dir()
	else:
		rename_dir()
	
	'''
	if 'create' in final_data:
		for i in range(0,len(final_data)):
			if final_data[i]=='directory':
				dir_name=final_data[i+1]
				break
	if dir_name:
		os.system('mkdir '+dir_name)
	else:
		print("try again!")
	'''

except:
	print("Could Not Understand!!")
	os.system("espeak -v female3 'Sorry could not understand'")
pass
