'''
文件名：test_开头/_test结尾
类名：Test开头
方法名：test_开头
'''
import logging
import time

import allure
import pytest
import yaml


# 读取文件
def get_add_datas():
    # with方法可以自动关闭文件
    with open("./datas/calc.yml") as f:
        datas = yaml.safe_load(f)
    add_int_datas = datas.get("add").get("int").get("datas")
    add_int_ids = datas.get("add").get("int").get("ids")
    return (add_int_datas, add_int_ids)


def get_div_datas():
    with open("./datas/calc.yml") as f:
        datas = yaml.safe_load(f)
    div_int_datas = datas.get("div").get("int").get("datas")
    div_int_ids = datas.get("div").get("int").get("ids")
    return (div_int_datas, div_int_ids)

# 读取文件第二种方式
# def get_datas1():
#     with open("./datas/calc.yml") as f:
#         # datas = yaml.safe_load(f)
#         add_int_datas = yaml.safe_load(f).get("add").get("int").get("datas")
#         # 第一次load走到后面，指针已经移到末尾，所以第二次load没有内容,第二次load消耗资源
#         add_int_ids = yaml.safe_load(f).get("add").get("int").get("ids")
#     return (add_int_datas, add_int_ids)


# def test_getdatas():
#     print(get_add_datas())


# param相当于数据的载体，会将数据一条一条载入测试数据中
# param放在函数中，函数本身不会return param中的数据，函数需要增加request的参数，然后返回request.param返回数据
@pytest.fixture(params=get_add_datas()[0], ids=get_add_datas()[1])
def get_datas_byfixture(request):
    print(f"request.param == {request.param}")
    # 固定写法
    return request.param

@pytest.fixture(params=get_div_datas()[0], ids=get_div_datas()[1])
def get_div_byfixture(request):
    return request.param


# def test_getdata_byfixture(get_datas_byfixture):
#     print(get_datas_byfixture)
@allure.story("排序3")
@pytest.mark.run(order = 3)
def test_ordering1():
    print("test1")
    with open('datas/1154371630079513.png', mode='rb') as f:
        file = f.read()
        allure.attach(file, 'random', attachment_type=allure.attachment_type.PNG)


@allure.story("排序1")
@pytest.mark.run(order = 1)
def test_ordering2():
    print("test2")


@allure.story("排序2")
@pytest.mark.run(order = 2)
def test_ordering3():
    print("test3")


# 日志文件按时间命名
@pytest.fixture(scope="session", autouse=True)
def manage_logs(request):
    """Set log file name same as test name"""
    now = time.strftime("%Y-%m-%d %H-%M-%S")
    #
    rootdir = request.config.rootdir
    print(rootdir)
    log_name = rootdir + "/output/log/Date_" + now + ".logs"
    print(log_name)

    request.config.pluginmanager.get_plugin("logging-plugin") \
        .set_log_path(log_name)


@allure.feature("计算器")
class TestCalc:

    # 第一种参数化方式
    @pytest.mark.parametrize('a, b, expect', get_add_datas()[0], ids=get_add_datas()[1])
    def test_add(self, a, b, expect, get_calc):
        logging.info(f"相加功能：参数 {a, b, expect}")
        assert get_calc.add(a, b) == expect

    # 第二种参数化方式
    @allure.story("相加功能")
    def test_add1(self, get_calc, get_datas_byfixture):
        logging.info(f"相加功能：参数 {str(get_datas_byfixture)}")
        assert get_calc.add(get_datas_byfixture[0], get_datas_byfixture[1]) == get_datas_byfixture[2]

    @allure.story("相除功能")
    def test_div(self, get_calc, get_div_byfixture):
        logging.info(f"相除功能：参数 {str(get_div_byfixture)}")
        assert get_calc.div(get_div_byfixture[0], get_div_byfixture[1]) == get_div_byfixture[2]

