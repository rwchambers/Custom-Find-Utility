#!/usr/bin/python2.7

import os, sys, argparse, re
from stat import *

parser = argparse.ArgumentParser()
parser.add_argument('buff', help ='buff help')
parser.add_argument('-grep', help='grep help')
parser.add_argument('-name', help='name help')
args = parser.parse_args()

count = 0

def walktree(top, callback):
    
	for f in os.listdir(top):
		global count
		count = 0
		if args.name and args.grep:
			with open(os.path.join(top, f),'r') as files:
				for words in files:
					count += 1
					if re.match(args.name,f) and re.search(args.grep,words):
						print os.path.join(top, f),'',count,' : ',words, 
			pathname = os.path.join(top, f)
		elif args.grep:
			with open(os.path.join(top, f),'r') as files:
				for words in files:
					count += 1
					if re.search(args.grep,words):
						print os.path.join(top, f),'',count,' : ',words, 
			pathname = os.path.join(top, f)	
		elif args.name:
			count += 1
			if re.match(args.name,f):
				print os.path.join(top, f),'',count,' : ',f
			pathname = os.path.join(top, f)
		else:
			count += 1
			print os.path.join(top, f),'',count,' : ',f
			pathname = os.path.join(top, f)
        
		mode = os.stat(pathname).st_mode
   
		if S_ISDIR(mode):
	   	# It's a directory, recurse into it
			walktree(pathname, callback)
		elif S_ISREG(mode):
	   	# It's a file, call the callback function
			callback(pathname)
		else:
	   	# Unknown file type, print a message
	  		print 'Skipping %s' % pathname

def visitfile(file):
	pass
#	print file
	
if __name__ == '__main__':
	walktree(args.buff, visitfile)

