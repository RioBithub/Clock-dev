from time import gmtime, strftime
import random, os, sys, time, argparse
os.system("sh termux")
print ('===================================================')
wait = {
    "user":True
       }
os.system("echo ~~Clock script")
os.system("echo Requirements is Finded")
os.system("python speed.py")
print ('===================================================')
print ('[Made by Alu from One Evo]')
print ('[Copyright will get banned]')
data = strftime("[Year]%Y\n[Month]%m\n[Day]%d\n[Clock] %H:%M:%S", gmtime())
total = time.time()
os.system("echo Loading data")
os.system("echo Importing data")
totol = time.time() -total
bk = ('Speed cmd:%s' % (totol))
print (data)
print (bk)

if wait["user"] == True:
    print ('You using a pro service')

parser = argparse.ArgumentParser() 
parser2 = argparse.ArgumentParser()
parser.add_argument('-info', help='See info about me')
parser2.add_argument('-datenow', help='See date only')
args = parser.parse_args()
args2 = parser2.parse_args()

foo = ['code:5845686', 'code:37737474', 'code:747473745', 'code:47473737450','code:1039384','code:47477437'] 
from random import randrange 
random_index = randrange(0,len(foo))
print foo[random_index]
