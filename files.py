### Playing With Files ###

def print_lines_file(some_file):
    for line in open(some_file):
        print(line)


f = open('data.txt','w')

f.write('Hello ')

f.write('world\n')

f.close

f = open('data.txt')

text = f.read()

print("Texto lido do arquivo: ",text)

print("Texto lido dividido: ",text.split())

print_lines_file('data.txt')
