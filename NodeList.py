class Node:
    def __init__(self, value: int, next=None) -> None:
        self.value = value
        self.next = next

    def __str__(self) -> str:
        return f'{self.value}'
    

class Add:
    @staticmethod
    def addstart(NodeList, value: int|list) -> None:
        def add(val):
            NodeList.len += 1

            node = Node(val, NodeList.head)
            NodeList.head = node

        if type(value) == int:
            add(value)
            return

        for i in value[::-1]:
            add(i)

    @staticmethod
    def addend(NodeList, value: int|list):
        def add(val):
            NodeList.len += 1
            head = NodeList.head

            if head == None:
                head = Node(val)

            while head.next:
                head = head.next

            head.next = Node(val)

        if type(value) == int:
            add(value)
            return
        
        for i in value:
            add(i)


class Remove:
    @staticmethod
    def pop(NodeList, index: int=-1) -> None:
        head = NodeList.head

        if (index * -1 >= NodeList.len or
                index == 0):
            NodeList.head = head.next
            NodeList.len -= 1
            return
        if index <= -1:
            index = NodeList.len + index
        
        for i in range(index-1):
            head = head.next
            if head is None:
                return

        head.next = head.next.next
        NodeList.len -= 1

    @staticmethod
    def remove(NodeList, value: str) -> None:
        head = NodeList.head

        if head.value == value:
            NodeList.head = head.next
            NodeList.len -= 1
            return

        while head.next.value != value and not (head.next is None):
            head = head.next

        if head is None:
            return
        
        head.next = head.next.next
        NodeList.len -= 1


class LinkedList(Remove, Add):
    def __init__(self, head: Node = None) -> None:
        self.head = head
        self.len = 0

    def __str__(self) -> str:
        return f'len {self.len} [{self.__print_list(self.head)}'

    def __print_list(self, head: Node) -> None:
        if head.next is None:
            return f'{head.value}]'
        return f'{head.value}, {self.__print_list(head.next)}'


    def search(self, value: int) -> bool:
        head = self.head

        while not(head is None) and head.value != value:
            head = head.next

        if head is None:
            return False
        
        return True
    
    def count(self, value: int) -> int:
        head = self.head
        count = 0

        while not(head is None):
            if head.value == value:
                count += 1
            head = head.next
    
        return count

    def get(self, start: int, end: int=0, step: int=1) -> int|list:
        head = self.head
        mass = []
        print(start, end, step)

        if (start >= self.len or start < 0 or  
                end - 1 >= self.len or end < 0 or
                step <= 0 or (start > end and end != 0)):
            print(123)
            return

        if end == 0:
            for i in range(start):
                head = head.next
            return head.value


        for i in range(start):
            head = head.next

        for i in range(start, end, step):
            mass.append(head.value)
            head = head.next

        return mass


    def addstart(self, value: int) -> None:
        super().addstart(self, value)

    def addend(self, value: int) -> None:
        super().addend(self, value)

    def pop(self, index: int=-1) -> None:
        super().pop(self, index)

    def remove(self, value: int) -> None:
        super().remove(self, value)



def main():
    ...


if __name__ == '__main__':
    main()

