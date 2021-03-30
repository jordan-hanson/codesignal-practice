# You are given a directed acyclic graph (DAG) that contains N nodes.

# Write a function that can find all the possible paths from node 0 to node N - 1.

# graph[a] is a list of all nodes b for which the edge a -> b exists.

# Example:
# Graph illustration

# Input: graph = [[1, 2],[3],[3],[4],[]]
# Output: [[0,1,3,4], [0,2,3,4]]
# Note: The results must be returned in sorted order. You can use any built-in sort method on the results array at the end of your function before returning.

# [execution time limit] 4 seconds (py3)

# [input] array.array.integer graph

# [output] array.array.integer
def csFindAllPathsFromAToB(graph):
    
    dicti = {}
    result = []
    edges = []
    setc = set({})
    for i in range(0, len(graph)):
        result = {i : graph[i]}
        dicti.update(result)
    d_items = dicti.items()
    d_keys = dicti.keys()
    d_values = dicti.values()
    def addObject(key, values):
        for value in values:
            edges.append(list((key, value)))
            setc.add(value)
    for item in d_items:
        if item[0] not in setc:
            addObject(item[0], item[1])
            continue
        if item[0] in setc:
            for edge in edges:
                for num in edge:
                    if item[0] == num:
                        if len(item[1]) == 1:
                            edge.append(item[1][0])
                    else:
                        continue
    return edges

# Fails with this graph
# graph:
# [[4,3,1], 
#  [3,2,4], 
#  [3], 
#  [4], 
#  []]