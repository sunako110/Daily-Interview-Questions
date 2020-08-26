# 02 - Apr - 2020

# Largest Product of 3 Elements

# You are given an array of integers. Return the largest product that can be made by multiplying any 3 integers in the array.
#
# Example:
#
# [-4, -4, 2, 8] should return 128 as the largest product can be made by multiplying -4 * -4 * 8 = 128.

def maximum_product_of_three(lst):
  # Fill this in.
    positive = 0
    product = 1
    if len(lst) < 3:
        return -1
    # for n in lst:
    #     if n > 0:
    #         positive += 1
    lst.sort(reverse=True)
    # for i in range(3):
    #     product *= lst[i]
    # if positive == len(lst) or positive == 0:
    #     return product
    # else:
    #     alternative = lst[0]
    #     for i in range(1,3):
    #         alternative *= lst[-i]
    #     if product > alternative:
    #         return product
    #     else:
    #         return alternative
    return max(lst[0] * lst[1] * lst[3], lst[0] * lst[-2] * lst[-1])



print(maximum_product_of_three([-4, -4, 2, 8]))
# 128