
def maxi(n1, n2, n3=None):
    if n3 is None :
        out = n1 if n1 > n2 else n2
        print("max(%s, %s) = "%(n1, n2), out)
    elif n1 > n2 and n1 > n3 :
        out = n1
        print("max(%s, %s, %s) = "%(n1, n2, n3), out)
    elif n1 < n2 and n2 > n3 :
        out = n2
        print("max(%s, %s, %s) = "%(n1, n2, n3), out)
    else :
        print("max(%s, %s, %s) = "%(n1, n2, n3), n3)

maxi(4,5)
maxi(4,5, 8)
