import requests
from huepy import *
form time import *
print (green(""" _____                       _     
/ _  / ___  _ __   ___      | |__  
\// / / _ \| '_ \ / _ \_____| '_ \ 
 / //\ (_) | | | |  __/_____| | | |
/____/\___/|_| |_|\___|     |_| |_|
#Developed by PiCarO                                   
"""))
attacktype=raw_input("Choose 1 for Single 2 for Mass : ")
def single(attacker,web):
	url="http://zone-h.com/notify/single"
	payload={'defacer':attacker,'domain1':web,'hackmode':1,'reason':1}
	r=requests.post(url,data=payload)
	if 'OK' in r.text:
		print (good("Done Posting !"))
	else:
		print(bad("Invalid Domain or domain has been defaced !"))
def mass(attacker,lists):
	with open(lists,'r') as f:
		f=f.readlines()
		url="http://zone-h.com/notify/single"
		for i in range(len(f)):
			payload={'defacer':attacker,'domain1':f[i].strip('\n'),'hackmode':1,'reason':1}
			r=requests.post(url,data=payload,headers={"Referer": "http://www.zone-h.org/"})
			if 'OK' in r.text:
				print (good("Done Posting ! "+f[i].strip('\n')))
			else:
				print(bad("Invalid Domain or domain has been defaced ! "+f[i].strip('\n')))
		sleep(3)
		print "......."
		sleep(3)
		print (info("Enjoy my tool and give me stars fuck you!"))
if attacktype=="1":
	name=raw_input("Attacker Name : ")
	url=raw_input("Attacked website : ")
	single(name,url)
if attacktype=="2":
	name=raw_input("Attacker Name : ")
	url=raw_input("website list : ")
	mass(name,url)
