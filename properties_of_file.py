#!/usr/bin/python3

import os
import time
import pwd
import grp


file = '/home/pranav/Desktop/adhcsummer/dir_operations/proper.py'


#____ to find the properties of the file
info = os.stat(file)
#print(info)

# to find permission in octal
per = str(oct(os.stat(file)[0]))[5:8]

#________ initalize the empty list to contain the permissions
per_mode=[]

for i in range(0,len(per)):
	if per[i]=='0':
		per_mode.append('No Permission')
	elif per[i]=='1':
		per_mode.append('Only Execute Permission')
	elif per[i]=='2':
		per_mode.append('Only Write Permission')
	elif per[i]=='3':
		per_mode.append('Write, Executive Permission')
	elif per[i]=='4':
		per_mode.append('Only Read Permission')
	elif per[i]=='5':
		per_mode.append('Read, Execute Permission')
	elif per[i]=='6':
		per_mode.append('Read, Write Permission')
	else :
		per_mode.append('All Permission')

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



print('')
print('File\'s Location   :', file)
print('')
print('User\'s name	   : ',userinfo)
print('Group\'s name	   : ',groupinfo)
print('User\'s  permission : ',per_mode[0])
print('Group\'s permission : ',per_mode[1])
print('Other\'s permission : ',per_mode[2])
print('Access time        : ', time.ctime(os.path.getatime(file)))
print('Modified time      : ', time.ctime(os.path.getmtime(file)))
print('Change time        : ', time.ctime(os.path.getctime(file)))
print('Size         	   : ', os.path.getsize(file),"Bytes")


