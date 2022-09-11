from numpy import  *
import  operator
def createDataSet():
    group = array([[1.0,1.1],[1.0,1.0],[0,0],[0,0.1]])
    labels = ['A','A','B','B']
    return group,labels
def file2matrix(filename):
    fr = open(filename)
    arrayOLines = fr.readlines()
    numberOfLines = len(arrayOLines)
    returnMat = zeros((numberOfLines,3))
    classLabelVector = []
    index = 0
    for line in arrayOLines:
        line = line.strip()
        listFromLine = line.split('\t')
        returnMat[index,:] = listFromLine[0:3]
        classLabelVector.append(int(listFromLine[-1]))
        index += 1
    return returnMat,classLabelVector

def autoNorm(dataSet):
    minVals = dataSet.min(0)
    maxVals = dataSet.max(0)
    ranges = maxVals - minVals
    normDataSet = zeros(shape(dataSet))
    m = dataSet.shape[0]
    normDataSet = dataSet - tile(minVals,(m,1))
    normDataSet = normDataSet/tile(ranges,(m,1))
    return  normDataSet,ranges,minVals

def datingClassTest():
    hoRatio = 0.10
    datingDataMat,datingLabels = file2matrix('datingTestSet2.txt')
    normMat,ranges,minVals = autoNorm(datingDataMat)
    m = normMat.shape[0]
    numTestVecs = int(m*hoRatio) # 测试数据规模
    errorCount = 0.0
    for i in range(numTestVecs):
        # 二维数组的':'和','问题，有逗号就是分割行和列的切片的，而分号是在具体的行或者列上进行切片操作的
        classfierResult = classify0(normMat[i,:],normMat[numTestVecs:m,:],datingLabels[numTestVecs:m],3)
        print("the classifier came back with : ",classfierResult,"the real answer is : ",datingLabels[i])
        if(classfierResult != datingLabels[i]) :
            errorCount += 1.0
    print("the total error rate is : ",(errorCount/float(numTestVecs))*100,"%")


def classify0(inX,dataset,labels,k):
    datasetSize = dataset.shape[0]
    diffMat = tile(inX,(datasetSize,1)) - dataset
    sqDiffMat = diffMat**2
    # .sum(axis = 0)是压缩列，也就是所有列相加组成一行；.sum(axis = 1)就是压缩行，也就是所有行相加，压缩成为一行
    sqDistances = sqDiffMat.sum(axis=1)
    distances = sqDistances**0.5
    sortedDistIndicies = distances.argsort() # 把distances这个数组进行排序，并且把各个位置上的数换成其序号
    # 从这里开始不太明白了
    classCount = {}
    for i in range(k):
        voteIlabel = labels[sortedDistIndicies[i]]
        classCount[voteIlabel] = classCount.get(voteIlabel,0) + 1 # .get()返回字典中的对应的这个索引的值
    sortedClassCount = sorted(classCount.items(),key = operator.itemgetter(1),reverse = True)
    return sortedClassCount[0][0]

def classifyPerson():
    resultList = ['not at all','in small does','in large does']
    percentTats = float(input("percentage of time spent playing video games?"))
    ffMiles = float(input("frequent flier miles earned per year?"))
    iceCream = float(input("liters of the ice cream consumed per year?"))
    datingDataMat,datingLabels = file2matrix('datingTestSet2.txt')
    normMat,ranges,minVals = autoNorm(datingDataMat)
    inArr = array([ffMiles,percentTats,iceCream])
    classifierResult = classify0((inArr - minVals)/ranges,normMat,datingLabels,3)
    print('You will probably like this person',resultList[classifierResult - 1])
    return 0
#
# fp = open("./test.txt")
# arrayOLines = fp.readlines()
# # for line in arrayOLines:
# #     line = line.strip()
#
#     a = arrayOLines.split('\t')
# print(a)
