import math

def trapezium(a, b, dist):
    return (dist/2)*(a+b)

def simpson(a, b, c, dist):
    return (dist/6)*(a+c+4*b)
    
def eval_vars(statement, x):
    return eval(statement, math.__dict__, {"x":x})

def choice(choices, text):
    c = sorted(choices.keys())
    print(text)
    for i, x in enumerate(c):
        print("{}) {}".format(i+1, x))
    print("")
    num = int(input("Choice: ")) - 1
    return choices[c[num]]

print("""
Intergration Calculator
""")

HELP_TEXT = """
1) Enter an function using any functions in the math library.
2) Choose bounds (using any functions in the math library)
3) Choose method of intergration.

"""
while True:
    if choice({"Help": True, "Enter Formula": False}, "Options:"):
        print(HELP_TEXT)
        continue
    function = input("formula: f(x)=")
    function = function.replace("^", "**")

    bounds = [eval_vars(input("lower bound:"), None), eval_vars(input("upper bound:"), None)]

    algorithm_choices = {"Simpson's Rule": simpson, "Trapezoidal Rule": trapezium}

    algorithm = choice(algorithm_choices, "Choose algorithm for approximation: ")

    ops = int(input("Number of applications: "))

    num_values = ops+1 if algorithm == trapezium\
            else ops*2 + 1

    difference = (bounds[1]-bounds[0])/(num_values-1)

    values = []

    for i in range(num_values+1):
        values.append(eval_vars(function, bounds[0]+ i*difference))

    approximation = 0
    if algorithm == simpson:
        for m, n in zip(range(0, num_values-1, 2), range(2, num_values+1, 2)):
            approximation+= simpson(*values[m:n+1]+[difference*2])

    if algorithm == trapezium:
        for m in range(num_values):
            approximation += trapezium(values[m], values[m+1],difference)

    print("Approximately: {}".format(approximation))
