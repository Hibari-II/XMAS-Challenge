# Day 1 
def openFile(filePath: str = 'example1.txt') -> list:
    l = list()
    with open(filePath, 'r') as file:
        for line in file.readlines():
            c = line.split(sep='\n')[0]
            l.append(int(c))
    return l

def calculate(lnum: list, isPartOne: bool = True):
    if (isPartOne):
        for i in range(len(l)):
            for j in range(i,len(l)):
                if (l[i] + l[j] == 2020):
                    print('{} + {} = {}'.format(l[i], l[j], l[i] + l[j]))
                    print('Part 1: {}'.format(l[i] * l[j]))
    else:
        for i in range(len(l)):
            for j in range(i,len(l)):
                for k in range(j,len(l)):
                    first = l[i]
                    second = l[j]
                    third = l[k]
                    if (first + second + third == 2020):
                        print('{} + {} + {} = {}'.format(first,second,third, first + second + third))
                        print('Part 2: {}'.format(first*second*third))

l = openFile()
calculate(l)
calculate(l, False)