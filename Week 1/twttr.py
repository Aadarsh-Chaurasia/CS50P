s = input('Input: ')
vowels = ['a', 'e', 'i', 'o', 'u']
s = ''.join([char for char in s if (char.lower() not in vowels)])
print(f'Output: {s}')
