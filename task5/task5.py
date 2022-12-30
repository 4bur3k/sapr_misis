import json
import numpy as np


def make_json_matrix(data):

    for i in range(len(data)):
        if type(data[i]) == str:
            data[i] = [int(data[i])]

        elif type(data[i]) == list:
            for j in range(len(data[i])):
                data[i][j] = int(data[i][j])



def return_group(data, num):
    for i in range(len(data)):
        if num in data[i]:
            return i
    return -1


def matrix_to_sheet(ranking):
    matrix = []
    matrix_length = sum([len(i) for i in ranking])

    for i in range(matrix_length):
        l = [0] * matrix_length
        for j in range(return_group(ranking, i + 1), -1, -1):
            for j in ranking[j]:
                l[j - 1] = 1

        matrix.append(l)
    return np.matrix(matrix)


def get_kernel(table):
    kernel = list()
    for i in range(table.shape[0]):
        for j in range(i, table.shape[1]):
            if table[i, j] == 0:
                kernel.append([str(i + 1),str(j + 1)])
    return kernel


def task(json1, json2):
    ranking_1 = json.loads(json1)
    ranking_2 = json.loads(json2)

    make_json_matrix(ranking_1)
    make_json_matrix(ranking_2)

    res_table = np.multiply(matrix_to_sheet(ranking_1), matrix_to_sheet(ranking_2)).T
    kern = get_kernel(res_table)

    return kern