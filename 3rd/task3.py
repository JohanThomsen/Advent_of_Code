input = open("3rd\input.txt", "r")
lines = input.readlines()

def get_prio(item):
    return ord(item)-96 if item.islower() else ord(item)-38
#task1
sum = 0
for line in lines:
    firstpart, secondpart = line[:len(line)//2], line[len(line)//2:]
    print(firstpart, secondpart)
    found_duplicates = []
    for char in firstpart:
        if char in secondpart:
            if char not in found_duplicates:
                print(char)
                found_duplicates.append(char)
                sum += get_prio(char)
print(sum)
#task2
for i in range(0, len(lines)-2, 3):
    er = i
    line1 = lines[i].strip()
    line2 = lines[i+1].strip()
    line3 = lines[i+2].strip()
    for char in line1:
        if char in line2 and char in line3:
            sum += get_prio(char)
            break
print(sum)
