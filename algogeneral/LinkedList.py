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

myList = LinkedList()
myList.curContent()
myList.addToEnd(2)
myList.addToEnd(3)
myList.addToEnd(4)
myList.curContent()


# myList.addToEnd(2)
# myList.addToEnd(1)
# myList.getLength()



