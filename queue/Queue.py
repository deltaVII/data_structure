from nodeList.NodeList import LinkedList

class Queue:
    def __init__(self):
        self.head = LinkedList()
    
    def get(self) -> any:
        return self.head.get(0)
    
    def insert(self, value: any) -> None:
        self.head.addend(value)

    def delete(self):
        self.head.pop(0) 
    
