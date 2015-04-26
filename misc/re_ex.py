#!/usr/bin/env python
# coding: utf-8
#copyRight by heibanke

import re
text = 'c++ python2 python3 perl ruby lua java javascript php4 php5 c'

#match,search,findall,split,sub
re.match(r'c++',text)
re.match(r'c\+\+',text)
re.match(r'java',text)
re.search(r'java',text)

print re.findall(r'python',text)
print re.split(r' perl ',text)
print re.sub(r'ruby','fortran',text)

# +   1-inf
# *   0-inf
# ?   0-1, 
# []  or
# {}  repeat
# [^] not
print re.findall(r'p+',text)
print re.findall(r'p[a-zA-Z]+',text)  #{1,}
print re.findall(r'c[a-zA-Z]*',text)  #{,inf}
print re.findall(r'c[^a-zA-Z]*',text)  #{,inf}
print re.findall(r'c[a-zA-Z]?',text)  #{,1}

# |   or
print re.findall(r'[pj][a-zA-Z]+',text)  #{,inf}
print re.findall(r'p[^0-9]+|j[a-zA-Z]+',text)   
print re.findall(r'p[^0-9 ]+|j[a-zA-Z]+',text) 

# ^   start
# $   end
# .   except \n
print re.findall(r'^c..',text)
print re.findall(r'c+',text)
print re.findall(r'c\++',text)
print re.findall(r'c$',text)

# \w  [a-zA-Z0-9_], \W
# \d  [0-9], \D
# \s  [ \t\n\r\f\v], \S
print re.findall(r'p\w+',text)
print re.findall(r'p\w+\d',text)
print re.findall(r'p\w+[0-9]',text)
print re.findall(r'p\w{5,9}',text)

# \b  word boundary
# \B  not \b
# \A  input start, ^
# \Z  input end, $
print re.findall(r'\bp[^0-9]',text)
print re.findall(r'p[^0-9]\b',text)

# *?  0~inf non-greedy
# +?  1~inf non-greedy
print re.findall(r'p[^0-9]*',text)
print re.findall(r'p[^0-9]*?',text)
print re.findall(r'p[^0-9]+\b',text)
print re.findall(r'p[^0-9]+?\b',text)

# ()  group
# (?P<name>pattern)
a=re.search(r'(p[a-zA-Z]+)([0-9])','python2')
print a.group(1), a.group(2)

a=re.search(r'(?P<name>p[a-zA-Z]+)(?P<version>[0-9])','python2')
print a.group('name'), a.group('version')
print a.groupdict()

pattern = re.compile(r'(?P<name>p[a-zA-Z]+)(?P<version>[0-9])')
results = pattern.search('python2')
print results.groupdict()
results = pattern.search('python3')
print results.groupdict()
results = pattern.search('php4')
print results.groupdict()

#########################################
for t in text.split(' '):
    results = pattern.search(t)
    if results:
      print results.groupdict()