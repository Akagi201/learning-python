# -*- coding: utf-8 -*-
#!/usr/bin/env python

from flask import Markup

#Markup(u'<strong>Hello &lt;blink&gt;hacker&lt;/blink&gt;!</strong>')
Markup('<strong>Hello %s!</strong>') % '<blink>hacker</blink>'

#Markup(u'&lt;blink&gt;hacker&lt;/blink&gt;')
Markup.escape('<blink>hacker</blink>')

#u'Marked up \xbb HTML'
Markup('<em>Marked up</em> &raquo; HTML').striptags()
