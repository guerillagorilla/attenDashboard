#!/usr/bin/python
# URL that generated this code:
# http://txt2re.com/index-python.php3?s=50PA-684%20Connection%20Open%20Checksum%20=%209A09%20Atten%20%201%20%2087%20Atten%20%202%20%2087%20Atten%20%203%20127%20Atten%20%204%20127%20Atten%20%205%20%20%207%20Atten%20%206%20%20%207%20Atten%20%207%20127%20Atten%20%208%20127%20Atten%20%209%20%2026%20Atten%2010%20%2026%20Atten%2011%20127%20Atten%2012%20127%20Atten%2013%20127%20Atten%2014%20127%20Atten%2015%20127%20Atten%2016%20127%20Checksum%20=%209A09&71&110&111&72&112&42&113&43&114&116&115&117&118&44&119&45&121&68&61&69&62&46&63&47&64&48&65&49&66&50&67&51

import re

txt='50PA-684 Connection Open Checksum = 9A09 Atten  1  87 Atten  2  87 Atten  3 127 Atten  4 127 Atten  5   7 Atten  6   7 Atten  7 127 Atten  8 127 Atten  9  26 Atten 10  26 Atten 11 127 Atten 12 127 Atten 13 127 Atten 14 127 Atten 15 127 Atten 16 127 Checksum = 9A09'

re1='.*?'	# Non-greedy match on filler
re2='\\d+'	# Uninteresting: int
re3='.*?'	# Non-greedy match on filler
re4='\\d+'	# Uninteresting: int
re5='.*?'	# Non-greedy match on filler
re6='\\d+'	# Uninteresting: int
re7='.*?'	# Non-greedy match on filler
re8='\\d+'	# Uninteresting: int
re9='.*?'	# Non-greedy match on filler
re10='(\\d+)'	# Integer Number 1
re11='.*?'	# Non-greedy match on filler
re12='(\\d+)'	# Integer Number 2
re13='.*?'	# Non-greedy match on filler
re14='(\\d+)'	# Integer Number 3
re15='.*?'	# Non-greedy match on filler
re16='(\\d+)'	# Integer Number 4
re17='.*?'	# Non-greedy match on filler
re18='(\\d+)'	# Integer Number 5
re19='.*?'	# Non-greedy match on filler
re20='(\\d+)'	# Integer Number 6
re21='.*?'	# Non-greedy match on filler
re22='(\\d+)'	# Integer Number 7
re23='.*?'	# Non-greedy match on filler
re24='(\\d+)'	# Integer Number 8
re25='.*?'	# Non-greedy match on filler
re26='(\\d+)'	# Integer Number 9
re27='.*?'	# Non-greedy match on filler
re28='(\\d+)'	# Integer Number 10
re29='.*?'	# Non-greedy match on filler
re30='(\\d+)'	# Integer Number 11
re31='.*?'	# Non-greedy match on filler
re32='(\\d+)'	# Integer Number 12
re33='.*?'	# Non-greedy match on filler
re34='(\\d+)'	# Integer Number 13
re35='.*?'	# Non-greedy match on filler
re36='(\\d+)'	# Integer Number 14
re37='.*?'	# Non-greedy match on filler
re38='(\\d+)'	# Integer Number 15
re39='.*?'	# Non-greedy match on filler
re40='(\\d+)'	# Integer Number 16
re41='.*?'	# Non-greedy match on filler
re42='(\\d+)'	# Integer Number 17
re43='.*?'	# Non-greedy match on filler
re44='(\\d+)'	# Integer Number 18
re45='.*?'	# Non-greedy match on filler
re46='(\\d+)'	# Integer Number 19
re47='.*?'	# Non-greedy match on filler
re48='(\\d+)'	# Integer Number 20
re49='.*?'	# Non-greedy match on filler
re50='(\\d+)'	# Integer Number 21
re51='.*?'	# Non-greedy match on filler
re52='(\\d+)'	# Integer Number 22
re53='.*?'	# Non-greedy match on filler
re54='(\\d+)'	# Integer Number 23
re55='.*?'	# Non-greedy match on filler
re56='(\\d+)'	# Integer Number 24
re57='.*?'	# Non-greedy match on filler
re58='(\\d+)'	# Integer Number 25
re59='.*?'	# Non-greedy match on filler
re60='(\\d+)'	# Integer Number 26
re61='.*?'	# Non-greedy match on filler
re62='(\\d+)'	# Integer Number 27
re63='.*?'	# Non-greedy match on filler
re64='(\\d+)'	# Integer Number 28
re65='.*?'	# Non-greedy match on filler
re66='(\\d+)'	# Integer Number 29
re67='.*?'	# Non-greedy match on filler
re68='(\\d+)'	# Integer Number 30
re69='.*?'	# Non-greedy match on filler
re70='(\\d+)'	# Integer Number 31
re71='.*?'	# Non-greedy match on filler
re72='(\\d+)'	# Integer Number 32

rg = re.compile(re1+re2+re3+re4+re5+re6+re7+re8+re9+re10+re11+re12+re13+re14+re15+re16+re17+re18+re19+re20+re21+re22+re23+re24+re25+re26+re27+re28+re29+re30+re31+re32+re33+re34+re35+re36+re37+re38+re39+re40+re41+re42+re43+re44+re45+re46+re47+re48+re49+re50+re51+re52+re53+re54+re55+re56+re57+re58+re59+re60+re61+re62+re63+re64+re65+re66+re67+re68+re69+re70+re71+re72,re.IGNORECASE|re.DOTALL)
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
    int17=m.group(17)
    int18=m.group(18)
    int19=m.group(19)
    int20=m.group(20)
    int21=m.group(21)
    int22=m.group(22)
    int23=m.group(23)
    int24=m.group(24)
    int25=m.group(25)
    int26=m.group(26)
    int27=m.group(27)
    int28=m.group(28)
    int29=m.group(29)
    int30=m.group(30)
    int31=m.group(31)
    int32=m.group(32)
    print "("+int1+")"+"("+int2+")"+"("+int3+")"+"("+int4+")"+"("+int5+")"+"("+int6+")"+"("+int7+")"+"("+int8+")"+"("+int9+")"+"("+int10+")"+"("+int11+")"+"("+int12+")"+"("+int13+")"+"("+int14+")"+"("+int15+")"+"("+int16+")"+"("+int17+")"+"("+int18+")"+"("+int19+")"+"("+int20+")"+"("+int21+")"+"("+int22+")"+"("+int23+")"+"("+int24+")"+"("+int25+")"+"("+int26+")"+"("+int27+")"+"("+int28+")"+"("+int29+")"+"("+int30+")"+"("+int31+")"+"("+int32+")"+"\n"

#-----
# Paste the code into a new python file. Then in Unix:'
# $ python x.py 
#-----
