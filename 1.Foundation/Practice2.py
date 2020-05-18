#!/usr/bin/python
# -*- encoding: utf-8 -*-

# 字符串和编码

# python3中字符串是以Unicode编码的，即python3支持多种语言

# 将字符转成整数表示
print(ord('A'))
print(ord('中'))

# 数字转换成字符
print(chr(66))
print(chr(20013))

print(hex(20013))

# 十六进制字符串
print("\u4e2d\u6587")

s = 'xxx'
c = b'ac' # bytes类型
z = b'\xe4\xb8\xad\xe6\x96\x87'
print(type(s))
print(type(c))
print(type(z))

# encode() 方法获取指定编码的字符串
print(s.encode("ASCII"))
print("中国".encode("utf-8"))

# print('中文'.encode('ascii')) 错误，中文超过了ASCII范围

# decode() 方法将bytes转化为string

print(b'ABC'.decode('ascii'))
print(b'ABC'.decode('utf-8'))
print(b'\xe4\xb8\xad\xe5\x9b\xbd'.decode("UTF-8"))

# print(b'\xe4\xb8\xad\xff'.decode('utf-8')) 错误无法解析s
print(b'\xe4\xb8\xad\xff'.decode('utf-8', errors='ignore'))

# len() 获取字符串长度 或者获取bytes的字节数
print(len(b'\xe4\xb8\xad\xe5\x9b\xbd'.decode("UTF-8")))
print(len(b'\xe4\xb8\xad\xe5\x9b\xbd'))
print(len('''中国'''))
# 1个中文字符经过UTF-8编码后通常会占用3个字节，而1个英文字符只占用1个字节

# 格式化输出
# 占位符        替换内容
# %d            整数
# %f            浮点型
# %s            字符串
# %x            十六进制整数

#格式化输出
# 整数的输出
# %o    oct 八进制
# %d    dec 十进制
# %x    hex 十六进制

print("%o" % 20)
print("%d" % 20)
print("%x" % 20)


# 浮点数输出
# %f    保留小数点后面六位有效数字  %.3f，保留3位小数
print("%f" % 1.1111)
print("%f" % 1.1111116)

# %2    保留小数点后面六位有效数字，指数形式输出    %.3e 保留3位小数位，使用科学计数法
print("%e" % 1.111)
print("%e" % 111111.111)
print("%.3e" % 111.6666)

# %g    在保证六位有效数字的前提下，使用小数方式，否则使用科学计数法 %.3g，保留3位有效数字，使用小数或科学计数法
print("%g" % 1111.1111)
print("%g" % 1111116)
print("%.7g" % 1111.1177)
print("%.2g" % 1111.1177)

'''
字符串输出
%s
%10s——右对齐，占位符10位
%-10s——左对齐，占位符10位
%.2s——截取2位字符串
%10.2s——10位占位符，截取两位字符串
'''
print('%s' % 'hello world')  # 字符串输出
print('%20s' % 'hello world')  # 右对齐，取20位，不够则补位
print('%-20s' % 'hello world')  # 左对齐，取20位，不够则补位
print('%.2s' % 'hello world')  # 取2位
print('%10.2s' % 'hello world')  # 右对齐，取2位
print('%-10.2s' % 'hello world')  # 左对齐，取2位

'''
format用法
 相对基本格式化输出采用‘%’的方法，format()功能更强大，该函数把字符串当成一个模板，通过传入的参数进行格式化，并且使用大括号‘{}’作为特殊字符代替‘%’
位置匹配
　　（1）不带编号，即“{}”
　　（2）带数字编号，可调换顺序，即“{1}”、“{2}”
　　（3）带关键字，即“{a}”、“{tom}”
'''
print('{} {}'.format('hello','world'))  # 不带字段
print('{0} {1}'.format('hello','world'))  # 带数字编号
print('{0} {1} {0}'.format('hello','world'))  # 打乱顺序
print('{1} {1} {0}'.format('hello','world'))
print('{a} {tom} {a}'.format(tom='hello',a='world'))  # 带关键字