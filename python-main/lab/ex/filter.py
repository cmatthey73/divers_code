
numbers=list(range(1,21))

# even_numbers = [i for i in numbers if i % 2 == 0]
even_numbers = list(filter(lambda x : x % 2 == 0, numbers))
odd_numbers = list(filter(lambda x : x % 2 != 0, numbers))
# odd_numbers = [i for i in numbers if i not in even_numbers] 

print(numbers)
print(even_numbers)
print(odd_numbers)

