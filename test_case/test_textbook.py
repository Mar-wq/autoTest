import sys,os

import allure
import pytest
import pdb


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
from common.basefunc import *


################################数据驱动准备########################################
file_path = './data/home_page_of_cloud_textbooks.xlsx'


################################开始测试########################################
@allure.feature("首页页面")
class Test_Case:
    @pytest.mark.parametrize('test_data',basefunc.transact(file_path))
    def test_case2(self,test_data, load_config):
        config = load_config
        basefunc.run_case(test_data)