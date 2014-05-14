#!/usr/bin/python
# URL that generated this code:
# http://txt2re.com/index-python.php3?s=10:%20%20%2026%20%20127%20%20127%20%20127%20%20127%20%20%20127%20%20127&10&1&2&3&4&5&6

import re

txt='10:   26  127  127  127  127   127  127'

re1='.*?'	# Non-greedy match on filler
re2='\\d+'	# Uninteresting: int
re3='.*?'	# Non-greedy match on filler
re4='(\\d+)'	# Integer Number 1
re5='.*?'	# Non-greedy match on filler
re6='(\\d+)'	# Integer Number 2
re7='.*?'	# Non-greedy match on filler
re8='(\\d+)'	# Integer Number 3
re9='.*?'	# Non-greedy match on filler
re10='(\\d+)'	# Integer Number 4
re11='.*?'	# Non-greedy match on filler
re12='(\\d+)'	# Integer Number 5
re13='.*?'	# Non-greedy match on filler
re14='(\\d+)'	# Integer Number 6
re15='.*?'	# Non-greedy match on filler
re16='(\\d+)'	# Integer Number 7

rg = re.compile(re1+re2+re3+re4+re5+re6+re7+re8+re9+re10+re11+re12+re13+re14+re15+re16,re.IGNORECASE|re.DOTALL)
m = rg.search(txt)
if m:
    int1=m.group(1)
    int2=m.group(2)
    int3=m.group(3)
    int4=m.group(4)
    int5=m.group(5)
    int6=m.group(6)
    int7=m.group(7)
    print "("+int1+")"+"("+int2+")"+"("+int3+")"+"("+int4+")"+"("+int5+")"+"("+int6+")"+"("+int7+")"+"\n"

#-----
# Paste the code into a new python file. Then in Unix:'
# $ python x.py 
#-----
