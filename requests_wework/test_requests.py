#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/3/1 22:52
# @Author  : liuliuliu
# @Site    : 
# @File    : test_requests.py
# @Software: PyCharm
import random
import re

import pytest
import requests
from filelock import FileLock


@pytest.fixture(scope="session")
def test_token():
    # 获取token
    while FileLock("session.lock"):
        corpid = "wwe53fe128a56983da"
        corpsecret = "iGqIYp9IGev6UfN3RiSNDwNEj3VL0CjeLMnW33Bk9kM"
        res = requests.get(f" https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid={corpid}&corpsecret={corpsecret}")
        print(res.json()["access_token"])
    return res.json()["access_token"]


def test_get(test_token):
    # 查询成员列表
    data = {
        "cursor": "1",
        "limit": 10000
    }
    userid = "xiaogao"
    res = requests.post(f"https://qyapi.weixin.qq.com/cgi-bin/user/list_id?access_token={test_token}")
    print(res.json())
    return res.json()


def test_create(userid, name, mobile, test_token):
    # 创建成员
    data = {
        "userid": userid,
        "name": name,
        "mobile": mobile,
        "department": [1],
    }
    res = requests.post(f"https://qyapi.weixin.qq.com/cgi-bin/user/create?access_token={test_token}", json=data)
    return res.json()


def test_update(userid, name, test_token):
    # 更新成员
    data = {
        "userid": userid,
        "name": name,
    }
    res = requests.post(f"https://qyapi.weixin.qq.com/cgi-bin/user/update?access_token={test_token}", json=data)
    return res.json()


def test_delete(userid, test_token):
    # 删除成员
    res = requests.post(f"https://qyapi.weixin.qq.com/cgi-bin/user/delete?access_token={test_token}&userid={userid}")
    return res.json()


def test_create_data():
    data = [("csuid" + str(x), "zhangshang", "138%08d" % x) for x in range(10)]
    print(data)
    return data


@pytest.mark.parametrize("userid,name,mobile", test_create_data())
def test_all(userid, name, mobile, test_token):
    try:
        assert "created" == test_create(userid, name, mobile, test_token)["errmsg"]
    except AssertionError as e:
        if "mobile existed" in e.__str__():
            # 如果手机号已经被使用,找出使用手机号的userid进行删除
            re_userid = re.findall(":(.*)", e.__str__())[0]
            if re_userid.endswith("'") or re_userid.endswith('"'):
                re_userid = re_userid[:-1]
            assert "deleted" == test_delete(re_userid, test_token)["errmsg"]
            assert "created" == test_create(userid, name, mobile, test_token)["errmsg"]

    assert "ok" == test_get(test_token)["errmsg"]
    assert "updated" == test_update(userid, "xxxa", test_token)["errmsg"]
    assert "deleted" == test_delete(userid, test_token)["errmsg"]
