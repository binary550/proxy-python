#!/bin/python

import sys
sys.path.insert(0, "lib")
import func_user
import func_open
import func_proxy

# Var.
proxy_file = "data/list"
proxy_conf = "data/proxychains.conf"
proxy_template = "data/proxychains.template"


# Main Program
if len(sys.argv) > 1:

	# Manual Proxy
	if sys.argv[1] == "-c" or sys.argv[1] == "--choose":
		func_proxy.manual(proxy_conf, proxy_template)

	# Random Proxy
	elif sys.argv[1] == "-r" or sys.argv[1] == "--random":
		func_proxy.random(proxy_file, proxy_conf, proxy_template)

	# Update Proxy list
	elif sys.argv[1] == "-u" or sys.argv[1] == "--update":
		func_proxy.update()

	# Show Available Proxy
	elif sys.argv[1] == "-l" or sys.argv[1] == "--list":
		func_proxy.list()

	# Display Help
	elif sys.argv[1] == "-h" or sys.argv[1] == "--help":
		func_user.help()
	
	else:
		func_user.error()


# Show error info
else:
	func_user.error()
