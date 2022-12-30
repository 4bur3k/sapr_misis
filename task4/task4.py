import csv
import math

def Solution(path_to_csv: str):
    #getting data from csv
    with open (path_to_csv, 'r') as f:
        reader = csv.reader(f, delimiter=',')
        data = [i for i in reader]

    graph = {}
    nodes = set()

    for pair in data:
        nodes.add(pair[0])
        nodes.add(pair[1])

        if int(pair[0]) not in graph:
            graph[int(pair[0])] = []

        graph[int(pair[0])].append(int(pair[1]))

    n = len(nodes)
    count_hierarchy = [[0]*5 for _ in range(n)]

    for i in graph.keys():
        for j in graph[i]:
            count_hierarchy[i - 1][0] += 1 
            count_hierarchy[j - 1][1] += 1 
            count_hierarchy[j - 1][4] += len(graph[i]) - 1
            if j in graph:
                count_hierarchy[i - 1][2] += len(graph[j]) 
                for k in graph[j]:
                    count_hierarchy[k - 1][3] += 1 
    dif_num = [0] * n
    for num_list in count_hierarchy:
        for i in range(1, n):
            dif_num[i] += num_list.count(i)
    
    enthropy = 0
    for i in range(1, len(dif_num)-1):
        enthropy -= dif_num[i] * i * math.log(i/(n-1), 2) * 1/(n-1)

    return enthropy

print(Solution('task.csv'))