'''
if选择结构，基本语法：
if 要判断的条件:
    如果条件成立，则自动执行下方的缩进代码
    如果条件不成立，则自动跳过缩进代码的执行
注意事项：if语句只能管到其下方缩进代码，如果下方代码没有缩进，和if条件没有任何关系，程序会自动执行
例子：去网吧，要求必须出示身份证（主要判断是否成年），年龄大于等于18岁，可以上网，反之，则不可以上网
'''
# 1. 定义一个变量age
age = 19
# 2. 实现条件判断
if age >= 18:
    print('已成年，可以正常上网！')
# 3.if语句只能管到其下方缩进代码，如果下方代码没有缩进，和if条件没有任何关系，程序会自动执行
print('我是if外侧的Python代码！')
