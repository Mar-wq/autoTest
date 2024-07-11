import os

import yaml





class Config:
    _instance = None

    def __new__(cls, config_file=None):
        if cls._instance is None:
            cls._instance = super(Config, cls).__new__(cls)
            if config_file:
                cls._instance.init_config(config_file)
        return cls._instance

    def init_config(self, config_path):
        with open(config_path, 'r', encoding='utf-8') as file:
            config_data = yaml.safe_load(file)
        suffix = config_data['choose']['activeEnvironment']
        role = config_data['choose']['activeUserRole']
        new_config_path = self.generate_new_config_path(config_path, suffix)

        actual_config_data =  self.read_config(new_config_path)
        self.url = actual_config_data['url']
        self.token = actual_config_data[role]['token']
        self.roles = actual_config_data[role]['roles']
        self.roles = set(self.roles)
        print()

    def read_config(self, config_path):
        with open(config_path, 'r', encoding='utf-8') as file:
            return yaml.safe_load(file)

    def generate_new_config_path(self, config_path, suffix):
        # 分割路径和文件名
        base_path, filename = os.path.split(config_path)
        # 分割文件名和扩展名
        base_name, ext = os.path.splitext(filename)
        # 拼接新的文件名
        new_filename = f"{base_name}_{suffix}{ext}"
        # 返回新的完整路径
        return os.path.join(base_path, new_filename).replace("\\", "/")


    def get_token(self):
        if self.role == 'admin':
            return self.config_data[self.env]['admin']['token']
        elif self.role == 'regular_user':
            return self.config_data[self.env]['regular_user']['ordinary_token']
        else:
            return None

    @staticmethod
    def get_instance():
        if Config._instance is None:
            raise Exception("Config instance is not initialized, call get_instance with a config file first.")
        return Config._instance
