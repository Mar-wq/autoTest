import pytest
from config.config import Config

@pytest.fixture(scope='session', autouse=True)
def load_config():
    # 初始化全局配置
    config = Config('./config/config.yaml')
    return config
