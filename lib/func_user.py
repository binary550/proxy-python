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
def exec(directory, program, lenght):
	program = directory + "/" + program + " " + " ".join(sys.argv[lenght:])
	os.system(program)
	
	
