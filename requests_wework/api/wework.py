#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/3/23 21:24
# @Author  : liuliuliu
# @Site    : 
# @File    : wework.py
# @Software: PyCharm
from requests_wework.api.base_api import BaseApi


class WeWork(BaseApi):
    def get_token(self, secrete):
        # 获取token
        corpid = "wwe53fe128a56983da"
        corpsecret = secrete
        data = {
            "method": "get",
            "url": " https://qyapi.weixin.qq.com/cgi-bin/gettoken",
            "params": {
                "corpid": corpid,
                "corpsecret": corpsecret
            }
        }
        return self.send(**data)["access_token"]
