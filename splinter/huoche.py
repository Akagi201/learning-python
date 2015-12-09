# -*- coding: utf-8 -*-
"""
@author: Akagi201
"""

from splinter.browser import Browser
from time import sleep
import traceback

###容错做的不好，考虑的情况也不够多，大家见谅

# 用户名，密码
username = u"改成用户名"
passwd = u"改成用户名"
# cookies值得自己去找, 下面两个分别是上海, 营口东
starts = u"%u4E0A%u6D77%2CSHH"
ends = u"%u8425%u53E3%u4E1C%2CYGT"
# 时间格式2016-01-31
dtime = u"2016-02-01"
# 车次，选择第几趟，0则从上之下依次点击
order = 0
###乘客名
pa = u"改成乘客姓名"

"""网址"""
ticket_url = "https://kyfw.12306.cn/otn/leftTicket/init"
login_url = "https://kyfw.12306.cn/otn/login/init"
initmy_url = "https://kyfw.12306.cn/otn/index/initMy12306"


def login():
    b.find_by_text(u"登录").click()
    sleep(3)
    b.fill("loginUserDTO.user_name", username)
    sleep(1)
    b.fill("userDTO.password", passwd)
    sleep(1)
    print u"等待验证码，自行输入..."
    while True:
        if b.url != initmy_url:
            sleep(1)
        else:
            break

def huoche():
    global b
    b = Browser(driver_name="chrome")
    b.visit(ticket_url)

    while b.is_text_present(u"登录"):
        sleep(1)
        login()
        if b.url == initmy_url:
            break

    try:
        print u"购票页面..."
        # 跳回购票页面
        b.visit(ticket_url)

        # 加载查询信息
        b.cookies.add({"_jc_save_fromStation": starts})
        b.cookies.add({"_jc_save_toStation": ends})
        b.cookies.add({"_jc_save_fromDate": dtime})
        b.reload()

        sleep(2)

        count = 0
        # 循环点击预订
        if order != 0:
            while b.url == ticket_url:
                b.find_by_text(u"查询").click()
                count +=1
                print u"循环点击查询... 第 %s 次" % count
                sleep(1)
                try:
                    b.find_by_text(u"预订")[order - 1].click()
                except:
                    print u"还没开始预订"
                    continue
        else:
            while b.url == ticket_url:
                b.find_by_text(u"查询").click()
                count += 1
                print u"循环点击查询... 第 %s 次" % count
                sleep(1)
                try:
                    for i in b.find_by_text(u"预订"):
                        i.click()
                except:
                    print u"还没开始预订"
                    continue
        sleep(1)
        b.find_by_text(pa)[1].click()
        print  u"能做的都做了.....不再对浏览器进行任何操作"
    except Exception as e:
        print(traceback.print_exc())

if __name__ == "__main__":
    huoche()
