#!/usr/local/bin/python3
# @IDE: PyCharm
# @.py: run
# -*- coding : utf-8
# @Author:may
# @Time: 2025/4/15
import pytest
import os
import time

if __name__ == "__main__":
    pytest.main(["-s", "./", "--capture=sys"])  # --capture=sys会把报错的情况写进测试报告中
    # 如果每次都覆盖前一个报告，可以不添加时间戳
    os.system('allure generate ./report -o ./report/allure_html --clean')
    # 保留每个报告记录，报告加时间戳
    # os.system('allure generate ./report -o ./report/{}.html --clean'.format(time.strftime("%Y%m%d-%H%M%S")))
