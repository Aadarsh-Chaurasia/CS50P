data = input("Greeting: ")

if "hello" in data.lower():
    print("$0")
else:
    if data[0].lower() == 'h':
        print('$20')
    else:
        print('$100')
