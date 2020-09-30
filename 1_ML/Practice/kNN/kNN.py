# [1, 2]
# --
# [
#     [1, 2],
#     [3, 4]
# ]
# --
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

def create_data_set():
    # 创建数据集和标签
    data_set = np.array([[1.0, 1.1],
                         [1.0, 1.0],
                         [0, 0],
                         [0, 0.1]])
    labels = ["A", "A", "B", "B"]
    return data_set, labels


def normalize(data_set):
    """
    normalized_value = (value - min_value)/(max_value - min_value)
    """
    min_values = data_set.min(axis = 0)
    max_values = data_set.max(axis = 0)
    range_values = max_values - min_values

    normalized_data_set = zeros(data_set.shape)
    number = data_set.shape[0]
    normalized_data_set = data_set - np.tile(min_values, (number, 1))
    normalized_data_set = normalized_data_set/np.tile(range_values, (range_values, 1))

    return normalized_data_set, range_values, min_values


def calssify_kNN(input_data, training_set, labels, k):
    training_set_size = training_set.shape[0]
    diff = np.tile(input_data, (training_set_size, 1)) - training_set # np.tile(A, reps)
    
    sq_diff = diff ** 2
    sq_distance = sq_diff.sum(axis=1) # across -->
    distance = sq_distance ** 0.5
    sorted_distance_indicies = distance.argsort()
    
    class_count = {}
    for i in range(k):
        vote_label = labels[sorted_distance_indicies[i]]
        class_count[vote_label] = class_count.get(vote_label, 0) + 1
    
    sorted_class_count = sorted(class_count.items(),
                                key = operator.itemgetter(1),
                                reverse = True)
    # sorted_class_count = [(key, value), (key, value), ...]

    return sorted_class_count[0][0]
    
    
# ============================== Main ==============================
if __name__ == "__main__":
    data_set, labels = create_data_set()
    test_data = [0.2, 0.3]
    test_result = calssify_kNN(test_data, data_set, labels, 2)
    print("* Test Result: {0}".format(test_result))