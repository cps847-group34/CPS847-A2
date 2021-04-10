import sys

def ml(value_list):
    total = 1
    if len(value_list) == 0:
        total = 0
    for i in value_list:
        if isinstance(i, int):
            total = total * i
    return total

strOfNumbers = sys.argv[1]
listOfNumbers= [int(x) for x in strOfNumbers.split(',')]

print(ml(listOfNumbers))