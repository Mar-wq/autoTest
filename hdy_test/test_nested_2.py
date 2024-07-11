import regex as re

# 匹配嵌套的 $[content] 模式的正则表达式


class GatterCls:

    def concat(self, str1, str2):
        return str1 + str2

    def get_something(self, a, b):
        return a + b

    def func1(self, a):
        return a

    def func2(self, a):
        return str(a)


getattr_obj = GatterCls()


def process_list(input_list):
    processed_list = []
    for item in input_list:
        # 去掉单引号包围的字符串中的单引号
        if item.startswith("'") and item.endswith("'"):
            item = item[1:-1]
        # 尝试将字符串转换为整数或浮点数
        elif item.isdigit():  # 纯数字字符串转换为整数
            item = int(item)
        elif item.replace('.', '', 1).isdigit():  # 检查是否为浮点数格式的字符串
            item = float(item)
        processed_list.append(item)
    return processed_list


def split_params(params_str):
    params = []
    param = ""
    depth = 0

    for char in params_str:
        if char == ',' and depth == 0:
            params.append(param)
            param = ""
        else:
            param += char
            if char == '[':
                depth += 1
            elif char == ']':
                depth -= 1

    if param:
        params.append(param)

    return params

def parse_nested_func(nested_func_str):
    pattern = re.compile(r'\$\[(.*)\]')
    match = pattern.match(nested_func_str)
    match_group = match.group(1)

    # 提取最外层函数名及其参数
    outer_func_pattern = re.compile(r"(\w+)\((.*)\)")
    match = outer_func_pattern.match(match_group)



    func_name = match.group(1)
    params_str = match.group(2)

    params_str = params_str.replace(' ', '')
    params_list = split_params(params_str)
    processed1_params_list = process_list(params_list)          #

    processed2_params_list = []
    for param in processed1_params_list:
        if isinstance(param, str) and '$' in param:
            param = parse_nested_func(param)
        processed2_params_list.append(param)

    params_tuple =  tuple(processed2_params_list)
    func = getattr(getattr_obj, func_name)
    res = func(*params_tuple)

    return res


str1 = "$[concat('/book/getList', $[get_something($[func1('b')], $[func2(2)])])]"
res = parse_nested_func(str1)
print(res)