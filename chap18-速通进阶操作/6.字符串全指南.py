# ==========================================
# Python 字符串（String）全指南：45个方法详解
# ==========================================

# --- 一、 大小写转换 ---

s = "i Love pYthoN"
print(f"01. capitalize (首字母大写): {s.capitalize()}")  # "I love python"
print(f"02. title (标题格式): {s.title()}")  # "I Love Python"
print(f"03. swapcase (大小写互换): {s.swapcase()}")  # "I lOVE PythON"
print(f"04. lower (全部小写): {s.lower()}")  # "i love python"
print(f"05. upper (全部大写): {s.upper()}")  # "I LOVE PYTHON"

# 06. casefold (更彻底的小写，支持德语等特殊字符转换)
print(f"06. casefold: {'Groß'.casefold()}")  # "gross"

# --- 二、 字符串填充与对齐 ---

# 07. center (居中)
print(f"07. center: {'shuai'.center(10, '*')}")  # "**shuai***"

# 08. ljust (左对齐)
print(f"08. ljust: {'Jack'.ljust(10, '#')}")  # "Jack######"

# 09. rjust (右对齐)
print(f"09. rjust: {'Joe'.rjust(10, '*')}")  # "*******Joe"

# 10. zfill (0填充，常用于ID格式化)
print(f"10. zfill: {'56'.zfill(5)}")  # "00056"

# --- 三、 字符串编码 (数据传输核心) ---

# 11. encode (编码: 字符串 -> 字节)
encoded = "我爱祖国".encode('utf-8')
print(f"11. encode 结果: {encoded}")

# 12. decode (解码: 字节 -> 字符串)
# 注意：decode 是 bytes 对象的方法，不是 str 的方法
print(f"12. decode 结果: {encoded.decode('utf-8')}")

# --- 四、 字符串查找 ---

s_search = "I love python"

# 13. find: 找索引，找不到返回 -1
print(f"13. find 'o': {s_search.find('o')}")

# 14. rfind: 从右边开始找
print(f"14. rfind 'o': {s_search.rfind('o')}")

# 15. index: 找索引，找不到会报错 ValueError
print(f"15. index 'p': {s_search.index('p')}")

# 16. rindex: 从右边找索引，找不到报错
# print(s_search.rindex('k')) # 会报错

# --- 五、 字符串格式化 ---

# 17. format (最强大的格式化)
print("17. format: {}购买了{}".format('马云', '淘宝'))

# 18. format_map (基于字典格式化)
info = {'name': '张三', 'score': 748}
print("18. format_map: {name}考了{score}分".format_map(info))

# --- 六、 逻辑判断 (返回 True/False) ---

s_check = "python3"

print(f"19. endswith ('n'): {s_check.endswith('n')}")
print(f"20. startswith ('p'): {s_check.startswith('p')}")
print(f"21. isalnum (字母或数字): {s_check.isalnum()}")
print(f"22. isalpha (纯字母): {s_check.isalpha()}")
print(f"24. isdigit (纯数字): {s_check.isdigit()}")
print(f"25. isidentifier (是否为合法变量名): {s_check.isidentifier()}")
print(f"26. islower: {s_check.islower()}")
print(f"27. isupper: {s_check.isupper()}")
print(f"29. isprintable (是否可见): {'\n'.isprintable()}")  # False
print(f"30. isspace (纯空格): {'  '.isspace()}")
print(f"31. istitle: {'Hello Python'.istitle()}")

# --- 七、 字符串修剪 (清理脏数据) ---

s_dirty = " \n word:我很帅 \t "
print(f"32. strip (两端去空格): '{s_dirty.strip()}'")
print(f"33. lstrip (去左侧): '{s_dirty.lstrip()}'")
print(f"34. rstrip (去右侧): '{s_dirty.rstrip()}'")

# --- 八、 转换表与翻译 (批量替换/加密) ---

# 35. maketrans & 36. translate
# 将 'abc' 映射为 '123'
table = str.maketrans('abc', '123')
print(f"36. translate: {'apple'.translate(table)}")  # "1pple"

# --- 九、 分割与合并 ---

s_url = "https://www.google.com"

# 37. partition (三段式分割: 前, 分隔符, 后)
print(f"37. partition: {s_url.partition('://')}")

# 38. rpartition (从右边开始分)

# 39. split (根据分隔符切成列表)
print(f"39. split: {s_url.split('.')}")

# 40. rsplit (从右边开始切)

# 41. splitlines (按行分割)
print(f"41. splitlines: {'line1\nline2'.splitlines()}")

# 42. join (将序列连成字符串 - 性能之王)
parts = ['py', 'th', 'o', 'n']
print(f"42. join: {'_'.join(parts)}")  # "py_th_o_n"

# --- 十、 替换与字符统计 ---

# 43. replace (替换)
s_rep = "I love python"
print(f"43. replace: {s_rep.replace('python', 'java')}")

# 44. expandtabs (将 \t 转为空格)
print(f"44. expandtabs: {'a\tb'.expandtabs(4)}")

# 45. count (统计出现次数)
print(f"45. count 'o': {s_rep.count('o')}")
