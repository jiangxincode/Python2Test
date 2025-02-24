'''
在函数体内部定义的变量就称之为局部变量。
探讨局部变量访问范围
① 局部作用域中可以访问局部变量
② 在全局作用域中，无法访问函数内部的局部变量
注意：局部变量只在局部作用域中有效，当函数执行完毕后，其内部的局部变量也会随之消失
'''
def func():
    # 1. 定义一个局部变量
    num2 = 100
    # 在局部作用域中尝试访问局部变量
    # print(num2)

# 2. 调用函数，注意：函数只有在调用时，其内部代码才会被执行
func()
print(num2)