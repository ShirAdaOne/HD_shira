from typing import List

import pytest
from Testcode.Calculator import Calculator


@pytest.fixture(autouse=True, scope="session")
def login():
    # setup 操作
    print("登陆操作")
    # yield 相当于 return 操作
    yield ['tom', '123456']
    # teardown 操作
    print("登出操作")

@pytest.fixture()
def start_app():
    print("启动")


'''
使用yield 模拟teardown
yield 前面的内容相当于setup
yield 相当于return
yield 后面的内容，相当于teardown操作
'''
@pytest.fixture
def get_calc():
    print("开始计算")
    calc = Calculator()
    yield calc  #相当于return
    print("计算结束")


def pytest_collection_modifyitems(
        session:"Session", config: "Config", items: List["Item"]
)-> None:
    for item in items:
        item.name = item.name.encode('utf-8').decode('unicode-escape')
        item._nodeid = item.nodeid.encode('utf-8').decode('unicode-escape')



