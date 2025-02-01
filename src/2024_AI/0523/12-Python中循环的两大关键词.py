'''
在循环中，有两个用于退出循环的关键词：continue 和 break
continue：中止本次循环，继而进入下一次循环 => 循环10次，在第3次遇到了continue，则第三次循环跳过，继而进入第4次循环
break：终止整个循环结构，循环10次，在第3次循环，遇到break了，则整个循环强制终止
最近减肥，晚上只吃苹果，每天只吃5个苹果 => 循环5次
情况一：吃完第3个苹果，准备吃第4个苹果，发现吃饱了，以后的苹果不吃了 => 最终答案：break
情况二：吃到第3个苹果，发现有个虫子，中止本次，继而进入下一次循环，吃第4个苹果 => 最终答案：continue
'''
# 1. 循环5次
# for i in range(1, 6):
#     # 2. 如果吃完了第3个，准备吃第4个，吃饱了
#     if i == 4:
#         print('吃饱了，后面的苹果不吃了！')
#         break
#
#     print(f'正在吃第{i}苹果！')

# 1. 循环5次
for i in range(1, 6):
    # 2. 吃到第3个苹果，不好，有大虫，这个苹果不吃了
    if i == 3:
        print('不好，有大虫，这个苹果不吃了')
        print('继续吃下面的苹果')
        continue
    print(f'正在吃第{i}个苹果！')

