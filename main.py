with open("test.txt", encoding='utf') as f:
    line = f.readline()
    while line != '':
        print(line, end='')
        line = f.readline()

print("\n=======")

with open("test.txt", encoding='utf') as f:
    for linea in f:
        print(linea, end='')
