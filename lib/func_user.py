#!/bin/python

import sys

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
