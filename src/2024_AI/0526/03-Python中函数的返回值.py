'''
当函数执行完毕后，可能给调用它的程序一个返回值。
编程建议：一般情况下，当函数执行完毕后，不建议使用print()直接打印结果，往往建议是通过一个return关键词返回最终结果给函数调用处
def 函数名称(函数的参数):
    函数体代码
    return 结果

函数名称(传递的参数值) : 当函数调用完毕后，可能给它的调用处返回一个结果（返回值）
'''
def greet(name):
    return '您好，' + name

# 调用greet函数
result = greet('老张')
print(result)  # 打印输出函数的返回结果