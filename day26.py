# 29 - Mar - 2020

# Course Prerequisites

# You are given a hash table where the key is a course code, and the value is a list of all the course codes
# that are prerequisites for the key. Return a valid ordering in which we can complete the courses.
# If no such ordering exists, return NULL.
#
# Example:
# {
#   'CSC300': ['CSC100', 'CSC200'],
#   'CSC200': ['CSC100'],
#   'CSC100': []
# }
#
# This input should return the order that we need to take these courses:
#  ['CSC100', 'CSC200', 'CSCS300']



def courses_to_take(course_to_prereqs):
  # Fill this in.
    seq = []

    color = {k: 1 for k in course_to_prereqs}
    class flag:
        is_possible = True

    def dfs(node):

        if not flag.is_possible:
            return

        color[node] = 2

        for neighbour in course_to_prereqs[node]:
            if color[neighbour] == 1:
                dfs(neighbour)
            elif color[neighbour] == 2:
                flag.is_possible = False
        color[node] = 3
        seq.append(node)

    for vertex in course_to_prereqs:
        if color[vertex] == 1:
            dfs(vertex)
    return seq if flag.is_possible else []

courses = {
  'CSC300': ['CSC100', 'CSC200'],
  'CSC200': ['CSC100'],
  'CSC100': []
}
print courses_to_take(courses)
# ['CSC100', 'CSC200', 'CSC300']
