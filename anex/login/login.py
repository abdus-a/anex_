def login(uname, upass, usrname, pwd):
	try:
		usi = usrname.index(uname)
		if (pwd.index(upass) == usi):
			print("Welcome")
			cookies = {'USERNAME_': uname, 'PASSWORD_': upass, 'LOGIN_S': True}
			return cookies

		else:
			print("wrong username or password")
	except:
		print("wrong username or password")
