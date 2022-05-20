import collections

class MyStack:

    def __init__(self):
        self.q = collections.deque()

    def push(self, x: int) -> None:
        self.q.append(x)
        for _ in range(len(self.q) - 1):
            self.q.append(self.q.popleft())    #스택처럼 늦게 들어온게 선출 되어야 하기 때문에 큐에서는 맨 왼쪽이 선출됨으로 맨 왼쪽으로 이동하기

    def pop(self) -> int:
        return self.q.popleft()

    def top(self) -> int:
        return self.q[0]

    def empty(self) -> bool:
        return len(self.q) == 0


