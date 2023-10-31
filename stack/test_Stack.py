from .Stack import Stack


class TestStack():
    def test_insert_and_get(self):
        stack = Stack()
        stack.insert(1)
        stack.insert(2)
        stack.insert(3)
        assert stack.get() == 3

    def test_delete(self):
        stack = Stack()
        stack.insert(1)
        stack.insert(2)
        stack.insert(3)
        stack.delete()
        assert stack.get() == 2
