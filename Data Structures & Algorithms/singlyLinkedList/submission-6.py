class Node:
    def __init__(self, val):
        self.value = val
        self.next = None

class LinkedList:
    
    def __init__(self):
        self.head = 0
        self.tail = 0
    
    def get(self, index: int) -> int:
        current = self.head
        i = 0
        while current:
            if i == index:
                return current.value
            current = current.next
            i += 1
        
        return -1

    def insertHead(self, val: int) -> None:
        new = Node(val)
        if not self.head:
            self.head = self.tail = new
        else:
            new.next = self.head
            self.head = new

    def insertTail(self, val: int) -> None:
        new = Node(val)
        if not self.head:
            self.head = self.tail = new
        else:
            self.tail.next = new
            self.tail = new       

    def remove(self, index: int) -> bool:
        if not self.head:
            return False

        if index == 0:
            self.head = self.head.next
            if not self.head:
                self.tail = None
            return True
        
        current = self.head
        i = 0
        while current and current.next:
            if i + 1 == index:
                if current.next == self.tail:
                    self.tail = current
                current.next = current.next.next
                return True
            
            current = current.next
            i += 1

        return False


    def getValues(self) -> List[int]:
        arr = []
        current = self.head
        if not self.head:
            return arr

        while current:
            arr.append(current.value)
            current = current.next

        return arr

        
