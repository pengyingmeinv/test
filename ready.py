#!/usr/bin/python  
# -*-coding:utf-8-*-
import yaml
import os

dirpath = os.path.realpath(os.path.dirname(__file__))
compath = os.path.join(dirpath, "common", "peizhi.yaml")
print(compath)

f = open(compath, "r", encoding="utf-8")
a = f.read()

f.close()

print(a)

# 把yaml转换成字典格式

d = yaml.load(a)
print(d)
