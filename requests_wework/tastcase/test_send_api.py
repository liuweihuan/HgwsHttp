#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/3/21 22:25
# @Author  : liuliuliu
# @Site    : 
# @File    : test_send_api.py
# @Software: PyCharm


def test_send_api():
    content=Content("./work.yaml")
    expression=api_action(content)


