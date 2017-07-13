#!/bin/python


# Func. read proxy list
def read(filename):
	with open(filename, "r") as function:
		print(function.read())


# Func. write proxy list
def write(filename, protocol, server, port):
	with open(filename," w") as function:
		
		info = protocol + " " + server + " " + port

		text = "strict_chain\nremote_dns_subnet 224\n"
		text = text + "\ntcp_read_time_out 15000\ntcp_connect_time_out 15000\n"
		text = text + "\n[ProxyList]\n" + info + "\n "

		function.write(text)
		
