#!/usr/bin/env python
# coding: utf-8
#copyRight by heibanke

text = 'c++ python2 python3 perl ruby lua java javascript php4 php5 c'

#index, slice
text[0]
text[0:3]
text[-1]
text[4:-1]
text[0:10:2]

# split, join
a = text.split(' ')
b = ', '.join(a)

# + , *
text[0:4]+text[-2:len(text)]
text[0:4]*5

#other func
print text.upper()
text.find('py')
text.replace('python','fortran')
print "%s like %s" %('we','python')

#strip
text = 'c++, python2, python3, perl, ruby, java, javascript, php4, php5, c'
a=text.split(',')
a[1].strip()

a = r'C:\newpython'

s = "用Python做些事"

s = u"用Python做些事"
