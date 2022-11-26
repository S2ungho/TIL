# ✏️ 이진 트리(Binary Tree)
> 모든 노드의 자식이 최대 2개인 트리 (자식이 2개 이하로 구성)

## 이진 트리의 종류
  + 포화 이진 트리(full binary tree)
  + 완전 이진 트리(complete binary tree)
  + 편향 이진 트리(skewed binary tree)
* 트리 노드 생성 클래스
``` python
class TreeNode():
    def __init__(self):
        self.data=None
        self.left=None
        self.right=None
```

## 이진 트리의 순회
> 이진 트리의 노드 전체를 한 번씩 방문하는 것을 순회(traversal)라고 함
* 노드데이터를 처리하는 순서에따라 전위순회, 중위순회, 후위순회로 나뉜다.
1. 전위 순회 : 루트 -> 왼쪽 -> 오른쪽
``` python
def preorder(node):
    if node==None:
        return
    print(node.data,end='->')
    preorder(node.left)
    preorder(node.right)
```
2. 중위 순회 : 왼쪽 -> 루트 -> 오른쪽
``` python
def inorder(node):
    if node==None:
        return
    inorder(node.left)
    print(node.data,end='->')
    inorder(node.right)
```
3. 후위 순회 : 왼쪽 -> 오른쪽 -> 루트
``` python
def postorder(node):
    if node==None:
        return
    postorder(node.left)
    postorder(node.right)
    print(node.data,end='->')
```
## 이진 탐색 트리

* 이진 탐색 트리 특징
1.  왼쪽 서브 트리는 루트 노드보다 모두 작은 값을 가진다.
2.  오른쪽 서브 트리는 루트 노드보다 모두 큰 값을 가진다.
3.  각 서브 트리도 1, 2 특징을 갖는다.
4.  모든 노드 값은 중복되지 않는다. 즉, 중복된 값은 이진 탐색 트리에 저장할 수 없다.
> 이진 탐색 트리 구성 코드
```python
class TreeNode():
    def __init__(self):
        self.data = None
        self.left = None
        self.right = None

#memory = []
root = None
nameAry = ['블랙핑크','레드벨벳','마마무','에이핑크','걸스데이','트와이스']
node = TreeNode()
node.data = nameAry[0]
root = node
# memory.append(node)
for name in nameAry[1:]:
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
        #memory.append(node)
```
***
🔺 2022. 11. 06.
## 이진 탐색 트리에서 데이터 검색

## 이진 탐색 트리에서 데이터 삭제