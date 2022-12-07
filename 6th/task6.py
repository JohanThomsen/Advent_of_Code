input = open("6th\input.txt", "r")
input = input.read()

def check_unique(str):
    for i in range(len(str)):
        for j in range(i + 1,len(str)):
           if(str[i] == str[j]):
                return False
    return True

#task1
for i in range(0, len(input) - 1):
    nextFour = input[i:i+4]
    isUnique = check_unique(nextFour)

    if isUnique:
        print(nextFour)
        print(i+4)
        break
#task2
for i in range(0, len(input) - 1):
    nextFourteen = input[i:i+14]
    isUnique = check_unique(nextFourteen)

    if isUnique:
        print(nextFourteen)
        print(i+14)
        break
        