import regex as re

# 匹配嵌套的 $[content] 模式的正则表达式
pattern = re.compile(r'\$\[(.*)\]')

str1 = "$[concat('/book/getList', $[get_something($[fun1('b')], $[fun2(2)])])]"
match = pattern.match(str1)
if match:
    group = match.group(0)
    match_group = match.group(1)
    print("group:", group)
    print("match_group:", match_group)
else:
    print("No match found")
