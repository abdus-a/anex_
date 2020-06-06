'''
[e.0]: main login system error probable cause TypeError, Logs avi (Crash System=False, return loginpage)
[e.11]: relog password error probable cause TypeError, NO LOGS avai

'''
# imports
import os # system wide
import loger # local
from loger import log__
from anexB import * # local
import sys # system wide
sys.path.insert(1, '../login/')
from info import * # local ^
from login import * # local ^^
import time # system wide

def relog(): # used for re-loging
	uname = str(input("Username: "))
	upass = str(input("Password: "))
	SysExcec(login(uname,upass,usrname,pwd)) # Local

def SysExcec(coockies_):
	try: # atempts to login to terminal
		if (coockies_['LOGIN_S'] == True):
			usernamestr = coockies_['USERNAME_']
			browser_on = False # sets local Browser var false for proper execution
			while (coockies_['LOGIN_S'] == True):
				localtime = time.asctime(time.localtime(time.time()))
				log__('./OS/oslog.txt', f'''
OS_time: {localtime};
SYS_output: < {coockies_['USERNAME_']} Loged in;
					''')

				userin = input(f"{usernamestr}:~$ ") # main input str
				if (userin == "poweroff"): 
					print("poweroff...")
					localtime = time.asctime(time.localtime(time.time()))
					log__('./OS/oslog.txt', f'''
OS_time: {localtime};
OS_function: {userin};
SYS_output: > System Poweroff;
							''')
					coockies_['LOGIN_S'] = False		
				elif (userin == "browser"): # browser Output requiers a display/GUI
					browser_on = True
					while browser_on == True:
						Browser_input = input(f"{usernamestr}[anexB]:~$ ")
						localtime = time.asctime(time.localtime(time.time()))
						log__('./OS/oslog.txt',f'''
OS_time: {localtime};
OS_function:{userin};
SYSTEM_CALL: < Browser <!Requirment GUI>;
URL: {Browser_input};
							''')

						if Browser_input == "exit":
							browser_on = False
						OpenB(Browser_input)
					localtime = time.asctime(time.localtime(time.time()))
					log__('./OS/oslog.txt', f'''
OS_time: {localtime};
OS_function: {userin};
SYS_output: ! System was online;
							''')
				elif(userin == "show sys_log"):
					if (coockies_['USERNAME_']) == ('root'):
						root_inp_pass = input("root password: ")
						if root_inp_pass == pwd[0]:
							os.system('cat ./OS/oslog.txt')
						elif root_inp_pass != pwd[0]:
							print("incorect password")

					elif ((coockies_['USERNAME_']) != ('root')):
						print("This action requiers root Privlages")
						localtime = time.asctime(time.localtime(time.time()))
						log__('./OS/oslog.txt', f'''
OS_time: {localtime};
OS_function: {userin};
OS_alert: {coockies_['USERNAME_']} Tried to view System logs.;
SYS_output: > This action requiers root Privlages;
							''')
				elif (userin == "clear sys_log"):
					if (coockies_['USERNAME_']) == ('root'):
						root_input_pass = input("root password: ")
						if root_input_pass == pwd[0]:
							f = open('./OS/oslog.txt', 'w')
							f.write("")
							f.close()
							print("cleared logs!!!!")
						elif root_inp_pass != pwd[0]:
							print("incorect password")
					elif (coockies_['USERNAME_']) != ('root'):
						print("This action requiers root Privlages")
						localtime = time.asctime(time.localtime(time.time()))
						log__('./OS/oslog.txt', f'''
OS_time: {localtime};
OS_function: {userin};
OS_alert: {coockies_['USERNAME_']} Tried to clear System logs.;
SYS_output: > This action requiers root Privlages;
						''')


				elif(userin == ">logout"):
					try:
						localtime = time.asctime(time.localtime(time.time()))
						log__('./OS/oslog.txt', f'''
OS_time: {localtime};
OS_function: {userin};
SYS_output: < User {coockies_['USERNAME_']} Loged out
							''')

						relog()	
					except TypeError as e :
						localtime = time.asctime(time.localtime(time.time()))
						log__('./OS/oslog.txt', f'''
OS_time: {localtime};
OS_function: {userin};
OS_Error: {e};
SYS_output: >! System Poweroff: Dew to faital System error; [e.11]
							''')
						print("System Poweroff: Dew to faital System error; [e.11]")
				elif(userin == "clear" or "cls"):
					os.system("clear")
										
		else:
			print("error!!!!")
	except TypeError as e:
		localtime = time.asctime(time.localtime(time.time()))
		log__('./OS/oslog.txt', f'''
OS_time: {localtime};
OS_Error: {e};
SYS_output: >! System Poweroff: Dew to faital System error; [e.0]
							''')
		relog()
