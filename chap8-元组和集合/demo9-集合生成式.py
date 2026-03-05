

# 列表生成式
lst = [i*i for i in range(10)]
print(lst)

# 集合生成式
s = {i*i for i in range(10)}
print(s)

"""总结
数据结构      是否可变    是否重复    是否有序    定义符号
列表（list)    可变      可重复       有序        []
元组（tuple）   不可变    可重复      有序      (）
字典(dict)     可变     key(不可，   无序     {key:value}
                       value(可
集合（set)     可变      不可重复    无序        {}
"""