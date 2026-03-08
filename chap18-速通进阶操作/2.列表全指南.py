# ==========================================
# Python 列表（List）全指南：创建、方法与操作
# ==========================================

# Python有6个内置的基本数据类型：Number（数字）、String（字符串）、List（列表）、
# Tuple（元组）、Set（集合）、Dictionary（字典）。
# 列表是其中最常用且最重要的数据类型，其元素不需要具有相同的类型。

# --- 一、 列表的创建 ---

# 01. 直接创建：用中括号 [] 包裹元素，逗号分隔
list1 = ['physics', 'chemistry', 1997, 2000]
list2 = [1, 2, 3, 4, 5]
list3 = ["a", "b", "c", [1, [2]]]
list4 = ['red', 'green', 'blue', 'yellow', 'white', 'black']

# 02. 使用 list() 方法转换生成
list_b = list("abc")  # 结果: ['a', 'b', 'c']
list_c = list((4, 5, 6))  # 结果: [4, 5, 6]

# 03. 列表推导式（List Comprehension）生成
list_a = [1, 2, 3]
list_d = [i for i in list_a]  # 结果: [1, 2, 3]
list_e = [i * j for i in list_a for j in list_c]  # 结果: [4, 5, 6, 8, 10, 12, 12, 15, 18]
list_f = [i * j for i, j in zip(list_a, list_c)]  # 结果: [4, 10, 18]
list_g = [i for i in list_a if i % 2 == 0]  # 结果: [2]

# 04. 结合 range() 函数生成数字列表
list_h = list(range(3))  # 结果: [0, 1, 2]
list_i = list(range(3, 7))  # 结果: [3, 4, 5, 6]
list_j = list(range(3, 9, 2))  # 结果: [3, 5, 7]
# 找出100以内能被3整除的正整数
list_k = list(range(3, 100, 3))  # [3, 6, 9, ..., 99]

# --- 二、 列表的11个内置方法 ---
# 使用 dir(list()) 可以查看这些方法

print("--- 列表方法演示 ---")

# 01. append(): 在列表末尾添加一个元素（可以是任何对象）
ls = [1, 2, 3, 4, 5, 6]
ls.append(12)  # 添加数字
ls.append([1, "a"])  # 添加列表
ls.append({2: "a", 3: "hj"})  # 添加字典
ls.append((1, "k", 3))  # 添加元组
ls.append({"1", "2", "h"})  # 添加集合
ls.append("123abc")  # 添加字符串
print(f"01. append 后的列表: {ls}")

# 02. clear(): 删除列表中的所有元素
ls_clear = [1, 2, 3, "4", 5, "a"]
ls_clear.clear()
print(f"02. clear 后的列表: {ls_clear}")

# 03. copy(): 生成列表副本
ls = [1, 2, 3, [4, 5, 6]]
lt = ls.copy()  # lt 是 ls 的浅拷贝
lk = ls  # lk 只是 ls 的别名（引用同一个内存地址）
print(f"03. copy 后的 lt: {lt}, 地址比较: {id(ls) == id(lk)}")

# 04. count(): 统计某个元素出现的次数
ls_count = [1, 2, 3, 5, 4, 5, 5, 5, 5, "python"]
print(f"04. 元素 5 出现的次数: {ls_count.count(5)}")

# 05. extend(): 在末尾一次性追加另一个序列中的多个值
ls = [1, 2, "a", [4, 5, "a"]]
lt = [1, "abc", "b", [1, 2]]
ls.extend(lt)  # 注意：extend 和 append 不同，它会将 lt 拆解后再添加
print(f"05. extend 后的 ls: {ls}")

# 06. index(): 查找元素第一次出现的索引位置
ls = [1, 2, 3, "a", 3, 5, "a", 5, [1, 7, "b"]]
print(f"06. 'a' 第一次出现的索引: {ls.index('a')}")
print(f"    从下标4开始查 'a': {ls.index('a', 4)}")

# 07. insert(): 在指定位置插入对象
ls = [1, 2, 3]
ls.insert(1, "inserted")  # 在索引1位置插入
print(f"07. insert 后的列表: {ls}")

# 08. pop(): 移除并返回指定位置的元素（默认最后一个）
ls = [1, 2, "a", "y", [1, 2, 3], "b"]
popped_item = ls.pop(0)  # 移除下标为0的元素
print(f"08. pop 出的元素: {popped_item}, 剩余: {ls}")

# 09. remove(): 移除列表中某个值的第一个匹配项
ls = [1, 2, "a", 3, 1, 1, 55, "a,1"]
ls.remove(1)  # 仅移除第一个遇到的 1
print(f"09. remove(1) 后的列表: {ls}")

# 10. reverse(): 反转列表中的元素
ls = [1, 2, 3, 4, 5]
ls.reverse()
print(f"10. reverse 后的列表: {ls}")

# 11. sort(): 对原列表进行排序
ls = [1, 3, 7, 2, 4, 5, 6]
ls.sort()  # 默认升序
print(f"11. sort 排序后: {ls}")

# 高级排序技巧：保留原列表的排序
ls = [1, 3, 7, 2, 4, 5, 6]
y = sorted(ls)  # 方案一：使用内置函数 sorted()
z = ls[:]  # 方案二：先切片复制副本
z.sort()
print(f"    原列表保持不变: {ls}")
print(f"    排序后的副本 y: {y}")

# sort 的 key 参数演示
ls_strings = ['5aa', 'aaaba', 'xxvvv', 'a22112x', 'wodesddddssd']
ls_strings.sort(key=len)  # 按长度排序

print(f"    按长度排序: {ls_strings}")

students = [
    {"name": "Alice", "age": 20},
    {"name": "Bob", "age": 18},
    {"name": "Charlie", "age": 22}
]
students.sort(key=lambda x: x["age"])
print("按照年龄排序", students)

employees = [("Tom", 4000, 20), ("Jerry", 4000, 24), ("Bob", 5000, 28)]
sorted_employees = sorted(employees, key=lambda x: (-x[1], x[2]))

# --- 三、 列表脚本操作符 ---
# 列表支持 + (拼接) 和 * (重复)
print(f"拼接 (+): {[1, 2, 3] + [4, 5, 6]}")
print(f"重复 (*): {['Hi!'] * 3}")
print(f"成员资格 (in): {3 in [1, 2, 3]}")

# --- 四、 列表相关常用内置函数 ---
# 1. len(list): 列表元素个数
# 2. max(list): 返回最大值
# 3. min(list): 返回最小值
# 4. list(seq): 将序列转换为列表
nums = [10, 20, 30, 5]
print(f"列表长度: {len(nums)}, 最大值: {max(nums)}, 最小值: {min(nums)}")
