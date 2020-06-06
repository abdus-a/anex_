import sys
sys.path.insert(1, './login/')
from info import *
from login import *
sys.path.insert(1, './OS/')
from OSSYS import *


uname = str(input("Username: "))
upass = str(input("Password: "))


SysExcec(login(uname,upass,usrname,pwd))
