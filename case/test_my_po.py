#!/usr/bin/python  
# -*-coding:utf-8-*-
'''
前提：打开app
1.点我的
2.点邀请好友
3.获取返回结果：获取文字，微信/朋友圈/QQ
4.期望结果：文字，微信/朋友圈/QQ
5.断言 ： 实际结果 == 期望结果
'''

import unittest
from appium import webdriver
import time
from common.base import BaseApp
from page.Mypage import MyPg
desired_caps = {
    "platformName": "Android",
    "platformVersion": "4.4.4",
    "deviceName": "79AEALF2PBLB",
    "appPackage": "com.yipiao",
    "appActivity": "com.zt.main.entrance.ZTLaunchActivity",
    "noReset": True,
    "unicodeKeyboard": True,
    "resetKeyboard": True
}

#driver = webdriver.Remote("http://localhonst:4723/wb/hu", desired_caps)


class Testsharm(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_caps)
        time.sleep(8)
        #cls.app = BaseApp(cls.driver)
        cls.my = MyPg(cls.driver)
    #点我的
    def setUp(self):
        self.my.click_my()
        time.sleep(2)

    def test_yaoqing(self):
        #点邀请
        self.my.click_yaoqing()
        time.sleep(2)

        #获取结果
        r = self.my.get_result()

        #判断实际结果与期望结果
        self.assertEqual(r, ['微信', '朋友圈', 'QQ', 'QQ空间', '短信'])
    def tearDown(self):
        self.driver.keyevent(4)
        time.sleep(3)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__ == '__main__':
    unittest.main