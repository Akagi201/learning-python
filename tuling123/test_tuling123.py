#!/usr/bin/env python
# -*- coding: utf-8 -*-

# curl "http://www.tuling123.com/openapi/api?key=申请到的key&info=聊天内容"

import os
import json
import urllib2

class Chat(object):
    key = "7747a8b00a2dac69e7ab1cb5290586bc"
    apiurl = "http://www.tuling123.com/openapi/api?"

    def __init__(self):
        os.system("clear")
        print("尽情调教我吧!")
        print("-" * 60)

    def get(self):
        print("> "),
        info = raw_input()
        if info == 'q' or info == 'exit' or info == "quit":
            print("- Goodbye")
            return
        self.send(info)

    def send(self, info):
        url = self.apiurl + 'key=' + self.key + '&' + 'info=' + info
        re = urllib2.urlopen(url).read()
        re_dict = json.loads(re)
        text = re_dict['text']
        print '- ', text
        self.get()

if __name__ == "__main__":
    chat = Chat()
    chat.get()
