import sympy
from decimal import Decimal

while True:
    function = input("sin/cos/tan: ")
    if function[0].lower() == "s":
        function = lambda x : sympy.mpmath.degrees( sympy.asin( sympy.mpmath.radians(x) ) )

    elif function[0].lower() == "c":
        function = lambda x : sympy.mpmath.degrees( sympy.acos( sympy.mpmath.radians(x) ) )

    elif function[0].lower() == "t":
        function = lambda x : sympy.mpmath.degrees( sympy.atan( sympy.mpmath.radians(x) ) )

    else:
        print("Error, try again")
        continue
    break
try:
    front = Decimal(input("Front (blank for 1):"))
except:
    front = Decimal(1)

numerator = input("Numerator (Leave blank for 1)").split('r')
denominator = input("Denominator (leave blank for 1)").split('r')
if len(numerator) < 2:
    numerator = [1,1]
if len(denominator) < 2:
    denominator = [1,1]
for n in numerator:
    if n == "":
        n = 1
    n = sympy.Float(n)

for n in denominator:
    if n == "":
        n = 1
    n = sympy.Float(n)
print(numerator)
numerator = numerator[0] * sympy.sqrt(numerator[1])
denominator = denominator[0] * sympy.sqrt(denominator[1])

val = front * (numerator / denominator)
val = function(val)
print(val)
lower_bound = input("Lower Bound (blank = 0)")
upper_bound = input("Upper Bound (blank = 360)")
