import json

import requests

from common.loggerController import log

from config.config import Config


class requestion_assertion:
    def __init__(self):
        self.session = requests.Session()

    def set_token(self, params):

        config_data = Config.get_instance()
        token =  config_data.token
        # 检查并更新 headers
        if 'headers' in params:
            params['headers']['token'] =token
        else:
            params['headers'] = {'token': token}


    def send_request(self, params_dict):
        self.set_token(params_dict)
        method = params_dict.pop('method', 'get').lower()
        url = params_dict.pop('url', None)
        role = params_dict.pop('role', None)
        headers = params_dict.pop('headers', {})


        # 准备请求参数
        params = params_dict if method == 'get' else None
        data = params_dict if method == 'post' and 'json' not in params_dict and 'files' not in params_dict else None
        json_data = params_dict if method == 'post' and 'json' in params_dict else None
        files = params_dict.pop('files', None)

        # 发送请求
        response = self.session.request(
            method=method,
            url=url,
            headers=headers,
            params=params,
            data=data,
            json=json_data,
            files=files
        )
        return {"response": response, "role": role}


    def unified_assert(self, check_params):
        """
        :param check_params: 断言需要的参数字典
        :return: response
        """

        unified_response = check_params.pop('unified_response')
        response = unified_response['response']
        need_role = unified_response['role']  #访问当前接口需要的身份权限
        roles = Config.get_instance().roles   #当前账户的身份权限集合
        status_code = response.status_code
        expected_status_code = check_params.pop('expected_status_code')



        if need_role not in roles:
            log.info("当前用户不满足接口调用的权限")
            assert status_code != 200
            return

        log.info("预期状态码为：{},实际状态码为：{}".format(expected_status_code, status_code))
        assert status_code == expected_status_code, "Expected status code {}, but got {}".format(
            expected_status_code, status_code)



        if not check_params:
            return

        # 获取 JSON 响应内容
        response_content = response.json()

        # 遍历 params_dict 中的键和值，检查是否与 response 中的对应项匹配
        for key, expected_value in check_params.items():
            actual_value = response_content.get(key)
            log.info("预期值为：{},实际值为：{}".format(expected_value, actual_value))
            assert actual_value == expected_value, "预期值：{}, 实际得到的值：{}".format(
                expected_value, actual_value)

        return response




requestion_assertion =  requestion_assertion()