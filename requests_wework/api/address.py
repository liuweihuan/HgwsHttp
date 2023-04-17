#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/3/20 21:15
# @Author  : liuliuliu
# @Site    : 
# @File    : address.py
# @Software: PyCharm
import requests

from requests_wework.api.base_api import BaseApi
from requests_wework.api.wework import WeWork


class Address(BaseApi):
    def __init__(self):
        secrete = "iGqIYp9IGev6UfN3RiSNDwNEj3VL0CjeLMnW33Bk9kM"
        self.token = WeWork().get_token(secrete)

    def get(self, test_token):
        # 查询成员列表
        data1 = {
            "cursor": "1",
            "limit": 10000
        }
        data = {
            "method": "post",
            "url": " https://qyapi.weixin.qq.com/cgi-bin/user/list_id",
            "params": {
                self.token
            }
        }
        return self.send().json()

    def create(self, userid, name, mobile):
        # 创建成员
        data = {
            "method": "post",
            "url": "https://qyapi.weixin.qq.com/cgi-bin/user/create",
            "params": {
                "access_token": self.token
            },
            "json": {
                "userid": userid,
                "name": name,
                "mobile": mobile,
                "department": [1]
            }

        }
        return self.send(**data)

    def update(self, userid, name):
        # 更新成员
        data = {
            "method": "post",
            "url": "https://qyapi.weixin.qq.com/cgi-bin/user/update",
            "params": {
                "access_token": self.token
            },
            "json": {
                "userid": userid,
                "name": name,
            }

        }
        return self.send(**data)

    def delete(self, userid):
        # 删除成员
        data = {
            "method": "get",
            "url": "https://qyapi.weixin.qq.com/cgi-bin/user/delete",
            "params": {
                "access_token": self.token
            },
            "json": {
                "userid": userid,
            }

        }
        return self.send(**data)
