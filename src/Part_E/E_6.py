#coding=gbk
'''
Created on 2014��7��16��

@author: jiangxin
���Ȳ���һ����������У�Ȼ����ˣ�����filter()����)�����е�ż��
'''
from random import randint

def is_odd(n):
    return n%2

numbers = []
for each in range(100):
    numbers.append(randint(1,99))
print filter(is_odd, numbers)
