import itertools

file = open('password.txt', 'w')

items = ['Ehirim', 'Chiedozie', 'David', 'Mmaduakolam', '1996', '_']
permutations = list(itertools.permutations(items, 3))
for i in permutations:
    i = i[0]+i[1]+i[2]
    file.write(i+'\n')
file.close()