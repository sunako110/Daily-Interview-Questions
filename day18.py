# 21 - Mar - 2020

# Word Search

# You are given a 2D array of characters, and a target string.
# Return whether or not the word target word exists in the matrix.
# Unlike a standard word search, the word must be either going left-to-right, or top-to-bottom in the matrix.

# Example:
#
# [['F', 'A', 'C', 'I'],
#  ['O', 'B', 'Q', 'P'],
#  ['A', 'N', 'O', 'B'],
#  ['M', 'A', 'S', 'S']]
#
# Given this matrix, and the target word FOAM, you should return true,
# as it can be found going up-to-down in the first column.

def word_search(matrix, word):
    # Fill this in.
    for items in matrix:
        if convert(items) == word:
            return True

    transpose = list(map(list,zip(*matrix)))

    for items in transpose:
        if convert(items) == word:
            return True

    return False

def convert(list):
    word = ""
    for char in list:
        word += char
    return word

matrix = [
    ['F', 'A', 'C', 'I'],
    ['O', 'B', 'Q', 'P'],
    ['A', 'N', 'O', 'B'],
    ['M', 'A', 'S', 'S']]
print word_search(matrix, 'FOAM')
# True