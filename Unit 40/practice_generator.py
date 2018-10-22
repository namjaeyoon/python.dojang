def file_read():
    with open('words.txt') as file:
        while True:
            line = file.readline()
            if line == '':
                break
            yield line.strip('\n')

for i in file_read():
    print(i)
