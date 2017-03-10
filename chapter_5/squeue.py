from chapter_3.lnode import LList1
class QueueUnderflow(ValueError):
    pass
class SQueue():
    def __init__(self, len = 8):
        assert isinstance(len, int),'长度应为整数'
        self._len = len
        self._num = 0
        self._head = 0
        self._elems = [0] * len

    def is_empty(self):
        return self._num == 0

    def peek(self):
        if self.is_empty():
            raise QueueUnderflow('error in SQueue.peek')
        return self._elems[self._head]

    def dequeue(self):
        if self.is_empty():
            raise QueueUnderflow('error in SQueue.dequeue')
        e = self._elems[self._head]
        self._head = (self._head + 1) % self._len
        self._num -= 1
        return e

    def enqueue(self, e):
        if self._num == self._len:
            self._extend()
        self._elems[(self._head + self._num) % self._len] = e
        self._num += 1

    def _extend(self):
        old_len = self._len
        self._len *= 2
        new_elems = [0]*self._len
        for i in range(old_len):
            new_elems[i] = self._elems[(self._head+i)%old_len]
        self._elems, self._head = new_elems, 0
class LList2(LList1):
    def top(self):
        return self._head.elem
class LQueue():
    def __init__(self):
        self._elems = LList2()
        self._num = 0

    def is_empty(self):
        return self._num == 0

    def peek(self):
        if self.is_empty():
            raise QueueUnderflow('error in SQueue.peek')
        return self._elems.top()

    def dequeue(self):
        if self.is_empty():
            raise QueueUnderflow('error in SQueue.dequeue')
        e = self._elems.pop()
        self._num -= 1
        return e

    def enqueue(self, e):
        self._elems.append(e)
        self._num += 1

if __name__ == '__main__':
    mylq = LQueue()
    for i in range(10):
        mylq.enqueue(i)
    print(mylq.peek())
    while not mylq.is_empty():
       print(mylq.dequeue(),end=' ')




