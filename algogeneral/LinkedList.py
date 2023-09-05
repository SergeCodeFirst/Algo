class node:
    def __init__(self, value=None):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = node()

    def addToEnd(self, value):
        newNode = node(value)
        curNode = self.head
        while curNode.next != None:
            curNode = curNode.next
        curNode.next = newNode

    def getLength(self):
        myLength = 0
        curNode = self.head
        while curNode.next != None:
            myLength+=1
            curNode = curNode.next
        return myLength
    
    def curContent(self):
        element =[]
        curNode = self.head
        while curNode.next != None:
            curNode = curNode.next
            element.append(curNode.value)
        print(element)

    def extract(self,index):
        cur_node = self.head
        pointer = -1

        if index >= self.getLength() or index < self.getLength():
            return "Index out of range"
        
        while cur_node.next != None:
            if index == pointer:
                return cur_node.value
            pointer += 1
            cur_node = cur_node.next

        if index == pointer:
            return cur_node.value
        
    def remove(self, index):
        cur_node = self.head
        pointer = -1
        preNode = cur_node

        if index >= self.getLength():
            print(f"Index out of range")
            return self

        while cur_node.next != None:
            if pointer == index:
                preNode.next = cur_node.next
                cur_node.next = None
                print(f"deleted node at index: {index}")
                return self
            preNode = cur_node
            cur_node = cur_node.next
            pointer += 1




myList = LinkedList()

# myList.curContent()
# print(myList.getLength())

myList.addToEnd(2)
myList.addToEnd(3)
myList.addToEnd(4)
myList.curContent()
# print(myList.getLength())

# print(myList.extract(2))
# print(myList.extract(3))

print(myList.remove(0).curContent())
# print(myList.remove(1))
# print(myList.remove(3))
# myList.curContent()


