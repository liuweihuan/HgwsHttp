#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/3/20 21:43
# @Author  : liuliuliu
# @Site    : 
# @File    : test_address.py
# @Software: PyCharm
from requests_wework.api.address import Address


class TestAddress:
    def setup(self):
        self.address = Address()

    def test_create(self):
        print(self.address.create("zhangshang221", "wangwu1", "13814784741"))

    def test_update(self):
        print(self.address.update("ggg222", "wangwu111", ))

    def test_delete(self):
        print(self.address.delete("zhangshang222"))
