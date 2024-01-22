 
#کلاس پشته 
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
