#!/usr/bin/python

import telnetlib
import re
#import sys

#values = int(sys.argv[1])

from __main__ import *

def telNetCall():
    global output
    host  = "172.30.0.100"
    telnet  = telnetlib.Telnet(host, 3001) 

    telnet.write('RAAE\n')
    
    telnet.write('DIS\n')
    txt = telnet.read_all()

    re1='.*?'		# Non-greedy match on filler
    re2='\\d+'		# Uninteresting: int
    re3='.*?'		# Non-greedy match on filler
    re4='\\d+'		# Uninteresting: int
    re5='.*?'		# Non-greedy match on filler
    re6='\\d+'		# Uninteresting: int
    re7='.*?'		# Non-greedy match on filler
    re8='\\d+'		# Uninteresting: int
    re9='.*?'		# Non-greedy match on filler
    re10='\\d+'		# Uninteresting: int
    re11='.*?'		# Non-greedy match on filler
    re12='\\d+'		# Uninteresting: int
    re13='.*?'		# Non-greedy match on filler
    re14='\\d+'		# Uninteresting: int
    re15='.*?'		# Non-greedy match on filler
    re16='\\d+'		# Uninteresting: int
    re17='.*?'		# Non-greedy match on filler
    re18='\\d+'		# Uninteresting: int
    re19='.*?'		# Non-greedy match on filler
    re20='\\d+'		# Uninteresting: int
    re21='.*?'		# Non-greedy match on filler
    re22='\\d+'		# Uninteresting: int
    re23='.*?'		# Non-greedy match on filler
    re24='\\d+'		# Uninteresting: int
    re25='.*?'		# Non-greedy match on filler
    re26='\\d+'		# Uninteresting: int
    re27='.*?'		# Non-greedy match on filler
    re28='\\d+'		# Uninteresting: int
    re29='.*?'		# Non-greedy match on filler
    re30='\\d+'		# Uninteresting: int
    re31='.*?'		# Non-greedy match on filler
    re32='(\\d+)'	# Integer Number 1
    re33='.*?'		# Non-greedy match on filler
    re34='(\\d+)'	# Integer Number 2
    re35='.*?'		# Non-greedy match on filler
    re36='(\\d+)'	# Integer Number 3
    re37='.*?'		# Non-greedy match on filler
    re38='(\\d+)'	# Integer Number 4
    re39='.*?'		# Non-greedy match on filler
    re40='(\\d+)'	# Integer Number 5
    re41='.*?'		# Non-greedy match on filler
    re42='(\\d+)'	# Integer Number 6
    re43='.*?'		# Non-greedy match on filler
    re44='(\\d+)'	# Integer Number 7
    re45='.*?'		# Non-greedy match on filler
    re46='(\\d+)'	# Integer Number 8
    re47='.*?'		# Non-greedy match on filler
    re48='(\\d+)'	# Integer Number 9
    re49='.*?'		# Non-greedy match on filler
    re50='\\d+'		# Uninteresting: int
    re51='.*?'		# Non-greedy match on filler
    re52='(\\d+)'	# Integer Number 10
    re53='.*?'		# Non-greedy match on filler
    re54='(\\d+)'	# Integer Number 11
    re55='.*?'		# Non-greedy match on filler
    re56='(\\d+)'	# Integer Number 12
    re57='.*?'		# Non-greedy match on filler
    re58='(\\d+)'	# Integer Number 13
    re59='.*?'		# Non-greedy match on filler
    re60='(\\d+)'	# Integer Number 14
    re61='.*?'		# Non-greedy match on filler
    re62='(\\d+)'	# Integer Number 15
    re63='.*?'		# Non-greedy match on filler
    re64='(\\d+)'	# Integer Number 16

    rg = re.compile(re1+re2+re3+re4+re5+re6+re7+re8+re9+re10+re11+re12+re13+re14+re15+re16+re17+re18+re19+re20+re21+re22+re23+re24+re25+re26+re27+re28+re29+re30+re31+re32+re33+re34+re35+re36+re37+re38+re39+re40+re41+re42+re43+re44+re45+re46+re47+re48+re49+re50+re51+re52+re53+re54+re55+re56+re57+re58+re59+re60+re61+re62+re63+re64,re.IGNORECASE|re.DOTALL)

    m = rg.search(txt)

    if m:
        int1=m.group(1)
        int2=m.group(2)
        int3=m.group(3)
        int4=m.group(4)
        int5=m.group(5)
        int6=m.group(6)
        int7=m.group(7)
        int8=m.group(8)
        int9=m.group(9)
        int10=m.group(10)
        int11=m.group(11)
        int12=m.group(12)
        int13=m.group(13)
        int14=m.group(14)
        int15=m.group(15)
        int16=m.group(16)
        
 	atten_str = int1+","+int2+","+int3+","+int4+","+int5+","+int6+","+int7+","+int8+","+int9+","+int10+","+int11+","+int12+","+int13+","+int14+","+int15+","+int16
        
	values = atten_str.split(',')
        
        #for x in output: 
	    #return x

	return values

        #return output[0]

telNetCall()


