#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/2/23 20:10
# @Author  : liuliuliu
# @Site    :
# @File    : test_demo.py
# @Software: PyCharm
import gzip

import requests
from jsonpath import jsonpath
from hamcrest import *


class TestDemo:
    def test_get(self):
        r = requests.get("https://httpbin.testing-studio.com/get")
        print(r.status_code)
        print(r.text)
        print(r.json())
        assert r.status_code == 200

    # get query请求
    def test_query(self):
        payload = {
            "level": 1,
            "name": "seveniruby"
        }
        r = requests.get("https://httpbin.testing-studio.com/get", params=payload)
        print(r.text)
        assert r.status_code == 200

    # post form请求
    def test_post_form(self):
        payload = {
            "level": 1,
            "name": "seveniruby"
        }
        r = requests.post("https://httpbin.testing-studio.com/post", data=payload)
        print(r.text)
        assert r.status_code == 200

    # post json请求
    def test_post_json(self):
        payload = {
            "level": 1,
            "name": "seveniruby"
        }
        r = requests.post("https://httpbin.testing-studio.com/post", json=payload)
        print(r.text)
        assert r.status_code == 200
        assert r.json()['json']['level'] == 1

    def test_header(self):
        r = requests.get("https://httpbin.testing-studio.com/get", headers={"h": "header demo"})
        print(r.status_code)
        print(r.text)
        print(r.json())
        assert r.status_code == 200
        assert r.json()["headers"]["H"] == "header demo"

    def test_hgwz_json(self):
        r = requests.get("https://ceshiren.com/categories.json")
        print(r.text)
        assert r.status_code == 200
        assert r.json()['category_list']['categories'][0]['name'] == '提问区'
        assert jsonpath(r.json(), '$..name')[0] == '提问区'
        assert_that(r.json()['category_list']['categories'][0]['name'], equal_to('提问区'))
