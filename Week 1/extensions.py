def main():
    types = {
        'gif' : 'image/gif',
        'jpg' : 'image/jpeg',
        'jpeg' : 'image/jpeg',
        'png' : 'image/pdf',
        'pdf': 'application/pdf',
        'txt' : 'text/plain',
        'zip': 'application/zip'
        }
    file = input("File name: ")

    for extension, application in types:
        if extension in file.lower():
            print(application)
        else:
            print('application/octet-stream')

if __name__ == '__main__':
    main()