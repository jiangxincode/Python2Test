#coding=gbk
'''
Created on 2014��7��16��

@author: jiangxin
'''
def printf(str_output,*tuple_output):
    print str_output % (tuple_output)

"""This is a test"""
printf("This is a test! %d,%d",9,10)