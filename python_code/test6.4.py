dicts = {'list': '列表', 'str': '字符串', 'tuple': '元组', 'dict': '字典', 'int': '整型' }
for key, value in dicts.items():
    print(f"{key}: {value}")

dicts['split'] = '切片'
dicts['if'] =  '条件'
dicts['class'] = '类'
dicts['object'] = '对象'
dicts['boolean'] = '布尔'

for key, value in dicts.items():
    print(f"{key}: {value}")