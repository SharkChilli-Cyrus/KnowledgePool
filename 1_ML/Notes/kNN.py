# [1, 2]
#
# [
#     [1, 2],
#     [3, 4]
# ]
#
# [
#     [
#         [1, 2],
#         [3, 4]
#     ],
#     [
#         [5, 6],
#         [7, 8]
#     ]
# ]
# ==> index: [0, 0, 1] --> 2

import numpy as np
import pandas as pd
import operator

def createDataSet():
    # 创建数据集和标签
    group = array([1.0, 1.1], [1.0, 1.0],
                  [0, 0], [0, 0.1]
                  )
    labels = ['A', 'A', 'B', 'B']
    return group, labels


def calssify_kNN(inX, dataSet, labels, k):
    dataSetSize = dataSet.shape[0]
    diffMat = np.tile(inX, (dataSetSize, 1)) - dataSet # np.tile(A, reps)
    
    sqDiffMat = diffMat**2
    sqDistance = sqDiffMat.sum(axis=1)
    distance = sqDistance**0.5
    sortedDistIndicies = distance.argsort()
    
    classCount = {}
    for i in range(k):
        voteIlabel = labels[sortedDistIndicies[i]]
        classCount[voteIlabel] = classCount.get(voteIlabel, 0) + 1
        
  	sortedClassCount = sorted(classCount.iteritems(), 
                              key = operator.itemgetter(1),
                              reverse = True
                              )
    return sortedClassCount[0][0]
    
    
# ============================== Main ==============================
group, labels = createDataSet()



