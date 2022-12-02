input = open("first\input.txt", "r")
lines = input.readlines()


#task1
max = 0
sum_of_elf = 0
for line in lines:
    if str.isspace(line):
        if sum_of_elf >= max:
            max = sum_of_elf
        sum_of_elf = 0
    else:
        sum_of_elf += int(line)

print(max)

#task2
calorie_list = []
for line in lines:
    if str.isspace(line):
        calorie_list.append(sum_of_elf)
        sum_of_elf = 0
    else:
        sum_of_elf += int(line)

calorie_list.sort()

print(sum(calorie_list[-3:]))
        