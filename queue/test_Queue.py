from .Queue import Queue

def test_get():
    queue = Queue()
    queue.insert(1)
    queue.insert(2)
    assert queue.get() == 1


def test_delete():
    queue = Queue()
    queue.insert(1)
    queue.insert(2)
    queue.delete()
    assert queue.get() == 2