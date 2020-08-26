# 25 - Mar - 2020

# Falling Dominoes

# Given a string with the initial condition of dominoes, where:
#
# . represents that the domino is standing still
# L represents that the domino is falling to the left side
# R represents that the domino is falling to the right side
#
# Figure out the final position of the dominoes. If there are dominoes that get pushed on both ends,
# the force cancels out and that domino remains upright.
#
# Example:
# Input:  ..R...L..R.
# Output: ..RR.LL..RR

class Solution(object):
  def pushDominoes(self, dominoes):
    # Fill this in.
    next_R = []
    next_L = []
    while True:
        old_dominoes = dominoes
        for i in range(len(dominoes)):
            if dominoes[i] == 'R':
                if i+2 < len(dominoes) and dominoes[i+2] == 'L':
                    continue
                elif i+1 < len(dominoes) and dominoes[i+1] == '.':
                    next_R.append(i+1)
            elif dominoes[i] == 'L':
                if i-2 >= 0 and dominoes[i-2] =='R':
                    continue
                elif i-1 >= 0 and dominoes[i-1] == '.':
                    next_L.append(i-1)
        for num in next_R:
            dominoes = dominoes[:num] + 'R' + dominoes[num+1:]
        next_R = []
        for num in next_L:
            dominoes = dominoes[:num] + 'L' + dominoes[num+1:]
        next_L = []
        if dominoes == old_dominoes:
            break
    return dominoes


print Solution().pushDominoes('..R...L..R.')
# ..RR.LL..RR