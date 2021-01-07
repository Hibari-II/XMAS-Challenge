def openFile(filePath: str = 'example4.txt') -> list:
    data = list()
    with open(filePath, 'r') as file:
        for line in file.readlines():
            data.append(line)
    return data

def createPassports(data: list = None) -> dict:
    if data is None:
        return
    passports = [dict()]
    countPerson = 0

    for i in range(len(data)):
        line = data[i]
        if (line == '\n'):
            countPerson += 1
            passports.append(dict())
            continue

        for substr in line.split(' '):
            pKey = substr.split(':')[0]
            pValue = substr.split(':')[1] if ('\n' not in substr) else substr.split(':')[1].split('\n')[0]
            passports[countPerson].update({pKey:pValue})
    return passports

def checkPassports(data:list = None) -> int:
    validPassports = 0
    fields = {'byr':(1920,2002), 
              'iyr':(2010,2020), 
              'eyr':(2020,2030), 
              'hgt':(('cm',150,193), 
                     ('in',59,76)), 
              'hcl':('#',6), 
              'ecl':('amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'), 
              'pid':(9)}

    for passport in data:
        for field in fields:
            if field not in passport:
                break
            else:
                pass
                
        else:
            validPassports += 1

    return validPassports

def checkField(fieldName: str, boundaries: tuple) -> bool:

    pass

passports = createPassports(openFile())
print(checkPassports(passports))