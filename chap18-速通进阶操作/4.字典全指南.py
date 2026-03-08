# ==========================================
# Python 字典（Dictionary）全指南：键值对的艺术
# ==========================================

# --- 一、 字典概述 ---

# 01. 字典格式
# 字典是可变的，键(Key)必须是不可变类型（字符串、数字、元组），值(Value)可以是任意类型。
# 格式: {key1: value1, key2: value2}
d_example = {"name": "fucov", "age": 18}

# 02. 多种创建方式 (结果均相等) dict(x1=??,) || {x1:??}
# zzz=dict(1=2,2=3,4=5) #报错
a = dict(one=1, two=2, three=3)

b = {'one': 1, 'two': 2, 'three': 3}
c = dict(zip(['one', 'two', 'three'], [1, 2, 3]))
d = dict([('two', 2), ('one', 1), ('three', 3)])
e = dict({'three': 3, 'one': 1, 'two': 2})
f = dict({'one': 1, 'three': 3}, two=2)
print(f"字典创建一致性检查: {a == b == c == d == e == f}")  # True

# 03. 键的特性
# 1) 唯一性：如果键重复，最后的赋值会覆盖前面的。
# 2) 不可变：列表不能做键，元组可以。
# bad_dict = {[1, 2]: "list_key"} # 报错：TypeError: unhashable type: 'list'

# --- 二、 字典的11个核心方法 ---

# 01. fromkeys(): 快速生成初始字典
seq = ('Google', 'Baidu', 'Taobao')
new_dict = dict.fromkeys(seq, 10)  # 所有键初始值都设为 10
# new_dict = dict(zip(seq, [10] * len(seq))) #
print(f"01. fromkeys 结果: {new_dict}")

# 02. clear(): 清空字典
dic_to_clear = {"python3": 123}
dic_to_clear.clear()
print(f"02. clear 后的字典: {dic_to_clear}")  # {}

# 03. copy(): 浅拷贝
# 注意：浅拷贝不拷贝内部的可变子对象。
import copy

d0 = {1: "a", 2: "b", 4: [1, 2, 3]}
d1 = d0  # 引用：两者指向同一个对象
d2 = d0.copy()  # 浅拷贝：父对象独立，但子对象（列表）仍引用同一个
d3 = copy.deepcopy(d0)  # 深拷贝：完全独立

d0[4].append(4)  # 修改原字典中的列表
print(f"03. 原字典 d0: {d0}")
print(f"    浅拷贝 d2 (受子对象影响): {d2}")
print(f"    深拷贝 d3 (完全不受影响): {d3}")

# 04. get(): 安全获取值（键不存在时不报错）
dic = {"uiui": "ioio"}
print(f"04. get 存在的键: {dic.get('uiui')}")
print(f"    get 不存在的键 (返回默认值): {dic.get('non_exist', '查无此人')}")

# 05. setdefault(): 获取值，若不存在则先插入再返回
dict_set = {'name': 'Alice', 'age': 23}
val = dict_set.setdefault('high', 178)  # 插入 'high': 178 并返回 178
print(f"05. setdefault 后的字典: {dict_set}")

# 06. keys(): 返回所有键
print(f"06. 所有键: {list(dict_set.keys())}")

# 07. values(): 返回所有值
print(f"07. 所有值: {list(dict_set.values())}")

# 08. items(): 返回(键, 值)元组列表
# 常用于循环遍历
print("08. items 遍历演示:")
for key, value in dict_set.items():
    print(f"    Key: {key}, Value: {value}")

# 09. pop(): 删除指定键并返回值
age = dict_set.pop('age')
print(f"09. pop 出的年龄: {age}, 剩余: {dict_set}")

# 10. popitem(): 删除并返回最后一对 (Python 3.7+)
# 在老版本中是随机删除
last_pair = dict_set.popitem()
print(f"10. popitem 结果: {last_pair}")

# 11. update(): 更新/合并字典
dict_main = {'name': 'Alice', 'age': 20}
dict_main.update({'age': 80, 'address': 'Hangzhou'})  # 更新 age，新增 address
print(f"11. update 结果: {dict_main}")

# --- 三、 其他常用操作 ---

my_dict = {'one': 1, 'two': 2, 'three': 3}

# 01. 长度
print(f"字典项数: {len(my_dict)}")

# 02. 取值与修改 (d[key])
my_dict['one'] = 10  # 修改
my_dict['four'] = 4  # 新增

# 03. 删除项 (del)
del my_dict['one']

# 04. 成员判断 (in / not in) - 针对的是键！
print(f"'two' 是否在字典中: {'two' in my_dict}")

# 05. 反向迭代 (Python 3.8+)
print(f"逆序键列表: {list(reversed(my_dict))}")

# 06. 字典合并操作符 (Python 3.9+)
d1 = {"a": 1, "b": 2}
d2 = {"b": 3, "c": 4}
d3 = d1 | d2  # 合并，若有冲突，d2 优先
print(f"3.9+ 合并符 (|): {d3}")  # {'a': 1, 'b': 3, 'c': 4}

d1 |= d2  # 就地更新
