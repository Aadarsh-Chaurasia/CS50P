def solve(x, y, z):
    x = float(x)
    z = float(z)
    if y == '+':
        return x + z
    elif y == '-':
        return x - z
    elif y == '*':
        return x * z
    elif y == '/':
        return x / z

def main():
    expression = input('Expression: ')
    x, y, z = expression.split(" ")
    print(solve(x, y, z))

main()
