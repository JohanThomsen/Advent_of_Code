input = open("4th\input.txt", "r")
lines = input.readlines()

def isContainedFully(firstpart, secondpart):
    first_list, second_list = create_lists(firstpart, secondpart)

    if set(first_list).issubset(set(second_list)):
        return 1
    if set(second_list).issubset(set(first_list)):
        return 1
    return 0

def create_lists(firstpart, secondpart):
    firstpart_low, firstpart_high = firstpart.split('-')
    secondpart_low, secondpart_high = secondpart.split('-')
    first_list = []
    second_list = []
    first_list.extend(range(int(firstpart_low), int(firstpart_high)))
    first_list.append(int(firstpart_high))

    second_list.extend(range(int(secondpart_low), int(secondpart_high)))
    second_list.append(int(secondpart_high))
    return first_list,second_list

def isContainedPartially(firstpart, secondpart):
    first_list, second_list = create_lists(firstpart, secondpart)

    for task in first_list:
        if task in second_list:
            return 1
    return 0

#task1
sum = 0
for line in lines:
    firstpart, secondpart = line.split(',')
    sum += isContainedFully(firstpart, secondpart)
print(sum)
#task2
sum = 0
for line in lines:
    firstpart, secondpart = line.split(',')
    sum += isContainedPartially(firstpart, secondpart)
print(sum)


