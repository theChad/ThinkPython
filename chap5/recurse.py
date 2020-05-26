# Exercise 4.4

# Output: sum of integers from 1 to n, plus s.

# Stack diagram:
# __main__      |
# --------------------------------
# recurse       |n->3
#               |s->0
# --------------------------------
# recurse       |n->2
#               |s->3
# --------------------------------
# recurse       |n->1
#               |s->5
# --------------------------------
# recurse       |n->0
#               |s->6

# 4.4.1
# Infinite recursion. recurse is called again with n=-2, then n=-3..
# It always goes lower, so it'll never reach the base case (n=0).

# 4.4.2
"""Prints out the sum of s and the sum of integers 1 to n.
n: nonnegative integer
s: number
"""
