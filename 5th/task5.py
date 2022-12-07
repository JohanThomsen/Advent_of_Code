import queue

input = open("5th\input.txt", "r")
lines = input.readlines()
list_dict = {
    
}
list_dict['list_1'] = ['M', 'S', 'J', 'L', 'V', 'F', 'N', 'R']
list_dict['list_2'] = ['H', 'W', 'J', 'F', 'Z', 'D', 'N', 'P']
list_dict['list_3'] = ['G', 'D', 'C', 'R', 'W']
list_dict['list_4'] = ['S', 'B', 'N']
list_dict['list_5'] = ['N', 'F', 'B', 'C', 'P', 'W', 'Z', 'M']
list_dict['list_6'] = ['W', 'M', 'R', 'P']
list_dict['list_7'] = ['W', 'S', 'L', 'G', 'N', 'T', 'R']
list_dict['list_8'] = ['V', 'B', 'N', 'F', 'H', 'T', 'Q']
list_dict['list_9'] = ['F', 'N', 'Z', 'H', 'M', 'L']

def make_queue(input_list):
    q = queue.LifoQueue()
    input_list.reverse()
    for char in input_list:
        q.put(char)
    return q

queue_dict = {}
for i in range(1,10):
    queue_dict[f'q{i}'] = make_queue(list_dict[f'list_{i}'])

def extract_x_from_queue(queue: queue.LifoQueue, amount):
    print(queue.qsize())
    extracted = []
    for i in range(0, int(amount)):
        extracted.append(queue.get())
    return extracted

def input_list_to_queue(queue: queue.LifoQueue, input_list):
    for element in input_list:
        queue.put(element)

def get_tops():
    tops = []
    for i in range(1,10):
        tops.append(queue_dict[f'q{i}'].get())
    return tops


#task1
def crateMover_9000():
    for line in lines:
        print(line)
        line = line.strip()
        _, amount, _, from_queue, _, to_queue = line.split(' ')
        tempList = extract_x_from_queue(queue_dict[f'q{from_queue}'], amount)
        input_list_to_queue(queue_dict[f'q{to_queue}'], tempList)

    tops = get_tops()
    return tops

#print(crateMover_9000())

#task2
def craterMover_9001():
    for line in lines:
        print(line)
        line = line.strip()
        _, amount, _, from_queue, _, to_queue = line.split(' ')
        tempList = extract_x_from_queue(queue_dict[f'q{from_queue}'], amount)
        tempList.reverse()
        input_list_to_queue(queue_dict[f'q{to_queue}'], tempList)
    return get_tops()

print(craterMover_9001())