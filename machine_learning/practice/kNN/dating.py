import sys
import os
import operator

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

import kNN

def file_to_matrix(filepath):
    with open(filepath) as f:
        array_lines = f.readlines()
        # [line1, line2, line3, ...]
        # line1 = "feature1\tfeature2\tfeature3\tlabel\n"

        number_lines = len(array_lines)
        to_matrix = np.zeros((number_lines, 3))

        class_label_vector = []
        index = 0
        for line in array_lines:
            line = line.strip()
            each_line = line.split('\t')
            to_matrix[index, :] = each_line[0:3]
            class_label_vector.append(int(each_line[-1])) # int("label\n") => label: int
            index += 1
    
    return to_matrix, class_label_vector



if __name__ == "__main__":
    root_path = os.path.dirname(os.path.abspath(__file__))
    data_folder = os.path.join(root_path, "data")
    data_file = os.path.join(data_folder, "dating_DataSet.txt")

    training_set, class_label_vector = file_to_matrix(data_file)
    normalized_training_set, range_values, min_value = kNN.normalize(training_set)

    # fig = plt.figure()
    # ax = fig.add_subplot(111)
    # ax.scatter(normalized_training_set[:, 0], normalized_training_set[:, 1],
    #             np.array(class_label_vector), np.array(class_label_vector))
    # plt.show()

    # Classifier Test 
    k = 5
    test_ratio = 0.15
    data_size = normalized_training_set.shape[0]
    test_set_size = int(data_size * test_ratio)

    error_count = 0
    for i in range(test_set_size):
        test_result = kNN.classify(input_data = normalized_training_set[i, :],
                                   training_set = normalized_training_set[test_set_size:, :],
                                   labels = class_label_vector[test_set_size:],
                                   k = k)

        if test_result != class_label_vector[i]:
            print("- The classifier came back with: {0}, the real answer is : {1}".format(test_result, class_label_vector[i]))
            error_count += 1
        else:
            pass
    error_rate = error_count/test_set_size


    info = """
    --------------------------------------------------
    * Data Set Shape: {0}
    * Training Set Size: {1}
    * Test Set Size: {2}
    * Test Set Sample Ratio: {3}
    * kNN Classifier:
        k = {4}, Error Rate = {5}%
    --------------------------------------------------
    """.format(normalized_training_set.shape,
               normalized_training_set.shape[0] - test_set_size,
               test_set_size,
               test_ratio,
               k,
               round(error_rate * 100, 2))
    print(info)