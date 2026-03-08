# --- 概 述 ---
# 列表推导式利用其他列表创建新的列表，工作方式类似于 for 循环。
# 它可以快速生成或筛选满足特定需求的列表。

print("--- 1. 单循环 ---")
# 生成 0 到 9 的数字列表
list1 = [i for i in range(10)]
print(f"基础生成: {list1}")
print("-" * 30)

print("--- 2. 单循环 + 条件 ---")
# 找出 0-20 中所有能被 3 整除的数
# 语法: [表达式 for 变量 in 序列 if 条件]
list2 = [i for i in range(20) if i % 3 == 0]
print(f"0-20中能被3整除的数: {list2}")
print("-" * 30)

print("--- 3. 多循环 - 2次 ---")
# 'ABC' 和 'EFG' 所有可能的两两组合（笛卡尔积）
list3 = [i + j for i in 'ABC' for j in 'EFG']
print(f"2次循环组合: {list3}")
print("-" * 30)

print("--- 4. 多循环 - 3次 ---")
# 'ABC'、'EFG'、'HIJ' 所有可能的三三组合
list4 = [i + j + u for i in 'ABC' for j in 'EFG' for u in 'HIJ']
print(f"3次循环组合(部分展示): {list4[:5]} ... 总数: {len(list4)}")
print("-" * 30)

# 数据准备：用于后续复杂的匹配案例
girls = ['alice', 'bernice', 'clarice']
boys = ['chris', 'arnold', 'bob', 'bernod']

print("--- 5. 多循环 + 单条件 ---")
# 找出首字母相同的男孩和女孩组合
list5 = [i + '<->' + j for i in girls for j in boys if i[0] == j[0]]
print(f"首字母相同组合: {list5}")
print("-" * 30)

print("--- 6. 多循环 + 多条件 ---")
# 第一个字母且第二个字母均相同
list6 = [i + '<->' + j for i in girls for j in boys if (i[0] == j[0] and i[1] == j[1])]
print(f"前两个字母均相同: {list6}")
print("-" * 30)

print("--- 7. 元组循环 (生成器表达式) ---")
# 使用 () 而非 [] 时，不会直接生成列表，而是生成一个“生成器对象”（迭代器）
# 这在处理大数据量时非常节省内存，因为它只在循环时才产生数据
tuples_gen = (i + '<->' + j for i in girls for j in boys if i[0] == j[0])
print(f"直接打印生成器对象: {tuples_gen}")

print("通过循环迭代生成器内容:")
for t in tuples_gen:
    print(f"  {t}")
print("-" * 30)

print("--- 8. 效率优化案例 ---")
# 在上面的男孩-女孩例子中，嵌套循环的效率为 O(N*M)。
# 如果列表很大，程序会进行大量无意义的检测。
# 优化思路：先建立索引（字典），将匹配复杂度降至接近 O(N)。

# 步骤1：建立女孩名字首字母的索引字典
letter_girls = {}
for girl in girls:
    letter_girls.setdefault(girl[0], []).append(girl)

# 步骤2：利用推导式快速匹配。仅在 boys 名字的首字母存在于字典中时才进行拼接
# 这样避免了对不匹配字母的无效循环
efficient_match = [i + '<->' + j for j in boys if j[0] in letter_girls for i in letter_girls[j[0]]]
print(f"优化后的匹配结果: {efficient_match}")
