from time import gmtime, strftime
import os, sys, time
os.system("sh termux")
print '==================================================='
os.system("echo ~~Clock script")
os.system("echo Requirements is Finded")
os.system("python speed.py")
print '==================================================='
print '[Made by Alu from One Evo]'
print '[Copyright will get banned]'
data = strftime("[Year]%Y\n[Month]%m\n[Day]%d\n[Clock] %H:%M:%S", gmtime())
total = time.time()
os.system("echo Loading data")
totol = time.time() -total
bk = ('Speed cmd:%s' % (totol))
print (data)
print (bk)

