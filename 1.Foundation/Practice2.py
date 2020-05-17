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

# TODO
# 格式化输出
# 占位符        替换内容
# %d            整数
# %f            浮点型
# %s            字符串
# %x            十六进制整数