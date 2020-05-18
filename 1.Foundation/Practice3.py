#!/usr/bin/python
# -*- encoding: utf-8 -*-

# if条件语句
age = 16
if age >= 18:
    print("成年人")
else:
    print("未成年人")

# bool类型
print(type(1 > 2))
b = True
c = False

height = float(input("请输入你的体重（千克）："))
weight = float(input("请输入你的身高（米）："))
BMI = height / (weight * weight)
print(BMI)
if BMI <= 18.5:
    print("BMI：", BMI, "，偏轻")
elif BMI <= 23.9:
    print("BMI：", BMI, "，正常")
elif BMI <= 27.9:
    print("BMI：", BMI, "，超重")
elif BMI > 27.9:
    print("BMI：", BMI, "，肥胖")

