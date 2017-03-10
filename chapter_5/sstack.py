from chapter_3.lnode import LList
class StackUnderflow(ValueError):
    pass
class SStack():
    def __init__(self):
        self._elems = []
    def is_empty(self):
        return self._elems == []
    def top(self):
        if self.is_empty():
            raise StackUnderflow('in SStack.top()')
        return self._elems[-1]
    def push(self, elem):
        self._elems.append(elem)
    def pop(self):
        if self.is_empty():
            raise StackUnderflow('in SStack.pop()')
        return self._elems.pop()

class LList3(LList):
    def top(self):
        return self._head.elem
class LStack():
    def __init__(self):
        self._elems = LList3()
        self._num = 0
    def is_empty(self):
        return self._num == 0
    def top(self):
        if self.is_empty():
            raise StackUnderflow('in SStack.top()')
        return self._elems.top()
    def push(self, elem):
        self._num += 1
        self._elems.prepend(elem)

    def pop(self):
        if self.is_empty():
            raise StackUnderflow('in LStack.pop()')
        self._num -= 1
        return self._elems.pop()
def check_parens(text):
    parens = '()[]{}'
    open_parens = '([{'
    opposite = {')':'(', ']':'[', '}':'{'}

    def parentheses(text):
        i, text_len = 0, len(text)
        while True:
            while i < text_len and text[i] not in parens:
                i += 1
            if i >= text_len:
                return
            yield text[i], i
    st = SStack()
    for pr, i in parentheses(text):
        if pr in open_parens:
            st.push(pr)
        elif st.pop() != opposite[pr]:
            print('Unmatching is found at', i, 'for', pr)
    print('All parentheses are correctly matched.')
    return True
class ESStack(SStack):
    def depth(self):
        return len(self._elems)

if __name__ == '__main__':
    myls = LStack()
    for i in range(10):
        myls.push(i)
    print(myls.top())

    while not myls.is_empty():
        print(myls.pop())
























