
# check if password has at least 1 uppercase i lowercase 1 number 1 special character and at least 8 characters long

import re

def is_pwd_strong(pwd):
	# print len(pwd)
	if re.search(r'^(?=.*\W)(?=.*[0-9])(?=.*[a-z])(?=.*[A-Z]).{8,20}$', pwd):
		return True
	return False


assert is_pwd_strong('******aA&&^%$7899871') == True
assert is_pwd_strong('*zA0$!@') == False
