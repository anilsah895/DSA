#BST for insert

class BST:
    def __init__(self, key):
        self.lchild = None
        self.rchild = None
        self.val = key

    def insert(self, data):
        if self.val == None:
            self.val = data
            return 
        if self.val == data:
            return
        if data < self.val:
            if self.lchild:
                self.lchild.insert(data)
            else:
                self.lchild = BST(data)
        else:
            if self.rchild:
                self.rchild.insert(data)
            else:
                self.rchild = BST(data)
    def search(self, data):
        if self.val == data:
            print("node is found!")
            return
        if data < self.val:
            if self.lchild:
                self.lchild.search(data)
            else:
                print("node is not present!")
        else:
            if self.rchild:
                self.rchild.search(data)
            else:
                print("node is not present!")

         
    
            
root = BST(10)
list1 = [11, 2, 3, 7, 0, 1, 10, 9]
for i in list1:
    root.insert(i)

root.search(-1)

            











