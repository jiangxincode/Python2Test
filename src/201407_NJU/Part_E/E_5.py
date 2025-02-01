#coding=gbk
'''
Created on 2014��7��16��

@author: jiangxin
�� reduce()���к���ʽ����Լ��ݹ顣
(a)��һ����д���� x,y���������ǳ˻�����Ϊ mult(x,y)�ļ�С�ɺ�����
(b)������ a�д����� mult()�����Լ� reduce������׳ˡ�
(c)���������� mult()��ʹ�� ���� lamda���ʽ�����
(d)���������һ���ݹ����������ҵ� N!
'''
def mult(x,y):
    return x*y

def factorial1(n):
    return reduce(mult,range(1,n+1))

def factorial2(n):
    return reduce((lambda x,y:x*y),range(1,n+1))

def factorial3(n):
    if n==1:
        return 1
    else:
        return n*factorial3(n-1)


"""This is a test"""
print mult(12, 13)
print factorial1(10)
print factorial2(10)
print factorial3(10)

