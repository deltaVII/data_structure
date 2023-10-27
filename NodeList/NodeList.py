'''
Реализация связнных списков
'''

class Node:
    '''
    Узел связного списка
    '''
    def __init__(self, value: int, next=None) -> None:
        self.value = value
        self.next = next

    def __str__(self) -> str:
        return f'{self.value}'
    

class Add:
    '''
    Класс определяет статичные методы добавления элементов (post)
    '''
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
                NodeList.head = Node(val)
                return

            while head.next:
                head = head.next

            head.next = Node(val)

        if type(value) == int:
            add(value)
            return
        
        for i in value:
            add(i)
    @staticmethod
    def insert(NodeList, index: int, value: int) -> None:
        if index < 0 or index > NodeList.len:
            return
        if index == 0:
            NodeList.addstart(value)
            return
        if index == NodeList.len:
            NodeList.addend(value)
            return
        head = NodeList.head
        for i in range(index):
            head = head.next
        node = Node(value, head.next)
        head.next = node
        NodeList.len += 1


class Remove:
    '''
    Класс определяет статичные методы удаления элементов (delete)
    '''
    @staticmethod
    def pop(NodeList, index: int=-1) -> None:
        head = NodeList.head

        if index < -1 or index >= NodeList.len:
            return
        
        if index == -1 or index == NodeList.len:
            # из-за бага надо дойти до пред последнего элемента
            index = NodeList.len-1
        if index == 0:
            NodeList.head = head.next
            NodeList.len -= 1
            return
        
        for i in range(index-1):
            head = head.next
            if head is None:
                return

        head.next = head.next.next
        NodeList.len -= 1

    @staticmethod
    def remove(NodeList, value: int) -> None:
        head = NodeList.head

        if head.value == value:
            NodeList.head = head.next
            NodeList.len -= 1
            return

        while not (head.next is None) and head.next.value != value:
            head = head.next

        if head.next is None:
            return
        
        print(head)

        head.next = head.next.next
        NodeList.len -= 1

class Get:
    @staticmethod
    def search(NodeList, value: int) -> bool:
        head = NodeList.head

        while not(head is None) and head.value != value:
            head = head.next

        if head is None:
            return False
        
        return True
    
    @staticmethod
    def count(NodeList, value: int) -> int:
        head = NodeList.head
        count = 0

        while not(head is None):
            if head.value == value:
                count += 1
            head = head.next
    
        return count

    @staticmethod
    def get(NodeList, start: int, end: int=-1, step: int=1) -> int|list: 
        head = NodeList.head

        if (step <= 0 or (end <= start and end != -1)
                or end >= NodeList.len 
                or start >= NodeList.len or start < 0):
            return

        if end == -1:
            for i in range(start):
                head = head.next
            return head.value

        mass = [0] * ((end - start) - ((end - start)//step))

        for i in range(start):
            head = head.next

        for i in range(0, end-start, step):
            mass[i//step] = head.value

            for j in range(step):
                head = head.next

        return mass



class Update:
    @staticmethod
    def update(NodeList, index: int, value: int) -> None:
        head = NodeList.head
        
        if index > NodeList.len or index < 0:
            return
        for i in range(index):
            head = head.next

        head.value = value

class LinkedList(Remove, Add, Get, Update):
    '''
    Указатель на первый узел
    использует методы (post, delete)
    классов Add и Remove соответственно.
    Абсолютно все методы не допускают отрицательных индексов
    '''
    def __init__(self, head: Node = None) -> None:
        self.head = head
        self.len = 0

    def __str__(self) -> str: # WTF!?!?!?!?
        mass = [None] * self.len
        head = self.head
        for i in range(self.len): 
            mass[i] = head.value
            head = head.next
        return f'len:{self.len}, {mass}'
    
    def get_all(self):
        mass = [None] * self.len
        head = self.head
        for i in range(self.len): 
            mass[i] = head.value
            head = head.next
        return mass

    def get(self, start: int, end: int=-1, step: int=1) -> int|list:
        return super().get(self, start, end, step)

    def search(self, value: int) -> bool:
        return super().search(self, value)

    def count(self, value: int) -> int:
        return super().count(self, value)

    def update(self, index: int, value: int) -> None:
        super().update(self, index, value)

    def insert(self, index: int, value: int) -> None:
        super().insert(self, index, value)

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

