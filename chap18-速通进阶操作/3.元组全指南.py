# ==========================================
# Python 元组（Tuple）全指南：不可变的艺术
# ==========================================

# 核心特性：
# 1. 不可变性：一旦创建，不能增、删、改。
# 2. 哈希值固定：因此元组可以作为字典的 Key，也可以作为集合（Set）的项。
# 3. 性能：比列表稍快，占用内存更小。

# --- 一、 元组的创建 ---

# 01. 使用圆括号创建空元组
t_empty = ()

# 02. 单元素元组（关键：必须加逗号！）
t_single_error = (1)  # 这只是一个括号括起来的整数，type 是 int
t_single_right = (1,)  # 这才是元组，type 是 tuple
a = 'a',  # 也可以省略括号，只要有逗号就行

# 03. 多元素元组
t_multi = (1, 2, 3)
t_no_brackets = 1, 2, 3,  # 结尾多一个逗号也没事，Python 很包容

# 04. 使用内置函数 tuple() 转换
t_from_list = tuple([1, 2, 3])
t_from_str = tuple("abc")  # 结果: ('a', 'b', 'c')

# --- 二、 元组的方法 ---
# 元组只有 2 个公共方法：count 和 index

print("--- 1. index() 获取元素下标 ---")
# 语法: index(value, start, stop)
t = ('s', 'a', 'a', 'r', 5)
print(f"'r' 的下标: {t.index('r')}")  # 结果: 3
print(f"5 的下标: {t.index(5)}")  # 结果: 4

# 寻找第二个 'a' 的位置 (从索引 2 开始找)
t_repeat = (1, 2, 3, 1, 2)
print(f"第二个 '1' 的索引: {t_repeat.index(1, 2)}")  # 结果: 3

print("\n--- 2. count() 统计出现次数 ---")
t_chars = ('a', 'a', 'b', 'c')
print(f"'a' 出现的次数: {t_chars.count('a')}")  # 结果: 2

# --- 三、 元组的其他常见操作 ---

s1 = (1, 2, 3)
s2 = ('a', 'b', 'c')

# 1) 拼接生成新元组 (并不会改变原元组)
s3 = s1 + s2
# 或者使用底层方法 s1.__add__(s2)

# 2) 成员检测
is_in = 2 in s1  # True
is_not_in = 'a' in s1  # False

# 3) 获取元素 (索引取值)
item = s1[0]  # 1
# 或者 s2.__getitem__(0)

# 4) 获取长度
length = len(s1)  # 3

# 5) 重复拼接
s_triple = s1 * 3  # (1, 2, 3, 1, 2, 3, 1, 2, 3)

# 6) 删除整个元组
# 元组内的元素不能删，但可以用 del 删掉整个变量
t_to_del = ("a", "b", "c")
del t_to_del
# print(t_to_del) # 这行会报错，因为 t_to_del 已经不存在了

# 7) 最大最小值
t_nums = (10, 22, 0, 15, 40)
print(f"最大值: {max(t_nums)}, 最小值: {min(t_nums)}")

# --- 四、 具名元组 (NamedTuple) ---
# 它是带“字段名”的记录，比普通元组更具可读性，像是一个不可变的轻量级类。

from collections import namedtuple

# 1. 定义一个 City 类
# 参数1: 类名; 参数2: 字段名（空格分隔）
City = namedtuple("City", "name country population coordinates")

# 2. 实例化
tokyo = City("Tokyo", 'JP', '36.93', ('35.68', '139.69'))
print(f"\n具名元组打印: {tokyo}")
print(f"通过属性访问名字: {tokyo.name}")  # 结果: Tokyo

# 3. 专有属性
print(f"所有字段名: {City._fields}")

# 4. _make 方法：从序列生成新实例
LatLong = namedtuple('LatLong', 'lat long')
xiamen_data = ('Xiamen', 'China', '40.54', LatLong(24.26, 118.03))
xiamen = City._make(xiamen_data)
print(f"使用 _make 生成: {xiamen}")

# 5. _asdict 方法：转为 OrderedDict (字典格式)
xiamen_dict = xiamen._asdict()
print(f"转为字典: {xiamen_dict['name']}")

# --- 五、 元组 vs 列表：什么时候用元组？ ---

# 1. 结构 (Structure) vs 顺序 (Order)
# 元组表示的是“结构”。例如一个坐标 (x, y) 这是一个整体结构。
point = (1, 2)

# 列表表示的是“顺序”。例如棋盘上所有坐标的序列。
points = [(1, 2), (1, 3), (4, 5)]

# 2. 安全性
# 当你不希望数据被意外修改时（如数据库配置、常量），用元组。

# 3. 作为字典的 Key
location_map = {
    (35.68, 139.69): "Tokyo",
    (24.26, 118.03): "Xiamen"
}  # 正常运行

# list_key_map = {[1, 2]: "Point"} # 这会报错：TypeError: unhashable type: 'list'
