class Node:
    def __init__(self, item, next):
        self.item = item
        self.nex = next

class Stack:
    def __init__(self):
        self.top is None

    def is_empty(self):
        self.top is None
        return

    def push(self, val):
        self.top = Node(val, self.top)

    def pop(self):
        if self.top is None:
            return None

        node = self.top
        self.top = self.top.next        #새로운 top을 기존의 top의 다음으로 지정
        return node.item
