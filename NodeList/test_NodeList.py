from .NodeList import LinkedList

def test_add():
    node_list = LinkedList()

    node_list.addstart(2)
    node_list.addstart(1)

    node_list = LinkedList()

    node_list.addend(3)
    node_list.addend(4)
    node_list.addstart([-2, -1, 0, 1])
    node_list.insert(3, 2)
    node_list.addend([5, 6, 7])
    assert node_list.get_all() == [i for i in range(-2, 8)]

def test_remove():
    node_list = LinkedList()
    node_list.addstart([-1, 0, 1, 2, 3, 4, 5])

    node_list.remove(-1)
    node_list.remove(-1)
    
    node_list.pop()
    node_list.pop(100)
    node_list.pop(0)

    assert node_list.get_all() == [i for i in range(1, 5)]

def test_get():
    node_list = LinkedList()
    node_list.addstart([-1, 0, 1, 2, 3, 3, 3])

    assert (
        node_list.search(-1) and not node_list.search(100) 
        and node_list.count(3) == 3 and node_list.count(100) == 0
        and node_list.get(0) == -1 and node_list.get(0, 5, 2) == [-1, 1, 3]
        and node_list.get(-2) is None and node_list.get(1, 100) is None
        and node_list.get() == 3
    )

def test_update():
    node_list = LinkedList()
    node_list.addstart([0, 1])

    node_list.update(0, 1)

    node_list.update(100, -1)
    assert node_list.get_all() == [1, 1]
