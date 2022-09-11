# 这是一个示例 Python 脚本。

# 按 Shift+F10 执行或将其替换为您的代码。
# 按 双击 Shift 在所有地方搜索类、文件、工具窗口、操作和设置。


def print_hi(name):
    # 在下面的代码行中使用断点来调试脚本。
    print(f'Hi, {name}')  # 按 Ctrl+F8 切换断点。


# 按间距中的绿色按钮以运行脚本。
if __name__ == '__main__':
    print_hi('PyCharm')

# 访问 https://www.jetbrains.com/help/pycharm/ 获取 PyCharm 帮助
from numpy import *
# random.rand(4,4)
# randMat = mat(random.rand(4,4))
# print(randMat)
#
# randMat_I = randMat.I
# print(randMat_I)
#
# result = randMat*randMat_I
# print(result)
#
# myeye1 = eye(4)
# print(myeye1)
#
# myeye2 = result - myeye1
# print(myeye2)

import kNN
# group,labels = kNN.createDataSet()
# print(group,'\n',labels)
# 这条语句中导入的模块在后续的代码中没有使用，所以变成灰色
import numpy as np
# import * 和 from * import *的区别：
# import是导入一个包，你在使用其中的函数时必须xx.*才能行
# 后者是直接导入这个函数，你可以直接使用*这个函数了
import pandas as pd

pd.set_option('display.max_columns', 1000)
pd.set_option('display.width', 1000)
pd.set_option('display.max_colwidth', 1000)

import kNN
# from numpy import array
# import  array
# datingDatamat, datinglabels = kNN.file2matrix("datingTestSet2.txt")
#
# print(datingDatamat)
# print(datinglabels)
#
# import matplotlib
# import matplotlib.pyplot as plt
# fig = plt.figure()
# ax = fig.add_subplot(111)
# ax.scatter(datingDatamat[:,0],datingDatamat[:,1],15.0*np.array(datinglabels),15.0*np.array(datinglabels))
# plt.show()
#
# normmat,ranges,minVals = kNN.autoNorm(datingDatamat)
# print(normmat)
# print(ranges)
#
# print(minVals)


# print(kNN.classify0([0,0],group,labels,3))
# print(kNN.datingClassTest())
print(kNN.classifyPerson())