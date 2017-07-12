#!/bin/python

import urllib.request

def update(filename_download, filename_write):
	
	# Var.
	url = "https://premproxy.com/list/ip-port/1.htm"
	search_begin = "	<!-- IP:Port list -->"
	search_end = "</pre>"
	i = 0
	
	# Get file
	get_html = urllib.request.urlretrieve(url, filename_download)


	# Read file
	with open(filename_download, "r") as function:

		# Search in all lines and increments i
		for line in function:
			i = i + 1
			if search_begin in line:
				search_begin_index = i
			if search_end in line:
				search_end_index = i - 1

	# Parse file
	with open(filename_download, "r") as function:
		ip_list = function.readlines()
	
		server_list = ""

		for i in range(search_begin_index, search_end_index):
			ip_list[i] = ip_list[i].replace(":", " ")
			server_list = server_list + ip_list[i]
	
	# Write file
	with open(filename_write, "w") as function:
		function.write(server_list)
