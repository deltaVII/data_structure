from nodeList.NodeList import LinkedList

class Stack():
    def __init__(self) -> None:
        self.head = LinkedList()

    def insert(self, value: any) -> None:
        self.head.addstart(value)

    def delete(self) -> None:
        self.head.pop(0)

    def get(self) -> any:
        return self.head.get(0)
            

