
values = [7.5, 'Hello', 42, None, 'World', 1.25, 69, 12]
int_lst = []
float_lst= []
str_lst = []

for value in values :
    print(value, type(value))
    if type(value) is str :
        str_lst.append(value)
    elif type(value) is float :
        float_lst.append(value)
    elif type(value) is int :
        int_lst.append(value)
    elif value is None :
        print("None value detected")

print(values)
print(int_lst)
print(float_lst)
print(str_lst)

    
