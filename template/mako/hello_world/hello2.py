#!/usr/bin/env python

from mako.template import Template

mytemplate = Template("hello world!")
print (mytemplate.render())