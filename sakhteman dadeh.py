# کلاس صف ------------------

class Queue:
    def __init__(self,k):
        self.k=k
        self.queue=[None]*k
        self.front=-1
        self.rear=-1

# تابع نمایش کلاس
    def disqueue(self):
        if self.front==-1:
            print('empty')
        for i in range(self.front,self.rear):
            print(self.queue[i])

    
    #تابع اضافه کردن به کلاس
    def insqueue(self,data):
        if self.rear==-1:
            self.front=0
            self.rear=0
            self.queue[0]=data
        elif self.rear+1==self.k:
            print('is full')
            return 
        else:
            self.rear+=1
            self.queue[self.rear]=data

#تابع کم کردن از کلاس
    def delqueue(self):
        if self.front==-1:
            print('empty')

        elif self.front==self.rear:
            t=self.queue[self.front]
            self.front=-1
            self.rear=-1
            return t
        
        else:
            t=self.queue[self.front]
            self.front+=1
            return t
        
#کلاس صف چرخشی 

class Queue_C:
    def __init__ (self,k):
        self.k=k
        self.queue=[None]*k
        self.front=-1
        self.rear=-1

#اضافه کردن به کلاس صف چرخشی
    def insqueue_C(self,data):
        if (self.rear+1)%k==self.front:
            print('Full')
        
        elif self.front==-1:
            self.front=0
            self.rear=0
            self.queue[self.rear]=data

        else:
            self.rear+=1
            self.queue[self.rear]=data

#حذف از کلاس صف چرخشی
    def delqueue_C(self):
        if self.front==-1:
            print('empty')

        elif self.front==self.rear:
            t=self.queues[self.front]
            self.front=-1
            self.rear=-1
            return t 
        
        else:
            t=self.queue[self.front]
            self.front=(self.front+1)%k 
            return t
        
    

class Stack():
    def __init__(self,limit=10):
        self.stack=[]
        self.limit=limit

    def peek(self):
        if len(self.stack)<=0:
            return -1
        
        else:
            return self.stack[len(self.stack)-1]
        
    def display(self):
        if len(self.stack)<=0:
            return -1
        else:
            for i in self.stack:
                print(i)

#تمرین : با استفاده از ساختمان داده پشته تابع ای را بنویسید که عددی را از مبنای 10 به 2 ببرد
    def dec2bin(number):
        s=Stack()
        while number>0:
            r=number%2
            s.push(r)
            number=number//2

        b=""
        while not s.is_empty():
            b=b+str(s.pop())
            return b

    def is_empty(self):
        if len(self.stack)<=0:
            return True
        else:
            return False
        

#تمرین :با اسفاده از پشته تابع ای بنویسید که محتوای یک لیست را معکوس کند
    
    def reverse(lst):
        s=Stack()
        for e in lst:
            s.push(e)
        for i in range(len(lst)):
            lst[i]=s.pop()

    def revers_Stack(s):
        s1=Stack()
        s2=Stack()
        while not s.is_empty():
            s1.push(s.pop())
        while not s1.is_empty():
            s2.push(s1.pop())
        while not s2.is_empty():
            s.push(s2.pop())

    def respost(self, lst):
        for e in lst:
            if e == '*':
                t2 = self.pop()
                t1 = self.pop()
                if t1 is not None and t2 is not None:
                    t = t1 * t2
                    self.push(t)

            elif e == '+':
                t2 = self.pop()
                t1 = self.pop()
                if t1 is not None and t2 is not None:
                    t = t1 + t2
                    self.push(t)

            elif e == '-':
                t2 = self.pop()
                t1 = self.pop()
                if t1 is not None and t2 is not None:
                    t = t1 - t2
                    self.push(t)

            elif e == '/':
                t2 = self.pop()
                t1 = self.pop()
                if t1 is not None and t2 is not None and t2 != 0:
                    t = t1 / t2
                    self.push(t)
            else:
                self.push(e)
        return self.pop()

    def match_s(self, str):
        pairs = {')': '(', ']': '[', '}': '{'}
        for i in str:
            if i in '({[':
                self.push(i)
            elif i in ')]}':
                if self.is_empty() or self.peek() != pairs[i]:
                    return False
                else:
                    self.pop()
        return self.is_empty()

class Node:
    def __init__(self, d):
        self.data = d
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def display(self):
        t = self.head
        while t:
            print(t.data, end=' --> ')
            t = t.next
        print('None')

    def add_in_start(self, data):
        n = Node(data)
        n.next = self.head
        self.head = n

    def add_in_end(self, data):
        n = Node(data)
        if not self.head:
            self.head = n
        else:
            t = self.head
            while t.next:
                t = t.next
            t.next = n

    def add_after(self, m, d):
        n = Node(d)
        t = self.head
        while t and t.data != m:
            t = t.next
        if t:
            n.next = t.next
            t.next = n

    def del_first(self):
        if self.head:
            self.head = self.head.next
        else:
            return 'empty'

    def del_last(self):
        if self.head and self.head.next:
            t = self.head
            while t.next.next:
                t = t.next
            t.next = None

    def del_after(self, m):
        t = self.head
        while t and t.data != m:
            t = t.next
        if t and t.next:
            t.next = t.next.next

class DNode:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class Dnode:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

    class dlinkedlist:
        def __init__(self):
            self.head = None

        def display(self):
            t = self.head
            while t != None:
                print(t.data, end="<-->")
                t = t.next
            print('None')

        def add_in_start(self, d):
            n = Dnode(d)
            if self.head != None:
                n.next = self.head
                self.head.prev = n
            self.head = n

        def add_in_end(self, d):
            n = Dnode(d)
            if self.head != None:
                t = self.head
                while t.next != None:
                    t = t.next
                t.next = n
                n.prev = t
            else:
                self.head = n
                n.next = self.head
                self.head.prev = n
                self.head = n

        def add_after(self, m, d):
            n = Dnode(d)
            t = self.head
            while t.data != m:
                t = t.next
            n.next = t.next
            n.prev = t
            t.next = n
            n.next.prev = n

        def del_first(self):
            if self.head == None:
                return -1
            self.head = self.head.next
            self.head.prev = None

        def del_lat(self):
            if self.head == None:
                return -1
            t = self.head
            while t.next != None:
                t = t.next
            t.prev.next = None
            t.prev = None

        def delete(self, d):
            t = self.head
            while t.data != d:
                t = t.next
            t.next.prev = t.prev
            t.prev.next = t.next
            t.next = None
            t.prev = None

        def del_mid(self):
            t = self.head
            count = 0
            while t != None:
                count += 1
            t = self.head
            if count % 2 == 0:
                for i in range(count // 2):
                    t = t.next
            else:
                for i in range(count // 2 + 1):
                    t = t.next
            t.next.prev = t.prev
            t.prev.next = t.next
            t.next = None
            t.prev = None
class Dnode:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class Clinkedlist:
    def __init__(self):
        self.head = None

    def display(self):
        t = self.head
        if t is None:
            print("empty")
            return
        while t.next != self.head:
            print(t.data, end="-->")
            t = t.next

        print(t.data)

    def addfirst(self, data):
        n = Dnode(data)
        if self.head is None:
            self.head = n
            n.next = n
            return
        n.next = self.head
        t = self.head
        while t.next != self.head:
            t = t.next

        t.next = n
        self.head = n

    def addafter(self, m, data):
        if self.head is None:
            return -1

        n = Dnode(data)
        t = self.head
        while t.data != m:
            t = t.next
            if t == self.head:
                return -1

        n.next = t.next
        t.next = n

    def delete(self, data):
        if self.head is None:
            print("empty")
            return
        if self.head.next == self.head:
            if self.head.data == data:
                self.head = None
                return
            return -1
        t = self.head
        while t.data != data:
            p = t
            t = t.next
            if t == self.head:
                return -1

        p.next = t.next
        t.next = None
        
class BTnode:
    def __init__(self,data,left = None,right= None):
        self.data = data
        self.Left = left
        self.Right = right

class BTree:
    def __init__(self,root = None):
        self.root = root

    def inorder(self, root):
        if (root == None):
            return
        else:
            inorder(root.left)
            print(root.data)
            inorder(root.right)

    def postorder(self, root):
        if (root == None):
            return
        else:
            postorder(root.left)
            postorder(root.right)
            print(root.data)

            
