"""
描述: collections 模块全家族（9大子类）实战演示
涵盖内容: Counter, deque, namedtuple, OrderedDict, defaultdict, ChainMap, UserDict/List/String
"""

import re
from collections import (
    Counter, deque, namedtuple, OrderedDict,
    defaultdict, ChainMap, UserDict, UserList, UserString
)

# ==========================================
# 1. Counter (计数器)：统计学大师
# ==========================================
print("--- 1. Counter 演示 ---")
# 场景：统计一段文字中单词出现的频率
text = "apple orange apple banana orange apple"
cnt = Counter(text.split())

print(f"原始计数: {cnt}")
print(f"出现次数最多的前2名: {cnt.most_common(2)}")
print(f"总计元素个数: {sum(cnt.values())}")

# 数学运算：计数器合并
c1 = Counter(a=3, b=1)
c2 = Counter(a=1, b=2)
print(f"计数器相加 (c1 + c2): {c1 + c2}")
print(f"交集 (取最小计数): {c1 & c2}")
print("-" * 30)


# ==========================================
# 2. deque (双端队列)：极速滑块
# ==========================================
print("--- 2. deque 演示 ---")
# 场景：固定长度的日志缓冲区，只保留最新的 3 条记录
dq = deque(maxlen=3)
for i in range(5):
    dq.append(f"Log_Entry_{i}")
    print(f"当前缓冲区状态: {list(dq)}")

# 两端操作
dq.appendleft("Emergency_Log") # 从左侧插入
print(f"左侧插入后: {dq}")
dq.rotate(1) # 向右循环移动 1 步
print(f"向右旋转 1 步: {dq}")
print("-" * 30)


# ==========================================
# 3. namedtuple (具名元组)：带标签的记录
# ==========================================
print("--- 3. namedtuple 演示 ---")
# 场景：定义一个“鱼”的数据模型
Fish = namedtuple('Fish', ['name', 'species', 'tank'])
sammy = Fish(name="Sammy", species="Shark", tank=1)

print(f"通过名字访问: {sammy.name}, 通过索引访问: {sammy[1]}")
# 转换成字典
print(f"转化为字典: {sammy._asdict()}")
# 替换某个值（注意：元组本身不可变，_replace 会生成新对象）
new_sammy = sammy._replace(tank=2)
print(f"换缸后的鱼: {new_sammy}")
print("-" * 30)


# ==========================================
# 4. OrderedDict (有序字典)：强迫症的福音
# ==========================================
print("--- 4. OrderedDict 演示 ---")
# 虽然 Python 3.7+ 的 dict 默认有序，但 OrderedDict 提供额外的移动方法
od = OrderedDict.fromkeys('ABCDE')
od.move_to_end('B') # 将 'B' 移到末尾
print(f"将 B 移到末尾: {list(od.keys())}")
od.move_to_end('B', last=False) # 将 'B' 移到开头
print(f"将 B 移到开头: {list(od.keys())}")
print("-" * 30)


# ==========================================
# 5. defaultdict (默认值字典)：拒绝报错
# ==========================================
print("--- 5. defaultdict 演示 ---")
# 场景：按颜色对水果分组
pairs = [('red', 'apple'), ('yellow', 'banana'), ('red', 'cherry')]
# 默认工厂函数是 list，当键不存在时会自动创建一个空列表
d_dict = defaultdict(list)
for color, fruit in pairs:
    d_dict[color].append(fruit)

print(f"分组结果: {dict(d_dict)}")
# 用于计数
d_int = defaultdict(int)
d_int['missing_key'] += 1
print(f"不存在的键自动初始化为0并自增: {d_int['missing_key']}")
print("-" * 30)


# ==========================================
# 6. ChainMap (映射链)：配置管理的王者
# ==========================================
print("--- 6. ChainMap 演示 ---")
# 场景：CLI 权限优先级（命令行参数 > 环境变量 > 默认配置）
defaults = {'theme': 'Default', 'language': 'zh'}
env = {'theme': 'Dark'}
cli_args = {} # 假设用户没传

# 搜索顺序由左及右
config = ChainMap(cli_args, env, defaults)
print(f"当前生效主题: {config['theme']}") # 输出 'Dark'
print(f"语言配置: {config['language']}") # 输出 'zh'
print("-" * 30)


# ==========================================
# 7-9. UserDict, UserList, UserString (定制化包装)
# ==========================================
print("--- User系列演示 ---")
# 场景：创建一个禁止存储偶数的列表
class OddList(UserList):
    def append(self, item):
        if item % 2 == 0:
            print(f"拒绝添加偶数: {item}")
            return
        super().append(item)

my_odd_list = OddList([1, 3])
my_odd_list.append(5)
my_odd_list.append(4) # 触发拦截
print(f"OddList 最终内容: {my_odd_list.data}")

# UserDict 示例：访问底层存储属性 .data
class MyDict(UserDict):
    pass
md = MyDict(a=1)
print(f"UserDict 的原始存储: {md.data}")