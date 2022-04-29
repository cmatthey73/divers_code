list_val = []

while(True):
    try:
        value = input("Value = ")
        if value == "x" :
            break
        value = int(value)
        list_val.append(value)
    except ValueError:
        print("Ungültiger Wert: ", value, "\n","Geben Sie bitte einen Integer Wert ein!")
    
print(list_val)
