import random

import requests

from config.config import Config


class parsefunc():
    def concat(self, last_str):
        """
        做字符串拼接，拼接url或者Referer
        :param value: 待拼接的字符串
        :return:   拼接完成的字符串
        """
        configManage = Config.get_instance()
        new_url = configManage.url + last_str
        return new_url


    def upload_file(self, file_path):
        """
        输入相对路径，从本地获取二进制文件对象
        :param file_path:  输入路径
        :return:  返回一个文件对象
        """
        file = open(file_path, 'rb')
        files = {'file': (file_path, file)}
        return files

    def request(self, params_dict):
        """
        统一请求处理，区别于测试案例里面的请求
        :param params_dict: 发请求需要的参数字典
        :return: 返回响应
        """
        method = params_dict.pop('method', 'get').lower()
        url = params_dict.pop('url', None)
        headers = params_dict.pop('headers', {})

        # 准备请求参数
        params = params_dict if method == 'get' else None
        data = params_dict if method == 'post' and 'json' not in params_dict and 'files' not in params_dict else None
        json_data = params_dict if method == 'post' and 'json' in params_dict else None
        files = params_dict.pop('files', None)

        # 发送请求
        response = requests.session().request(
            method=method,
            url=url,
            headers=headers,
            params=params,
            data=data,
            json=json_data,
            files=files
        )
        return response

    def get_random_element_from_list(self, element_list):
        """
        随机获取列表中的一个元素
        :param element_list:
        :return:
        """
        random_element = random.choice(element_list)
        return random_element


    def get_book_id_from_current_user(self):
        """
        从当前用户的书籍下选择一本书的book_id
        :return: book_id
        """
        config_obj = Config.get_instance()
        params_dict = {'headers': {}}

        params_dict['headers']['token'] = config_obj.token
        params_dict['headers']['Referer'] = config_obj.url + '/index/allScan'
        params_dict['url'] = config_obj.url + '/book/getList'
        params_dict['method'] = 'get'
        params_dict['page'] = 1
        params_dict['page_size'] = 10

        response = self.request(params_dict)
        json_response = response.json();
        books = json_response.get('data').get('books')
        book = self.get_random_element_from_list(books)


        return book.get('book_id')



parsefunc_obj = parsefunc()