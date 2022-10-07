import re


# returns the list of nodes and their relation
def task(file_content):

    nodes = re.findall(r'\d', file_content)

    nodes = [int(item) for item in nodes]

    graph = {i: [] for i in range(1, max(nodes) + 1)}

    string = file_content.split('\n')

    if string[-1] == '':
        del string[-1]

    for i in string:
        nodes = i.split(',')
        graph[int(nodes[0])].append(nodes[1])

    r1, r2, r3, r4, r5 = [], [], [], [], []


    for key in graph:
        if len(graph[key]) > 0:
            r1.append(key)
        for exit_node in graph[key]:
            if int(exit_node) not in r2:
                r2.append(int(exit_node))

    for i in r1:
        if len(graph[i]) > 1:
            for exit_node in graph[i]:
                if int(exit_node) not in r5:
                    r5.append(int(exit_node))
        for exit_node_1 in graph[i]:
            for exit_node_2 in graph[int(exit_node_1)]:
                if i not in r3:
                    r3.append(i)
                if int(exit_node_2) not in r4:
                    r4.append(int(exit_node_2))

    return [r1, r2, r3, r4, r5]



def main():
    with open('data.csv') as file:
        file_content = file.read()
        task(file_content)


if __name__ == '__main__':
    main()
