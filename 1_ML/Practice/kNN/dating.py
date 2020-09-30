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
    print(training_set.shape)


    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.scatter(training_set[:, 0], training_set[:, 1],
                np.array(class_label_vector), np.array(class_label_vector))
    plt.show()

