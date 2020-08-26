# 20 - Mar - 2020

# Find Cycles in a Graph

# Given an undirected graph, determine if a cycle exists in the graph.

passed = []

def find_cycle(graph):
    # Fill this in.
    if not graph:
        return False
    for key, sub in graph.items():
        if key in passed:
            return True
        else:
            passed.append(key)
        if sub:
            if find_cycle(sub):
                return True
            else:
                continue
        else:
            continue
    return False


graph = {
  'a': {'a2':{}, 'a3':{} },
  'b': {'b2':{}},
  'c': {}
}
print(find_cycle(graph))
# False
graph['c'] = graph
print(find_cycle(graph))
# True