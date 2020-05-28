#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import base64
import requests
import os, sys
import subprocess
import socket
from time import sleep

# Lets give a hand to the python2'ers
try: input = raw_input
except: pass

_version_ = 0.7

# Give some beauty colors
RED = '\033[1;31m'
BLUE = '\033[94m'
BOLD = '\033[1m'
GREEN = '\033[32m'
YELLOW = '\033[33m'
END = '\033[0m'

def git_https_force():
	subprocess.Popen('git config --global url."https://github.com/".insteadOf git@github.com:;git config --global url."https://".insteadOf git://', shell=True).wait()

def self_update():
	# force https
	git_https_force()

	# try to update ourself first
	print("Trying to update myself first.. Then starting framework.")
	subprocess.Popen("git pull", shell=True).wait()
	sleep(2)

def check_internet():
	"""
	Check for internet access.
	"""
	try:
		print(YELLOW + "[i] Checking for an Internet connection..."+ END)
		rhost = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
		rhost.connect(('google.com', 0))
		rhost.settimeout(2)
		return 1

	except Exception:
		return 0


def help_menu():
	print("Some commands:")
	print("-h  or  --help\t Displays this help menu")
	print("| Skip the internet connection and just run")
	print("| --no-internet")
	print("| --no-check-internet")
	print("--"*30)
	print("Usage: python %s [commands] <number>*" % sys.argv[0])
	print("*The number is how many codes you want to generate")

# Who doesn't use a banner?
def banner():
	banner = RED + """                                                                                                                                                                                                     
	██╗  ██╗ █████╗  ██████╗██╗  ██╗████████╗██╗  ██╗███████╗██████╗  ██████╗ ██╗  ██╗
	██║  ██║██╔══██╗██╔════╝██║ ██╔╝╚══██╔══╝██║  ██║██╔════╝██╔══██╗██╔═══██╗╚██╗██╔╝
	███████║███████║██║     █████╔╝    ██║   ███████║█████╗  ██████╔╝██║   ██║ ╚███╔╝ 
	██╔══██║██╔══██║██║     ██╔═██╗    ██║   ██╔══██║██╔══╝  ██╔══██╗██║   ██║ ██╔██╗ 
	██║  ██║██║  ██║╚██████╗██║  ██╗   ██║   ██║  ██║███████╗██████╔╝╚██████╔╝██╔╝ ██╗
	╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝   ╚═╝   ╚═╝  ╚═╝╚══════╝╚═════╝  ╚═════╝ ╚═╝  ╚═╝
	██╗███╗   ██╗██╗   ██╗██╗████████╗███████╗                        
	██║████╗  ██║██║   ██║██║╚══██╔══╝██╔════╝                        
	██║██╔██╗ ██║██║   ██║██║   ██║   █████╗                          
	██║██║╚██╗██║╚██╗ ██╔╝██║   ██║   ██╔══╝                          
	██║██║ ╚████║ ╚████╔╝ ██║   ██║   ███████╗                        
	╚═╝╚═╝  ╚═══╝  ╚═══╝  ╚═╝   ╚═╝   ╚══════╝   
	"""
	banner += RED + """[+] Version: """ + END + YELLOW + str(_version_) + "\n"+ END
	banner += GREEN + "\t[+] hackthebox.eu Invite Code Generator\n" + END
	banner += GREEN + "\t[+] Author: AgentWhite (@_agentwhite_)\n" + END
	banner += GREEN + "\t[+] Website: https://thegibson.xyz\n" + END
	banner += YELLOW +"\t[+] World Designed By Technology Is A World Designed To Be Broken.\n" + END
	banner += RED + "\t-----------------------------------------------------------------------------\n" + END
	banner += BOLD + BLUE + """
	This was meant to help generate an invite code for HTB (hackthebox.eu)
	This is kind of cheating since getting the invite code will be the 'first'
	hack you will do on the platform but also on the actual HTB.
	So I encourage you to not use this script but rather do it yourself""" + END	

	return banner

# Ummmm... Still need explanation what this function does?
# Thanks to Argagel (https://github.com/artagel) who got this to work.
def get_code(num):
	try:
		sleep(0.5)
		print("[!] Here are your codes you requested:")
		for i in range(int(num)):
			#os.system("bash code.sh")
			r = requests.post('https://www.hackthebox.eu/api/invite/generate', headers={ 
				"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36"
			})
			resp = r.json()
			code = resp.get('data', {}).get('code', '')
			print(YELLOW + "\t" + base64.b64decode(code).decode() + END)
	except ValueError:
		help_menu()
		sys.exit()

if __name__ == "__main__":
	os.system("cls||clear")
	print(banner())

	if '-h' in sys.argv or '--help' in sys.argv:
		help_menu()
		sys.exit()
	try:
		if "--no-internet" not in sys.argv[1:] or "--no-check-internet" not in sys.argv[1:]:
			# check internet connection
			if check_internet() == 0:
				print(RED + """
Unable to detect Internet connection. Needed for HTB Invite Code Generator.
We will now exit. Launch again when you got a connection.
You can also run ptf with the --no-internet or --no-check-internet\nargument to bypass the network check.
				""" + END)
				sys.exit()
			else:
				print(GREEN + "[i] Found an internet connection..." + END)
				get_code(sys.argv[-1])
		else:
			print("[i] Skipping internet connection test...")
			# Grab latest update if any
			self_update()
			os.system("cls||clear")
			print(banner())
			get_code(sys.argv[-1])
	except IndexError as error:
		print(error)
		help_menu()
		sys.exit()
	except ValueError as error:
		print(error)
		help_menu()
		sys.exit()
