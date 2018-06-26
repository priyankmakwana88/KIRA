#!/usr/bin/python3

import os
import time
import pwd
import grp


file = '/home/priyank/Desktop/myNapster.py'


#____ to find the properties of the file
info = os.stat(file)
#print(info)

# to find permission in octal
per = str(oct(os.stat(file)[0]))[5:8]

#________ initalize the empty list to contain the permissions
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

#print(per_mode)           #_____________ print permissions in english!!!!!!!!!!!!

# to find owner name from owner id:-

uid = info.st_uid   # get the owner uid number
#print(uid)
userinfo = pwd.getpwuid(uid)[0]  #________ get the owner name from owner id

#_____________________ complete ___________ user_name______________________


# to find group name from group id:-

gid = info.st_gid   # get the owner uid number
#print(gid)
groupinfo = grp.getgrgid(gid)[0]  #________ get the owner name from owner id

#_____________________ complete ___________ group_name______________________




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


