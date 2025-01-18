var = input("camelCase: ")
for char in var:
    if char.isupper():
        var = var.replace(char, f'_{char.lower()}')
print(var)
