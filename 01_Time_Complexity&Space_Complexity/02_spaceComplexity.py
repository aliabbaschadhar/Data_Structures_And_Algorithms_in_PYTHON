# Space complexity

# Space complexity is the amount of memory space required by an algorithm to run to completion.

# It is also measured in Big O, Big Omega and Big Theta notation.

# Space complexity is divided into two parts:
# 1. Fixed part: It is the space required by constants, simple variables, fixed-size variable components, program code, etc. This part is independent of the size of the problem.
# 2. Variable part: It is the space required by dynamic variables, recursion stack space, function call stack space, etc. This part is dependent on the size of the problem.

# Memory space is divided into two parts:
# 1. Auxiliary space: It is the extra space or temporary space used by an algorithm. It does not include space for input values.
# 2. Input space: It is the space required to store the input values. It is not included in the auxiliary space.

def sum(m,n,p):
    return m+n+p

result = sum(1,2,3)

print(result)  # Output: 6

# Here the result space is auxiliary space and the input space are for m, n and p.