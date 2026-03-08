# ==========================================
# Python itertools 全指南：高效迭代的艺术
# ==========================================

import itertools
import operator

# --- 一、 模块概述 ---
# itertools 是 Python 处理迭代器的核心工具集。
# 核心优势：
# 1. 内存效率：采用“惰性求值”（Lazy Evaluation），按需产生数据，不占用大内存。
# 2. 速度快：底层由 C 语言实现。
# 3. 简洁：将复杂的嵌套循环简化为单行函数。

# --- 二、 排列组合迭代器 (Combinatoric Iterators) ---

print("--- 2.1 product: 笛卡尔积 ---")
# 相当于嵌套的 for 循环
for each in itertools.product('ABC', 'XY'):
    print(f"  组合: {each}")
# repeat 参数表示序列自身的重复次数
#

print("\n--- 2.2 permutations: 排列 (顺序有关) ---")
# 从 'abc' 中取 2 个进行排列，会产生 (a,b) 和 (b,a)
for each in itertools.permutations('abc', 2):
    print(f"  排列: {each}")

print("\n--- 2.3 combinations: 组合 (顺序无关) ---")
# 从 'abc' 中取 2 个进行组合，(a,b) 和 (b,a) 被视为同一个，只保留一个
for each in itertools.combinations('abc', 2):
    print(f"  组合: {each}")
#

print("\n--- 2.4 combinations_with_replacement: 可重复组合 ---")
# 允许同一个元素被多次选择
for each in itertools.combinations_with_replacement('abc', 2):
    print(f"  组合: {each}") # 会出现 ('a', 'a') 等

# --- 三、 无限迭代器 (Infinite Iterators) ---
# 注意：使用无限迭代器时必须有 break 条件，否则程序会卡死！

print("\n--- 3.1 count: 无限递增计数 ---")
for i in itertools.count(start=10, step=2):
    print(f"  计数: {i}", end=" ")
    if i >= 16: break
print()

print("\n--- 3.2 cycle: 无限循环序列 ---")
count_a = 0
for i in itertools.cycle('ABC'):
    print(f"  循环: {i}", end=" ")
    if i == 'A': count_a += 1
    if count_a >= 3: break # 遇到第三个 A 停止
print()

print("\n--- 3.3 repeat: 重复对象 ---")
# 重复 'Hello' 3 次
print(f"  重复结果: {list(itertools.repeat('Hello', 3))}")

# --- 四、 有限迭代器 (Finite Iterators) ---

print("\n--- 4.1 accumulate: 累积汇总 ---")
# 默认是累加
nums = [1, 2, 3, 4, 5]
print(f"  累加: {list(itertools.accumulate(nums))}")
# 配合 operator 模块计算累乘
print(f"  累乘: {list(itertools.accumulate(nums, operator.mul))}")
# 计算累计最大值
data = [3, 4, 6, 2, 1, 9, 0, 7]
print(f"  累计最大值: {list(itertools.accumulate(data, max))}")
#

print("\n--- 4.2 chain: 链状连接 ---")
# 将多个可迭代对象连成一个
print(f"  连接结果: {list(itertools.chain('ABC', [1, 2], ('!',)))}")

print("\n--- 4.3 chain.from_iterable: 扁平化(降维) ---")
# 处理嵌套的可迭代对象
nested = [['1'], ['2', '3'], ('4', '5')]
print(f"  降维结果: {list(itertools.chain.from_iterable(nested))}")

print("\n--- 4.4 compress: 过滤选择 ---")
# 根据 selectors (1/0 或 True/False) 筛选 data
print(f"  筛选结果: {list(itertools.compress('ABCD', [1, 0, 1, 1]))}") # 'A', 'C', 'D'

print("\n--- 4.5 dropwhile & 4.10 takewhile ---")
# dropwhile: 只要条件满足就丢弃，直到遇到第一个不满足的，返回后面所有
print(f"  dropwhile (<5): {list(itertools.dropwhile(lambda x: x < 5, [2, 1, 6, 8, 2, 1]))}") # [6, 8, 2, 1]
# takewhile: 只要条件满足就保留，直到遇到第一个不满足的，停止
print(f"  takewhile (<5): {list(itertools.takewhile(lambda x: x < 5, [1, 3, 5, 6]))}") # [1, 3]

print("\n--- 4.6 filterfalse: 过滤假值 ---")
# 保留函数结果为 False 的元素
print(f"  保留偶数: {list(itertools.filterfalse(lambda x: x % 2, range(6)))}") # [0, 2, 4]

print("\n--- 4.7 groupby: 分组 ---")
# 注意：使用 groupby 前通常需要对数据排序，否则只能分组连续的重复项
#
for key, group in itertools.groupby('AABBBAAC'):
    print(f"  组名: {key}, 内容: {list(group)}")

print("\n--- 4.8 islice: 迭代器切片 ---")
# 语法: islice(iterable, start, stop, step)
print(f"  切片结果: {list(itertools.islice('ABCDEFG', 1, 4))}") # 'B', 'C', 'D'

print("\n--- 4.9 starmap: 星号映射 ---")
# 针对已经打包成元组的数据执行函数
print(f"  乘法结果: {list(itertools.starmap(lambda x, y: x * y, [(2, 5), (3, 2)]))}")

print("\n--- 4.11 tee: 分裂迭代器 ---")
# 将一个迭代器复制成 n 个独立的副本
it1, it2 = itertools.tee([1, 2, 3], 2)
print(f"  副本1: {list(it1)}, 副本2: {list(it2)}")

print("\n--- 4.12 zip_longest: 补齐拉链 ---")
# 传统的 zip 谁短听谁的，zip_longest 谁长听谁的，不足处用 fillvalue 补齐
res = itertools.zip_longest('XYZ', '12', fillvalue='*')
print(f"  补齐结果: {list(res)}") # [('X', '1'), ('Y', '2'), ('Z', '*')]

# --- 五、 实战案例：计算文本相似度 (Jaccard) ---
def jaccard_similarity(s1, s2):
    set1, set2 = set(s1), set(s2)
    # 利用 & (intersection) 和 | (union)
    return len(set1 & set2) / len(set1 | set2)

print(f"\nJaccard 相似度示例: {jaccard_similarity('罗志祥', '罗志祥出轨')}")