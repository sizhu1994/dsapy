class LinkedListUnderflow(ValueError): #链表错误
    pass
class LNode:                          #链表节点
    def __init__(self, elem, next_ = None):
        self.elem = elem
        self.next = next_
class LList:                        #普通单链表
    def __init__(self):
        self._head = None
        self.num = 0
    def seq2LL(self,l):
        for i in l:
            self.append(i)
    def is_empty(self):
        return self._head is None
    def prepend(self, elem):
        self._head = LNode(elem, self._head)
        self.num += 1
    def append(self, elem):
        self.num += 1
        if self._head is None:
            self._head = LNode(elem)
            return
        p = self._head
        while p.next is not None:
            p = p.next
        p.next = LNode(elem)
    def pop(self):
        if self._head is None:
            raise LinkedListUnderflow('in pop')
        e = self._head.elem
        self._head = self._head.next
        self.num -= 1
        return e
    def pop_last(self):
        if self._head is None:
            raise LinkedListUnderflow('in pop_last')
        p = self._head
        self.num -= 1
        if p.next is None:
            e = p.elem
            self._head = None
            return e
        while p.next.next is not None:
            p = p.next
        e = p.next.elem
        p.next = None
        return e
    def __len__(self):
        return self.num
    def find(self, pred):
        p = self._head
        while p:
            if pred(p.elem):
                return p.elem
            p = p.next
    def printall(self):
        p = self._head
        while p :
            print(p.elem, end='')
            if p.next is not None:
                print(',',end='')
            p = p.next
        print('')
    def for_each(self, proc):
        p = self._head
        while p:
            proc(p.elem)
            p = p.next
    def elements(self):
        p = self._head
        while p:
            yield p.elem
            p = p.next
    def __iter__(self):
        return self.elements()
    def filter(self, pred):
        p = self._head
        while p :
            if pred(p.elem):
                yield p.elem
            p = p.next
    def rev(self):
        p = None
        while not self.is_empty():
            q = self._head
            self._head = q.next
            q.next = p
            p = q
        self._head = p
class LList1(LList): #带有尾节点引用的单链表
    def __init__(self):
        LList.__init__(self)
        self._rear = None
    def prepend(self, elem):
        self.num += 1
        self._head = LNode(elem, self._head)
        if self._rear is None: #空表
            self._rear = self._head
    def append(self, elem):
        self.num += 1
        if self._head is None:
            self._head = LNode(elem)
            self._rear = self._head
        else:
            self._rear.next = LNode(elem)
            self._rear = self._rear.next
    def pop_last(self):
        if self._head is None:
            raise LinkedListUnderflow('in pop_last')
        p = self._head
        self.num += -1
        if p.next is None:
            self._head = None
            return p.elem
        while p.next.next:
            p = p.next
        e = p.next.elem
        p.next = None
        self._rear = p
        return e
class LCList:             #循环单列表类（尾部）
    def __init__(self):
        self._rear = None
    def is_empty(self):
        return self._rear is None
    def prepend(self, elem):
        p = LNode(elem)
        if self.is_empty():
            p.next = p
            self._rear = p
        else:
            p.next = self._rear.next
            self._rear.next = p
    def append(self,elem):
        self.prepend(elem)
        self._rear = self._rear.next
    def pop(self):
        if self.is_empty():
            raise LinkedListUnderflow('in pop of LCList')
        p = self._rear.next
        if self._rear is p:
            self._rear = None
        else:
            self._rear.next = p.next
        return p.elem
    def printall(self):
        if self.is_empty():
            return
        p = self._rear.next
        while True:
            print(p.elem)
            if p is self._rear:
                break
            p = p.next
    def turn(self, m):
        for i in range(m):
            self._rear = self._rear.next


class DLNode(LNode): #双链表节点
    def __init__(self, elem, prev=None, next_=None):
        LNode.__init__(self, elem, next_)
        self.prev = prev
class DLList(LList1):   #双链表
    def __init__(self):
        LList1.__init__(self)
    def prepend(self, elem):
        self.num += 1
        p = DLNode(elem, None, self._head)
        if self.is_empty():
            self._rear = p
        else:
            self._head.prev = p
        self._head = p
    def append(self, elem):
        self.num += 1
        p = DLNode(elem, self._rear,None)
        if self.is_empty():
            self._head = p
        else :
            self._rear.next = p
        self._rear = p
    def pop(self):
        if self.is_empty():
            raise LinkedListUnderflow
        e = self._rear.elem
        self.num += -1
        self._head = self._head.next
        if not self.is_empty():
            self._head = None
        return e

def Josephus(n, k, m):
    lcl = LCList()
    for i in range(n):
        lcl.append(i+1)
    lcl.turn(k-1)
    while not lcl.is_empty():
        lcl.turn(m-1)
        print(lcl.pop(), end=('\n' if lcl.is_empty() else ','))
def LL2seq(mylist):
    l = iter(mylist)
    p = list(l)


if __name__ == '__main__':
    mylist1 = LList()
    for i in range(10):
        mylist1.prepend(i)
    for i in range(11, 20):
        mylist1.append(i)
    mylist1.printall()
    mylist1.rev()
    mylist1.printall()
    Josephus(10,2,7)

