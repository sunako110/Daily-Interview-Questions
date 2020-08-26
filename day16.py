# 19 - Mar - 2020

# Create a Simple Calculator

# Given a mathematical expression with just single digits,
# plus signs, negative signs, and brackets, evaluate the expression. Assume the expression is properly formed.

# Example:
# Input: - ( 3 + ( 2 - 1 ) )
# Output: -4

def eval(expression):
        # Fill this in.
        expression = expression.replace(' ','')
        if len(expression) == 1:
            return int(expression)
        else:
            if expression[0] == '-':
                return -1 * eval(expression[1:])
            if expression[0] == '+':
                return 1 * eval(expression[1:])
            if expression[0] == '(':
                return eval(expression[1:-1])
            else:
                if expression[1] == '-':
                    return int(expression[0]) - eval(expression[2:])
                if expression [1] == '+':
                    return int(expression[0]) + eval(expression[2:])

print eval('- (3 + ( 2 - 1 ) )')
# -4