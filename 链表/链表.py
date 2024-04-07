class Node:
    def __init(self, initdata):
        self.data = initdata
        self.next = None
    def getData(self):
        return self.data
    def getNext(self):
        return self.next
    def setData(self, newdata):
        self.data = newdata
    def setNext(self, newnext):
        self.next = newnext

class UnorderedList:
    def __init__(self):
        self.head = None
    def isEmpty(self):
        return self.head == None
    def add(self, item):
        temp = Node(item)
        temp.setNext(self.head)
        self.head = temp
    def length(self):
        count = 0
        current = self.head
        while current != None:
            count += 1
            current = current.getNext()
        return count
    def search(self, item):
        current = self.head
        found = False
        while current != None:
            if current == item:
                found = True
                break
            else:
                current = current.getNext()
        return found
    def remove(self, item):
        # 链表中的数据是唯一的吗？是否可重复出现？
        previous = None
        found = False
        current = self.head
        while not found:   # 查
            if current == item:
                found = True
            else:
                previous = current
                current = current.getNext()
        # 删
        if previous != None:
            previous.setNext(current.getNext())
        else:
            self.head = current.getNext()
    
if __name__ == "__main__":

    ul = UnorderedList()
    ul.add(3)
    print(ul.length())
    ul.add(5)
    print(ul.length())
            
