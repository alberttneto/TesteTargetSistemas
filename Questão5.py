string = input("Informe a string: ")

inverso = ""

for i in range(len(string)):
    inverso += string[len(string)-1-i]

print(inverso)