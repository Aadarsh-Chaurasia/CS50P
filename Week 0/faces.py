def convert(data):
    data = data.replace(':)', '🙂')
    data = data.replace(':(', '🙁')
    return data

def main():
    print(convert(input('Enter your emotions: ')))

main()