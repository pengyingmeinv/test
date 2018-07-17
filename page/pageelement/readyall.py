#!/usr/bin/python  
# -*-coding:utf-8-*-
import os
import yaml

yamlpath = os.path.dirname(os.path.realpath(__file__))


def parseyaml():
    pageElements = {}
    # def readyallyaml():
    for fpath, dirname, fnames in os.walk(yamlpath):
        for name in fnames:

            yamlfile_path = os.path.join(fpath, name)
            # print(yamlfile_path)

            # 排除一些非。yaml文件
            if ".yaml" in str(yamlfile_path):
                # print(yamlfile_path)
                with open(yamlfile_path, "r", encoding="utf-8") as f:
                    # print(yamlfile_path)
                    page = yaml.load(f)
                    pageElements.update(page)


    return pageElements
a=parseyaml()["Mypage"]['locators']
# print(a)
for i in a:
    print(i["name"])
# print(parseyaml()["Mypage"]["locators"])
def get_local(pageame, name):
    for i in parseyaml()[pageame]['locators']:
        if i["name"] == name:

            print(i)


#     return a
# get_local("Mypage", "我的")
# # if __name__ == '__main__':
# #
# #     # print(parseyaml()["Mypage"])
# #     get_local("Mapage")