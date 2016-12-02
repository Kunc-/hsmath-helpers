import math, sys

# This will stop python from thinking i'm in an infinite loop
sys.setrecursionlimit(10009)

# This is the function that actually does the calculation.
def recurse_denom(odd, prog):
    if odd == -1:
        return prog
    return recurse_denom(odd-2, (odd**2)/(2+prog))

# This is a "wrapper" function. It allows the programmer to call a simpler function than
# the recursive one, and not have to worry about setting default values or additional calculations
def pi(depth):
    denom = 1 + recurse_denom((2*depth)-1, 1.0)
    return 4/denom


depth = input("Depth of approximation: ")
approx_pi = pi(depth)
print("Approximation of pi to depth of {}: {}\nError: {}".format(
        depth,
        approx_pi,
        # This statement calculates the difference between our pi and python's pi. It's an idea of error.
        approx_pi-math.pi
    ))
