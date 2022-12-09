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
        else:
            if current.right == None:
                current.right = node
                break
            current = current.right
        