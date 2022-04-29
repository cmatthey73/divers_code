print("Hello World")

name = input("aaaaa : ")
print(name)
print(type(name))

help(print)
print(dir(abs))

i=1
f=1.5
b=True
s="Donnerstag"

a=[i,f,b,s]
[type(z) for z in a]

names = ["Peter", "Mike", "Erika"]
numbers = [1,3,7]

for n in names:
    print(n)

for p in enumerate(names):
    print(type(p), p)

for i, n in enumerate(names):
    print(i,n)

for p in zip(numbers, names):
    print(type(p), p)

for i, n in zip(numbers, names):
    print(i,n)

def test(a,b,c):
    print(a,b,c)

test(*[1,2,55])

def apply(lst, f):
    new_items=[]
    for i in range(len(lst)):
        new_items.append(f(lst[i]))
    return new_items

prices=[3,78,99,900]
apply(prices, lambda x:x**2)

words = ["Alice", "alfred", "Berta", "beni"]

words.sort()

words = ("Hello", "World", "Hello")
unique_words = set(words)

d = {
      1:"Hello",
      2:"World"
}

print(d[1])
print(d.get(2))
print(d.get(3, "Aaaaa"))

class Person:

    countP = 0

    def __init__(self, firstn, lastn, jahrg):
        self.firstname = firstn
        self.lastname = lastn
        self.jahrgang = jahrg
        Person.countP += 1
        print(Person.countP)

    def name(self):
        return str(self.firstname) + " " + str(self.lastname)

    def __str__(self) :
        return str(self.firstname) + " " + str(self.lastname)+ " " + str(self.jahrgang)

p1 = Person("AaAaa", "Bbbbb", 1956)
p1.name()
print(p1)

p2 = Person("Eddde", "LLllllll", 1989)

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 

# Read XL
df = pd.read_excel("umsatz.xlsx")

monate = df["Monat"].to_list()
umsaetze = df["Umsatz"].to_list()

# Barchart
plt.bar(monate, umsaetze)
plt.bar(df["Monat"], df["Umsatz"])
plt.show()




