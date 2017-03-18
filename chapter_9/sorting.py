class record:
    def __init__(self, key, datum):
        self.key = key
        self.datum = datum

def insert_sort(lst):
    for i in range(1,len(lst)):
        x = lst[i]
        j = i
        while j > 0 and lst[j-1].key > x.key:
            lst[j] = lst[j-1]
            j -= 1
        lst[j] = x

def select_sort(lst):
    for i in range(len(lst) - 1):
        k = i
        for j in range(i, len(lst)):
            if lst[j].key < lst[k].key:
                k = j
        if i != k:
            lst[i], lst[k] = lst[k], lst[i]

def bubble_sort(lst):
    for i in range(len(lst)):
        found = False
        for j in range(1, len(lst)-i):
            if lst[j-1].key > lst[j].key:
                lst[j-1], lst[j] = lst[j], lst[j-1]
                found = True
        if not found:
            break

def quick_sort(lst):
    qsort_rec(lst, 0, len(lst)-1)

def qsort_rec(lst, l, r):
    if l >= r: return
    i, j = l, r
    pivot = lst[i]
    while i < j:
        while i < j and lst[j].key >= pivot.key:
            j -= 1
        if i < j:
            lst[i] = lst[j]
            i += 1
        while i < j and lst[i].key <= pivot.key:
            i += 1
        if i <  j:
            lst[j] = lst[i]
            j -= 1
        lst[i] = pivot
        qsort_rec(lst, l, i-1)
        qsort_rec(lst, i+1, r)



















