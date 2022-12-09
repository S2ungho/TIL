class TreeNode():
    def __init__(self):
        self.data = None
        self.left = None
        self.right = None

def Preorder(node):
    if node == None:
        return
    print(node.data)
    Preorder(node.left)
    Preorder(node.right)

def Inorder(node):
    if node == None:
        return
    Inorder(node.left)
    print(node.data)
    Inorder(node.right)

def Postorder(node):
    if node == None:
        return
    Postorder(node.left)
    Postorder(node.right)
    print(node.data)

root = None
dataAry = ["1","2","3","4","5"]
node = TreeNode()
node.data = dataAry[0]
root = node
for name in dataAry[1:]:
    node = TreeNode()
    node.data = name
    current = root
    while True:
        if current.data > node.data:
            if current.left == None:
                current.left = node
                break
            current = current.left
        if current.data < node.data:
            if current.right == None:
                current.right = node
                break
            current = current.right
        
findData = "3"
current = root
while True:
    if findData == current.data:
        print("here")
        break
    elif findData < current.data:
        if current.left == None:
            print("x")
            break
        current = current.left
    elif findData > current.data:
        if current.right == None:
            print("x")
            break
        current = current.right

deleteData = "3"
current = root
parent = None

while True:
    if deleteData == current.data:
        if parent == None:
            if current.left == None and current.right == None:
                del(current)
            elif current.left != None and current.right == None:
                root = current.left
                del(current)
            elif current.left == None and current.right != None:
                root = current.right
                del(current)
            else:
                find = current.left
                while find.right != None:
                    find = find.right
                current.data = find.data
                del(find)
            break
        else:
            if current.left == None and current.right == None:
                del(current)
            elif current.left != None and current.right == None:
                if parent.left == current:
                    parent.left = current.left
                else:
                    parent.right = current.right
                    del(current)
            elif current.left == None and current.right != None:
                if parent.left == current:
                    parent.left = current.right
                else:
                    parent.right = current.right
                    del(current)
                parent.right = current.right
            else:
                find = current.left
                while find.right != None:
                    find = find.right
                current.data = find.data
                del(find)
        

            
            
                
