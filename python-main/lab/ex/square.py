
sq = lambda x : x**2

for i in [1,20,55,32,1,-5,-9,120,23,6]:
    sq(i)

lin = lambda x : 1 + 0.5*x
x_lst = range(-2, 4, 1)

for i in x_lst:
    print("y für x %s = %s"%(i, lin(i)))

