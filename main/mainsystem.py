#script_by_alu_from_oneevo

from time import gmtime, strftime
import random, os, sys, time, argparse
os.system("sh termux")
print ('===================================================')
wait = {
    "user":False,
    "tps":False
       }
os.system("echo ~~Clock script")
os.system("echo Requirements is Finded")
os.system("python speed.py")
print ('===================================================')
print ('[Made by Alu from One Evo]')
print ('[Copyright will get banned]')
data = strftime("[Year]%Y\n[Month]%m\n[Day]%d\n[Clock] %H:%M:%S", gmtime())
total = time.time()
print ('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
os.system("echo Loading data")
os.system("echo Importing data")
totol = time.time() -total
bk = ('Speed cmd:%s' % (totol))

if wait["user"] == True:
    print ('permission is granted')
if wait["user"] == False:
    print ('permission not granted')

permission_granted = 'Permission is granted :D'

print ('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
parser = argparse.ArgumentParser() 
parser2 = argparse.ArgumentParser()
parser.add_argument('-info', help='See info about me')
parser2.add_argument('-datenow', help='See date only')
args = parser.parse_args()
args2 = parser2.parse_args()

foo = ['code:5845686', 'code:37737474', 'code:747473745', 'code:47473737450', 'code:1039384','code:47477437', 'code:447377', 'code:20945820', 'code:10485830'] 
from random import randrange 
random_index = randrange(0,len(foo))

if wait["tps"] == False:
    print('Permission Code is exploiting') #(/require termux
    wait["user"] = True

if wait["user"] == True:
    print foo[random_index]
    print(permission_granted)
print ('{D}{E}{V} \n%s' % data)
print (bk)
print (totol)
os.system("echo Supported by First Step")

#end_of_main_system_don't_remove_this_file
