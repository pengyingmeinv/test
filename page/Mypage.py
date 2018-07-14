#!/usr/bin/python  
# -*-coding:utf-8-*-
from common.base import BaseApp
import yaml
import os
#from page.pageelement import read
from page.pageelement import read
from page.pageelement.read import get_locals




class MyPg(BaseApp):
    # locl11 = {"by": "text", "value": "我的", "name": "我的"}
    # locl2 = {"by": "text", "value": "邀请好友", "name": "邀请好友"}
    # locl3 = {"by": "id", "value": "com.yipiao:id/socialize_text_view"}
    # locl4 = {"by": "text", "value": "取消分享", "name": "取消分享"}

    # if locl1 == locl11:
    #     print('yes')
    # else:
    #     print('no')
    # get_locals(read.a, "我的")
    locl1 = get_locals(read.a, "我的")
    locl2 = get_locals(read.a, "邀请好友")
    locl3 = get_locals(read.a, "分享框")
    locl4 = get_locals(read.a, "取消分享")


    def click_my(self):
        self.click(self.locl1)

    def click_yaoqing(self):
        self.click(self.locl2)

    def get_result(self):
        all = self.finds(self.locl3)

        result = []
        for i in all:
            print(i.text)
            result.append(i.text)

        return result

    def click_quxiao(self):
        self.click(self.locl4)