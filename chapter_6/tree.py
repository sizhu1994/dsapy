from chapter_5.sstack import LStack
from chapter_5.squeue import LQueue
class PrioQueueError(ValueError):
    pass
class PrioQue:
    def __init__(self,elist = []):
        self._elems = list(elist)
        self._elems.sort(reverse=True)
    def enqueue(self, e):
        i = len(self._elems) - 1
        while i>=0:
            if self._elems[i] < e:
                i -= 1
            else:
                break
        self._elems.insert(i+1, e)
    def is_empty(self):
        return not self._elems

    def peek(self):
        if self.is_empty():
            raise PrioQueueError('in PrioQue.peek')
        return self._elems[-1]

    def dequeue(self):
        if self.is_empty():
            raise PrioQueueError('in PrioQue.dequeue')
        return self._elems.pop()
class PrioQueue:
    def __init__(self, elist=[]):
        self._elems = list(elist)
        if elist:
            self.buildheap()
    def is_empty(self):
        return not self._elems
    def peek(self):
        if self.is_empty():
            raise PrioQueueError('in PrioQueue.peek')
        return self._elems[0]
    def enqueue(self, e):
        self._elems.append(None)
        self.siftup(e, len(self._elems)-1)

    def siftup(self, e, last):
        elems, i, j = self._elems, last, (last-1)//2
        while i>0 and e < elems[j]:
            elems[i] = elems[j]
            i, j = j, (j-1)//2
        elems[i] = e

    def dequeue(self):
        if self.is_empty():
            raise PrioQueueError('in Prioqueue.dequeue')
        elems = self._elems
        e0 = elems[0]
        e = elems.pop()
        if len(elems)>0:
            self.siftdown(e, 0, len(elems))
        return e0
    def siftdown(self, e, begin, end):
        elems, i, j = self._elems, begin, begin*2+1
        while j<end:
            if j+1 < end and elems[j+1] < elems[j]:
                j += 1
            if e<elems[j]:
                break
            elems[i] = elems[j]
            i, j = j, 2*j+1
        elems[i] = e

    def buildheap(self):
        end = len(self._elems)
        for i in range(end//2, -1, -1):
            self.siftdown(self._elems[i], i, end)



class BinTNode:
    def __init__(self, dat, left=None, right=None):
        self.data = dat
        self.left = left
        self.right = right

class BinTree:
    def __init__(self):
       def is_empty(self):
        return self._root is None
    def root(self):
        return self._root
    def leftchild(self):
        return self._root.left
    def rightchild(self):
        return self._root.right
    def set_root(self,roodnode):
        self._root = roodnode
    def set_left(self,leftchild):
        self._root.left = leftchild
    def set_right(self, rightchild):
        self._root.right = rightchild

    def preorder_elements(self):
        t, s = self._root, LStack()
        while t is not None or not s.is_empty():
            while t is not None:
                s.push(t.right)
                yield t.data
                t = t.left
            t = s.pop()


def levelorder(t, proc):
    qu = LQueue()
    qu.enqueue(t)
    while not qu.is_empty():
        t = qu.dequeue()
        if t is None:
            continue
        qu.enqueue(t.left)
        qu.enqueue(t.right)
        proc(t.data)
def preorder_nonrec(t, proc):
    s = LStack()
    while t is not None or not s.is_empty():
        while t is not None:
            proc(t.data)
            s.push(t.right)
            t = t.left
        t = s.pop()

def preorder_elements(t):
    s = LStack()
    while t is not None or not s.is_empty():
        while t is not None:
            s.push(t.right)
            yield t.data
            t = t.left
        t = s.pop()

def inorder_nonrec(t, proc):
    s = LStack()
    while t is not None or not s.is_empty():
        while t is not None:
            s.push(t)
            t = t.left
        t = s.pop()
        proc(t.data)
        t = t.right

def postorder_nonrec(t, proc):
    s = LStack()
    while t is not None or not s.is_empty():
        while t is not None:
            s.push(t)
            t = t.left if t.left is not None else t.right
        t = s.pop()
        proc(t.data)
        if not s.is_empty() and s.top().left == t:
            t = s.pop().right
        else:
            t = None
class HTNode(BinTNode):
    def __lt__(self, other):
        return self.data < other.data

class HuffmanPrioQ(PrioQueue):
    def number(self):
        return len(self._elems)\

def HuffmanTree(weights):
    trees = HuffmanPrioQ()
    for w in weights:
        trees.enqueue(HTNode(w))
    while trees.number() > 1:
        t1 = trees.dequeue()
        t2 = trees.dequeue()
        x = t1.data + t2.data
        trees.enqueue(HTNode(x,t1,t2))
    return trees.dequeue()



if __name__ == '__main__':
    t = BinTNode(0,BinTNode(1,BinTNode(3),BinTNode(4)),BinTNode(2,BinTNode(5,BinTNode(7)),BinTNode(6)))
    t = inorder_nonrec(t,lambda x:print(x,end=' '))
