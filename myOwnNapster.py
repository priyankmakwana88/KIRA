#!/usr/bin/env python3


#IMPORT LIBRARIES
import speech_recognition as sr
import os
import time
import pwd
import grp
import subprocess            
import requests
import webbrowser as wb                                                  


#CREATING SYNONYMS DICTIONARY
mk=['make','create','mk']		#DO THE INSERTIONS IN THE BEG. (CREATE SYNO.)
rm=['delete','remove','drop','rm']	#DO THE INSERTIONS IN THE BEG. (REMOVE SYNO.)
dictionary_op=[mk,rm]			#TO DETECT OPERATION

dir_type=['directory','folder','folders','directories','dir']
file_type=['file','files','fi']
dictionary_type=[dir_type,file_type]	#TO DETECT OPERATION TYPE

count=['total','number','num']
list_file=['list','li']
dictionary_count=[count,list_file]	#DETECT VISIBLITY TYPE i.e. count total files(count) or list total files(list_file)

metadata=['property','properties','details','detail','size','permission','permissions','md'] 	#DETECT THE PROPERTIES KEYWORD
dictionary_md=[metadata]

mv=['move','transfer','mv']		#DETECT WEATHER TO MOVE OR COPY THE DIR
cp=['copy','cp']
hide=['hide','hd']
empty=['empty','clean','emty']
dictionary_change=[mv,cp,hide,empty]

play=['play','youtube','song','ply']	#DETECT WEATHER TO PLAY A SONG OR SEARCH THROUGH WEB
search=['google','web','search','srch']
dictionary_web=[play,search]


#RECOGNIZER DEFINED
r=sr.Recognizer()


	## CREATING FUNCTIONS ## ------------------------------------------------------------------------------------------------

'''
#ASKS FOR THE FILE {SPECIFIED} NAME IF REQUIRED ( --RETURNS NAME OF FILE-- )		
def ask_name_file():
	with sr.Microphone() as  source:
		r.adjust_for_ambient_noise(source)
		print("Can you mention the name?")
		audio=r.listen(source)
	try:
		name=r.recognize_google(audio)
		split_data=name.split()
		for i in range(0,len(split_data)):
			if split_data[i]=='dot':
				split_data[i]=='.'
		n_name=''
		for i in split_data:
			n_name=n_name+i
		return n_name
	except:
		print("Sorry, could Not Understand!!")
		pass

'''
#ASKS FOR THE FILE/FOLDER NAME IF REQUIRED ( --RETURNS NAME OF FILE-- )		
def ask_name():
	with sr.Microphone() as  source:
		r.adjust_for_ambient_noise(source)
		print("Can you mention the name?")
		audio=r.listen(source)
	try:
		name=r.recognize_google(audio)
		return name
	except:
		print("Sorry, could Not Understand!!")
		pass
		


def confirmation_ask():
	with sr.Microphone() as  source:
		r.adjust_for_ambient_noise(source)
		print("Are you sure (yes/no)? (CAUTION : ACTION CANNOT BE UNDONE)")
		audio=r.listen(source)
	try:
		confirm_choice=r.recognize_google(audio)
		return confirm_choice
	except:
		print("Sorry, could Not Understand!!")
		pass



#ASKS FOR THE LOCATION IF REQUIRED ( --RETURNS LOC. OF FILE-- )
def ask_path():
	path="/"
	final="/home/"+subprocess.getoutput("whoami")
	c=[] 
	#f=0   
	d=""
	with sr.Microphone() as  source:
		r.adjust_for_ambient_noise(source)
		print("Can you mention the path or location ? (HOME  is default path)")
		audio=r.listen(source)
	try:
		raw_path=r.recognize_google(audio)
		#strip_data=raw_path.strip()
		#split_data=strip_data.split()
		#print(split_data)
		if (raw_path=="current location") or (raw_path=="current path") or (raw_path=="present location") or (raw_path=="present path"):
			final=subprocess.getoutput("pwd")
			#if path is a somewhere else in user
		else:
			split_data=raw_path.split()
			for i in range(0,len(split_data)):
				if split_data[i]=='desktop':
					split_data[i]='Desktop'
				

			if ("on" in split_data) or ("in" in split_data) or ("at" in split_data):
				for i in range(0, len(split_data)):
					if (split_data[i]=="on") or (split_data[i]=="in") or (split_data[i]=="at"):
						c.insert(len(c),split_data[i+1])
						for j in range(0, len(c)):
							d=(path+c[j])
							final=(final+d)
							d=""
							c=[]
		return final
		## THINK FOR THE SOLUTION ##

	except:
		print("Sorry, could Not Understand!!")
		pass


#CONVERTING LIST TO LOWER CASE ( --RETURNS LIST AS ARGUMENT INTO LOWER CASE-- )
def tolower(ip_list):
	for i in range(0,len(ip_list)):
		ip_list[i]=ip_list[i].lower()
	return ip_list


#DICTIONARY CHECKING FOR REQUIRED DETAILS ( --RETURNS MULTIPLE-- ) 

def check_dict(ip):
	operation='null'
	op_type='null'
	count_type='null'
	file_details='null'
	dir_op='null'
	web_op='null'
	#TO DETECT OPERATION TO PERFORM
	for i in range(0,len(ip)):
		for j in range(0,len(dictionary_op)):
			if ip[i] in dictionary_op[j]:
				operation = dictionary_op[j][-1]
				break
			
	#TO DETECT FILE TYPE ON WHICH OPERATION WILL BE PERFORMED		
	for p in range(0,len(ip)):
		for k in range(0,len(dictionary_type)):
			if ip[p] in dictionary_type[k]:
				op_type = dictionary_type[k][-1]
				break
			
	#DETECTING WEATHER TO PRINT LIST OF FILES OR NUMBER		
	for p in range(0,len(ip)):
		for k in range(0,len(dictionary_count)):
			if ip[p] in dictionary_count[k]:
				count_type = dictionary_count[k][-1]
				break

	#DETECTING PERMISSION DETAILS ASKED		
	for p in range(0,len(ip)):
		for k in range(0,len(dictionary_md)):
			if ip[p] in dictionary_md[k]:
				file_details = dictionary_md[k][-1]
				break

	#DETECTING WEATHER TO MOVE OR COPY A DIR		
	for p in range(0,len(ip)):
		for k in range(0,len(dictionary_change)):
			if ip[p] in dictionary_change[k]:
				dir_op = dictionary_change[k][-1]
				break

	#DETECTING WEATHER TO PLAT A SONG OR SEARCH THROUGH WEB		
	for p in range(0,len(ip)):
		for k in range(0,len(dictionary_web)):
			if ip[p] in dictionary_web[k]:
				web_op = dictionary_web[k][-1]
				break

	return operation ,op_type,count_type,file_details,dir_op,web_op
	#return ("\nI have been designed to perform directory operations, not to handle your BULLSHIT!!!")


#CREATING FOLDER ( --RETURNS NOTHING-- )
def create_dir():
	dir_name=ask_name()
	print(dir_name)
	loc=ask_path()
	print(loc)
	os.system('mkdir '+loc+'/'+dir_name)

#REMOVING FOLDER ( --RETURNS NOTHING-- )	## NEED TO EMPTY THE FOLDER BEFOREHAND (INTEGRATE EMPTY_DIRECTORY FUNCTION AFTER DONE)
def remove_dir():
	dir_name=ask_name()
	print(dir_name)
	loc=ask_path()
	print(loc)
	confirm=confirmation_ask()
	if (confirm=="yes") or (confirm=="ya") or (confirm=="sure"):
		os.system('rmdir '+loc+'/'+dir_name)
	
#RENAMING FOLDER ( --RETURNS NOTHING-- )
def rename_dir():
	source_dir=ask_name()
	print (source_dir+' will be renamed.')	
	loc=ask_path()
	print (loc)
	print('Mention the new name.')
	new_dir=ask_name()
	os.system('mv '+loc+'/'+source_dir+' '+loc+'/'+new_dir)


#COUNT DIRECTORIES AND FILES ( ** 2 functions **) ( --RETURNS NOTHING-- )
#DIRECTORY
'''
def count_dir():
	loc=ask_path()
	total_dirs=0
	for root,dirs,files in os.walk(loc+'/',topdown=True):
		for all in range(0,len(dirs)):
			total_dirs = total_dirs + len(dirs[all])
	print('Total directories present on '+loc+'/ : ',total_dirs)
'''
def count_dir():
	count=0
	a=ask_path()
	os.system("ls -l "+a+" | grep -c ^d")

#FILES
'''
def count_file():
	loc=ask_path()
	total_files=0
	for root,dirs,files in os.walk(loc+'/',topdown=True):
		for all in range(0,len(files)):
			total_files = total_files + len(files[all])
	print('Total files present on '+loc+'/ : ',total_files)
'''
def count_file():
	count=0
	a=ask_path()
	os.system("ls -l "+a+" | egrep -c '^-'")



#LIST DIRECTORIES AND FILES ( --RETURNS NOTHING-- )
def list_dir():
	loc=ask_path()
	dir_names = os.listdir(loc+'/')
	for i in dir_names:
		print(i)
	

#SHOW PROPERTIES ( --RETURNS NOTHING-- )
def show_properties():
	#GET FILE NAME
	with sr.Microphone() as  source:
		r.adjust_for_ambient_noise(source)
		print('Mention the name of file')
		audio=r.listen(source)
		#GET LOCATION OF FILE
	try:
		##
		#file_name=r.recognize_google(audio)	#speech_ip --> VOICE INPUT
		file_name=r.recognize_google(audio)
		split_data=file_name.split()
		for i in range(0,len(split_data)):
			if split_data[i]=='dot':
				split_data[i]=='.'
		n_name=''
		for i in split_data:
			n_name=n_name+i		
		##
		print(n_name)
		loc=ask_path()
		file = loc+'/'+n_name 
		#____ to find the properties of the file
		info = os.stat(file)
		# to find permission in octal
		per = str(oct(os.stat(file)[0]))[5:8]
		#____ initalize the empty list to contain the permissions
		per_mode=[]
		for i in range(0,len(per)):
			if per[i]=='0':
				per_mode.append('---')
			elif per[i]=='1':
				per_mode.append('--x')
			elif per[i]=='2':
				per_mode.append('-w-')
			elif per[i]=='3':
				per_mode.append('-wx')
			elif per[i]=='4':
				per_mode.append('r--')
			elif per[i]=='5':
				per_mode.append('r-x')
			elif per[i]=='6':
				per_mode.append('rw-')
			else :
				per_mode.append('rwx')
		# to find owner name from owner id:-
		uid = info.st_uid   # get the owner uid number
		userinfo = pwd.getpwuid(uid)[0]  #________ get the owner name from owner id
		# to find group name from group id:-
		gid = info.st_gid   # get the owner uid number
		groupinfo = grp.getgrgid(gid)[0]  #________ get the owner name from owner id
	
		#printing details	
		print('File\'s Location   :', file)
		print('')
		print('Group\'s name:    ',groupinfo)
		print('User\'s name:    ',userinfo)
		print('User\'  permission :  ',per_mode[0])
		print('Group\' permission :  ',per_mode[1])
		print('Other\' permission :  ',per_mode[2])
		print('Access time       : ', time.ctime(os.path.getatime(file)))
		print('Modified time     : ', time.ctime(os.path.getmtime(file)))
		print('Change time       : ', time.ctime(os.path.getctime(file)))
		print('Size         	  : ', os.path.getsize(file))
	except:
		print("Could Not Understand!!")
		pass


#MOVE, COPY AND HIDE DIRECTORIES ( ** 3 functions **) ( --RETURNS NOTHING-- )
#MOVE
def move_dir():
	dir_name=ask_name()
	print(dir_name)
	dir_loc=ask_path()
	print('Can you tell me the location where do you want to move it?')
	final_loc=ask_path()
	
	os.system('mv '+dir_loc+'/'+dir_name+' '+final_loc+'/'+dir_name)

#COPY
def copy_dir():
	dir_name=ask_name()
	print(dir_name)
	dir_loc=ask_path()
	print('Can you tell me the location where do you want to copy it?')
	final_loc=ask_path()
	
	os.system('cp '+dir_loc+'/'+dir_name+' '+final_loc+'/'+dir_name)

#HIDE
def hide_dir():
	dir_name=ask_name()
	print(dir_name)
	dir_loc=ask_path()
		
	os.system('mv '+dir_loc+'/'+dir_name+' '+dir_loc+'/.'+dir_name)

#EMPTY
def empty_folder():
	dir_name=ask_name()
	path=ask_path()
	final_path=path+'/'+dir_name+"/*"
	confirm=confirmation_ask()
	if (confirm=="yes") or (confirm=="ya") or (confirm=="sure"):
		os.system("rm -r "+final_path)


#PLAYS SONGS ON YOUTUBE ( --RETURNS NOTHING-- )
def youtube_play():
	r=sr.Recognizer()

	with sr.Microphone() as  source:
		r.adjust_for_ambient_noise(source)
		print ("What is your favroute song?")
		audio=r.listen(source)

	try:
		speak=r.recognize_google(audio)
		
		#VOICE DATA CLEANING
		final_string=''
		stripped_data=speak.strip()	#____Removing extra spaces
		final_data=stripped_data.split()#____Fetching individual words
		print(final_data)
		
		#CREATING USABLE LINK FROM CLEANED DATA
		for i in final_data:
			final_string=final_string+i+'+'	
		last=len(final_string)
		final_string=final_string[:last-1]
		url_new="http://www.youtube.com/results?search_query="+final_string
		print (url_new)
		
		#SCRAPPING FOR USEABLE LINK
		page = requests.get(url_new)
		
		html_source=page.text
		#print(html_source)
		
		link_code=html_source.find('watch?v=')
		end_quote=html_source.find('"',link_code)
		watch_link=html_source[link_code:end_quote]
		print(watch_link)
		
		#OPENING THE LINK(PLAYING SONG)
		print('Playing '+speak)
		wb.open_new_tab('http://www.youtube.com/'+watch_link)
			
	except:
		print("Could Not Understand!!")
		pass


#SEARCH THROUGH WEB ( --RETURNS NOTHING-- )	
def web_search():
	r=sr.Recognizer()

	with sr.Microphone() as  source:
		r.adjust_for_ambient_noise(source)
		print ("What do you wanna search?")
		audio=r.listen(source)

	try:
		speak=r.recognize_google(audio)
		
		#VOICE DATA CLEANING
		final_string=''
		stripped_data=speak.strip()	#____Removing extra spaces
		final_data=stripped_data.split()#____Fetching individual words
		print(final_data)
		
		#CREATING USABLE LINK FROM CLEANED DATA
		for i in final_data:
			final_string=final_string+i+'+'	
		last=len(final_string)
		final_string=final_string[:last-1]
		url_new="http://www.google.com/search?q="+final_string
		print (url_new)
		
		#OPENING THE LINK(i.e. SEARCHING GOOGLE)
		print('Searching '+speak+' on google...')
		wb.open_new_tab(url_new)
			
	except:
		print("Could Not Understand!!")
		pass


 	## MAIN PART ## -----------------------------------------------------------------------------------------------------------------


#INITIAL INTRACTION WITH USER
with sr.Microphone() as  source:
	r.adjust_for_ambient_noise(source)
	print ("Heyyy, Whatsup chief!!!")
	print("How can i help you?")	
	audio=r.listen(source)

try:
	
	speech_ip=r.recognize_google(audio)	#speech_ip --> VOICE INPUT
	print(speech_ip)
	
	#VOICE DATA CLEANING
	stripped_data=speech_ip.strip()		#____Removing extra spaces
	data=stripped_data.split()		#____Fetching individual words spoken
	data=tolower(data)
	print(data)
	
	#DICTIONARY CHECKING FOR KEYWORDS
	operation,op_type,count_type,file_details,dir_op,web_op=check_dict(data)
	print(operation,op_type,count_type,file_details,dir_op,web_op)
	
	if operation=='mk' and op_type=='dir':		#CREATE DIR		<check ok>
		create_dir()
	elif operation=='rm' and op_type=='dir':	#REMOVE DIR		<check ok>
		remove_dir()
	elif ('rename' in data) and op_type=='dir':	#RENAME DIR		<check ok>
		rename_dir()
	elif count_type=='num' and operation == 'null':	
		if op_type=='dir':
			## folder
			count_dir()			#COUNT DIR		<check ok>
		elif op_type=='fi':
			## files
			count_file()			#COUNT FILES		<check ok>
		else :
			## files+folder
			count_dir()
			count_file()
	elif count_type=='li' and operation == 'null':
		#if op_type=='dir':
			## list directories and files
		list_dir()				#LIST DIR		<check ok>
	elif file_details=='md':
		show_properties()			#SHOW PROPERTIES	<check ok>
	elif dir_op=='mv' and op_type=='dir':
		move_dir()				#MOVE DIR		<check ok>
	elif dir_op=='cp' and op_type=='dir':
		copy_dir()				#COPY DIR		<check ok>
	elif dir_op=='hd' and op_type=='dir':
		hide_dir()				#HIDE DIR		<check ok> 
	elif dir_op=='emty' and op_type=='dir':
		empty_folder()				#EMPTY A DIR		<check ok>
	elif web_op=='ply' and operation=='null':
		youtube_play()				#PLAY SONG ON YOUTUBE	<check ok>
	elif web_op=='srch' and operation=='null':
		web_search()				#SEARCH QUERY ON WEB	<check ok>

	else :
		#print("I have been designed to perform directory operations, not to handle your BULLSHIT!!!")
		print("\nSeriously, what do you think i am? A Freakin GOD.")
		print("\nI am KIRA, get that stuck in your head.\n")
	
except:
	print("Could Not Understand!!")
	pass



