#!/usr/bin/python
#-*- encoding: utf-8 -*-

# list与tuple

# list：Python内置的一种数据类型是列表，是一种有序的集合，可以随时添加和删除其中的元素

# 不限制存储的类型
fruit = ['苹果', '香蕉', '橘子', 1, 2, 4]
print(fruit)

# 获取元素个数
print(len(fruit))

'''
索引访问：
1、正序访问：[0, 1, 2, ... len - 1]
2、倒叙访问：[-len, ..., -2, -1]
'''
print(fruit[0])
print(fruit[-6])

# list是可变序列

# 插入元素
fruit.insert(1, '奇异果')
print(fruit)

# 在末尾追加元素
fruit.append('荔枝')
print(fruit)

# 删除元素

# 删除末尾元素直接使用pop
fruit.pop()
print(fruit)

# 删除指定位置元素
fruit.pop(4)
print(fruit)
fruit.pop(-1)
print(fruit)

# 替换元素
fruit[0] = 'Apple'
print(fruit)

#删除元素
del fruit[-1]
print(fruit)

# list内可以嵌套list
'''
假设有如下矩阵
1 0 0
0 1 0
0 0 1
'''
matrix = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
print(matrix)
print(matrix[1][2])
print(matrix[-1][2])

# list切片
print(fruit)

# 从头部切片 [)
print(fruit[:3])
print(fruit[1:3])

# 从尾部切片 [)
print(fruit[-4:])
print(fruit[-4:-2])

# 空list
list1 = []
print(list1)
print(len(list1))
