#!/bin/python

import sys
import os

# Func. help message
def help():
	print(
	"""
Usage: proxy-python [OPTION]... [PROGRAM]...
Change proxy to a random server found in data file or from premproxy.net

  -c, --choose     manual proxy           [protocol server port]
  -r, --random     random proxy
  -u, --update     update proxy list
  -l, --list       show available proxy
  -h, --help       display this help
"""
)

# Func. error message
def error():
	print(
	"""
 * Internal error..
 Try 'proxy-python -h' to see help.
"""
)


# Func. user exec
def exec(directory, program, proxy_conf, lenght):
	program = directory + "proxychains -f " + proxy_conf + " " + directory + program + " " + " ".join(sys.argv[lenght:])
	
	#os.system("/usr/bin/curl -s checkip.amazonaws.com")
	
	# Check if proxy is online
	proxy_ip = directory + "proxychains -q -f " + proxy_conf + " " + directory + "curl -s checkip.amazonaws.com > /dev/null"
	#proxy_up = os.system(proxy_ip)

	if os.system(proxy_ip) == 0:
		print("[OK] Proxy server online")
		print("[OK] Connected to proxy\n")
		os.system(program)
	
	else:
		print("[ERR] Proxy server is offline\n")
