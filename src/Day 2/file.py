# Day 2 
def openFile(filePath: str = 'example2.txt') -> list:
    pwd = list()
    with open(filePath, 'r') as file:
        for line in file.readlines():
            # pwd contains Policies & Password
            cur = line.split(': ')
            pwd.append((cur[0], cur[1]))
    return pwd

# Function for Part 1
def checkPassword(pwd: list) -> int:
    countValidPassword = 0
    for p in pwd:
        policies = p[0].split(sep=' ')
        min = int(policies[0].split('-')[0])
        max = int(policies[0].split('-')[1])
        character = policies[1]
        password = p[1]
        countChar = 0

        for c in p[1]:
            if c == character:
                countChar += 1
        if (countChar >= min and countChar <= max):
            countValidPassword += 1
    else:
        return countValidPassword

# Function for Part 2
def checkPasswordAdvanced(pwd: list) -> int:
    countValidPassword = 0
    for p in pwd:
        policies = p[0].split(sep=' ')
        min = int(policies[0].split('-')[0])
        max = int(policies[0].split('-')[1])
        character = policies[1]
        password = p[1]
        if ((character == password[min-1]) != (character == password[max-1])):
            countValidPassword += 1
    else:
        return countValidPassword

pwd = openFile()
print("Part 1 Result: {0}".format(checkPassword(pwd)))
print("Part 2 Result: {0}".format(checkPasswordAdvanced(pwd)))
