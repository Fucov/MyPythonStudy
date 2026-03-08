# ==========================================
# Python 集合（Set）全指南：去重与逻辑运算
# ==========================================

# --- 一、 集合的定义与特性 ---

# 01. 特性：无序、唯一、元素必须不可变（可哈希）
# 自动去重演示
set1 = {1, 2, 4, 3, 3, 4, 4, 3, 3, 2, 2, 2, 2, 1}
print(f"自动去重结果: {set1}")  # {1, 2, 3, 4}

# 无序性演示
set_names = {"fucov", "真", "是", "帅"}
print(f"无序打印展示: {set_names}")  # 顺序随机,每次都不同

# 02. 集合的创建
s_empty = set()  # 创建空集合必须用 set()
d_empty = {}  # 注意：这创建的是空字典！

s_from_str = set('我爱我的祖国')  # 结果: {'国', '我', '爱', '的', '祖'}
s_from_list = set([1, 2, 3, 4]) # 等价：{1, 2, 3, 4}

# 集合推导式
s_comp = {x * 2 for x in 'abc'}  # {'aa', 'bb', 'cc'}

# --- 二、 集合的 17 个方法全解析 ---

# 数据准备：以“罗志祥女友集合”为例
s_girls1 = {'周扬青', '徐怀钰', 'Makiyo', 'Selina'}
s_girls2 = {'周扬青', '徐怀钰', '罗玉凤', '乔碧萝'}

# 01. add(): 添加单个元素
s_girls1.add('罗玉凤')
print(f"01. add 凤姐后: {s_girls1}")

# 02. clear(): 清空
s_temp = {1, 2, 3}
s_temp.clear()

# 03. copy(): 浅拷贝
s_copy = s_girls1.copy()

# 04. difference(): 返回差集 (s1 - s2)
# 即：在 s1 中但不在 s2 中的元素
print(f"04. 差集 (s1有但s2没有): {s_girls1.difference(s_girls2)}")

# 05. difference_update(): 原地修改为差集
s_up = {'a', 'b', 'c'}
s_up.difference_update({'a'})  # s_up 变为 {'b', 'c'}

# 06 & 13. discard() vs remove(): 移除元素
# remove 如果元素不存在会报错 KeyError，而 discard 不会
s_girls1.discard('女助理')  # 没这人，不报错
# s_girls1.remove('女助理') # 没这人，会报错！

# 07. intersection(): 返回交集 (s1 & s2)
# 即：两个集合中都有的元素
print(f"07. 交集 (共同好友): {s_girls1.intersection(s_girls2)}")

# 08. intersection_update(): 原地修改为交集
s_inter = {'a', 'b'}
s_inter.intersection_update({'b', 'c'})  # s_inter 变为 {'b'}

# 09. isdisjoint(): 判断是否完全没有交集
x = {"apple", "banana"}
y = {"google", "facebook"}
print(f"09. 是否无交集: {x.isdisjoint(y)}")  # True

# 10. issubset(): 判断是否为子集
print(f"10. {'a', 'b'} 是 {'a', 'b', 'c'} 的子集吗: {'a', 'b'}.issubset({'a', 'b', 'c'})")

# 11. issuperset(): 判断是否为超集
print(f"11. {'a', 'b', 'c'} 是 {'a', 'b'} 的超集吗: {'a', 'b', 'c'}.issuperset({'a', 'b'})")

# 12. pop(): 随机移除并返回一个元素
popped = s_girls1.pop()
print(f"12. pop 掉的随机女友: {popped}")

# 14. symmetric_difference(): 返回对称差集
# 即：两人不重叠的部分（s1 有或 s2 有，但不同时有的）
print(f"14. 对称差集 (各自独有): {s_girls1.symmetric_difference(s_girls2)}")

# 15. symmetric_difference_update(): 原地修改为对称差集

# 16. union(): 并集 (s1 | s2)
# 即：合并所有人，并去重
print(f"16. 并集 (所有人): {s_girls1.union(s_girls2)}")

# 17. update(): 更新集合（合并另一个集合或序列）
x = {"apple"}
x.update(["orange", "apple", "banana"])
print(f"17. update 后的集合: {x}")


# --- 三、 进阶实战：文本相似度 (Jaccard Similarity) ---

def jaccard_sim(str0, str1):
    """利用交集和并集计算两个字符串的相似度"""
    set1 = set(str0)
    set2 = set(str1)
    # 相似度 = 交集大小 / 并集大小
    return len(set1 & set2) / len(set1 | set2)


arg0 = '罗志祥道歉人设崩塌:多个品牌商中枪 代言微博遭删除'
arg1 = '凌晨五点的罗志祥:你知不知道为了出轨,我有多努力'
print(f"\n文本相似度计算结果: {jaccard_sim(arg0, arg1):.4f}")
