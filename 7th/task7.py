input = open("7th\input.txt", "r")
#input = open("7th\\testInput.txt", "r")
lines = input.readlines()

class node:
    def __init__(self,name: str, parent):
        self.name = name
        self.parent = parent

    def get_parent(self):
        return self.parent
    
    def climb_to_root(self):
        currentNode = self
        if self.parent is not None:
            return self.parent.climb_to_root()
        else:
            return currentNode

class directory(node):
    def __init__(self, name: str, parent):
        super().__init__(name, parent)
        self.children = []
        self.size = 0
        self.bigSubDir = False

    def add_child(self, node):
        self.children.append(node)

    def get_size(self):
        for node in self.children:
            if (isinstance(node, file)):
                self.size += node.Filesize
            elif (isinstance(node, directory)):
                self.size += node.get_size()
        return self.size
    
    def get_closest_value(self, spaceNeeded, closestValue):
        for node in self.children:
            if (isinstance(node, directory)):
                closestValue = node.get_closest_value(spaceNeeded, closestValue)
                if self.size > spaceNeeded:
                    if self.size - spaceNeeded < closestValue:
                        print(self)
                        closestValue = self.size - spaceNeeded
        return closestValue          
     

    def get_size_of_sum_less_than_100000(self):
        for node in self.children:
            if (isinstance(node, file)):
                self.size += node.Filesize
            elif (isinstance(node, directory)):
                subDirSize = node.get_size_of_sum_less_than_100000()
                if subDirSize == -1:
                    self.bigSubDir = True
                self.size += subDirSize
        if self.size <= 100000:
            if self.bigSubDir == False:
                dirLessThan100000.append(self)
                return self.size
            return -1
        self.size = 0
        return -1
        
    def get_child(self, childName):
        for node in self.children:
            if node.name == childName:
                return node
        return None
    
    def get_sub_dirs(self):
        return [node for node in self.children if isinstance(node, directory)]

    def __repr__ (self) -> str:
        return f"dir: {self.name}, size: {self.size}"
        
class file(node):
    def __init__(self, name: str, parent, Filesize: int):
        super().__init__(name, parent)
        self.Filesize = Filesize
    
    def __repr__ (self) -> str:
        return f"file: {self.name} - {self.Filesize}"

dirLessThan100000 = []
def add_dir_sizes(nodes):
    size = 0
    for node in nodes:
        size += node.size
    return size

currentNode = directory('/', None)
#task1
for line in lines:
    line = line.strip()
    split = line.split(' ')
    if len(split) == 3:
        #CD command
        dirName = split[2]
        if dirName == '..':
            currentNode = currentNode.get_parent()
        else:
            currentNode = currentNode.get_child(dirName)
    elif len(split) == 2:
        firstWord = split[0]
        secondWord = split[1]

        if(firstWord == '$'):
            #LS command
            continue
        elif(firstWord == 'dir'):
            #Dir info
            currentNode.add_child(directory(secondWord, currentNode))
        else:
            #File info
            currentNode.add_child(file(secondWord, currentNode, int(firstWord)))
root = currentNode.climb_to_root()
#answerSize = root.get_size_of_sum_less_than_100000()
#print(rootSize)
#print(answerSize)
#print(add_dir_sizes(dirLessThan100000))
#task2
closestValue = 70000000
rootSize = root.get_size()
print(rootSize)
spaceAvailable = 70000000 - rootSize
print(spaceAvailable)
spaceNeeded = 30000000 - spaceAvailable
print(spaceNeeded)
closestValue = root.get_closest_value(spaceNeeded, closestValue)
print(closestValue)

        