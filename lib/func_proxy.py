#!/bin/python

import sys
from random import randrange

# Func. write
def write(filename_template, filename_conf, proxy_info):
	
	# Read
	with open(filename_template, "r") as function:
		proxy_content = function.readlines()
		proxy_line = len(proxy_content)
	
	# Replace proxy info
	proxy_content[proxy_line - 1] = proxy_info

	# Write
	with open(filename_conf, "w") as function:
		function.writelines(proxy_content)

# Func. manual proxy
def manual(filename_conf, filename_template):
	if len(sys.argv) == 5:
		
		# Get sys. argument
		protocol = sys.argv[2]
		server = sys.argv[3]
		port = sys.argv[4]

		# Create proxy info
		proxy_info = protocol + " " + server + " " + port

		# Write
		write(filename_template, filename_conf, proxy_info)

# Func. random proxy
def random(filename_list, filename_conf, filename_template):
	with open(filename_list, "r") as function:

		# Parse 
		proxy_list = function.readlines()
		proxy_list = [x.strip() for x in proxy_list]
		
	# Random
	proxy_len = len(proxy_list)
	proxy_random = randrange(0, proxy_len)
	proxy_info = proxy_list[proxy_random]
	
	write(filename_template, filename_conf, proxy_info)
