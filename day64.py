# 12 - May - 2020

# Circle of Chained Words

# Two words can be 'chained' if the last character of the first word is the same as the first character of the second word.
#
# Given a list of words, determine if there is a way to 'chain' all the words in a circle.
#
# Example:
# Input: ['eggs', 'karat', 'apple', 'snack', 'tuna']
# Output: True
# Explanation:
# The words in the order of ['apple', 'eggs', 'snack', 'karat', 'tuna'] creates a circle of chained words.

from collections import defaultdict

def chainedWords(words):
    # Fill this in.
    adj = defaultdict(list)
    visited = defaultdict()
    inp = defaultdict(int)
    start = words[0][0]
    for w in words:
        adj[w[0]].append(w[-1])
        visited[w[0]] = False
        inp[w[-1]] += 1

    return isEulerianCycle(start, visited, adj, inp)

# Method to check if this graph is Eulerian or not
def isEulerianCycle(start, visited, adj, inp):

    # Do DFS traversal starting from first non zero degree vertex.
    DFSUtil(start, visited, adj)

    # If DFS traversal doesn't visit all vertices, then return false.
    for i in adj.keys():
        if len(adj[i]) > 0 and visited[i] == False:
            return False
        # Check if in degree and out degree of every vertex is same
        if len(adj[i]) != inp[i]:
            return False

    # Create a reversed graph
    new_adj, new_inp, new_visited = getTranspose(adj)

    # Mark all the vertices as not visited (For second DFS)

    # Do DFS for reversed graph starting from first vertex.
    # Staring Vertex must be same starting point of first DFS
    DFSUtil(list(new_adj.keys())[0], new_visited, new_adj)

    # If all vertices are not visited in second DFS, then
    # return false
    for i in new_adj.keys():
        if len(new_adj[i]) > 0 and new_visited[i] == False:
            return False
        # Check if in degree and out degree of every vertex is same
        if len(new_adj[i]) != new_inp[i]:
            return False


    return True

def DFSUtil(v, visited, adj):

    # Mark the current node as visited and print it
    visited[v] = True

    # Recur for all the vertices adjacent to this vertex
    for i in range(len(adj[v])):
        if not visited[adj[v][i]]:
            DFSUtil(adj[v][i], visited, adj)

def getTranspose(adj):
    new_adj = defaultdict(list)
    inp = defaultdict(int)
    visited = defaultdict()
    for v in adj.keys():
        # Recur for all the vertices adjacent to this vertex
        for i in range(len(adj[v])):
            new_adj[adj[v][i]].append(v)
            visited[adj[v][i]] = False
            inp[v] += 1
    return new_adj, inp, visited

print(chainedWords(['apple', 'eggs', 'snack', 'karat', 'tuna']))
# True