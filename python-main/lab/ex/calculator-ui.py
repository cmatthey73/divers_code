
import calculator as calc
import re

op = input("Le calcul : ")
n1, o, n2 =op.split()

# msg = None
# if "+" in op:
#     res = calc.add(int(n1), int(n2))
# elif "*" in op:
#     res = calc.mult(int(n1), int(n2))
# elif "/" in op:
#     if int(n2) == 0:
#         msg = "Division durch 0"
#     else:
#         res = calc.div(int(n1), int(n2))
# elif "-" in op:
#     res = calc.sub(int(n1), int(n2))
# else :
#     msg = "Ungültier Operator"

# if msg is None :
#     print("Calculate : ", op, "\n", res)
# else:
#     print(msg)

map = {"+" : calc.add, "-" :calc.sub, "*" : calc.mult, "/" :calc.div}
f = map.get(o)
if f is None :
    print("Ungültier Operator")
elif f == calc.div and float(n2) == 0:
    print("Division durch 0")
else :
    print("Calculate : ", op, "\n", f(float(n1), float(n2)))
 

