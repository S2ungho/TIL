# ✏️ 우선순위 큐: 힙
* 큐는 먼저 들어간 값이 먼저 나오는 First-in-First-out 구조이다. 하지만 우선순위 큐는 들어간 순서와 상관없이 우선순위가 높은 데이터가 먼저 나온다.
* 컴퓨터 내부에서 동일한 자원을 요구하는 여러 프로그램이 있으면 우선순위를 부여해서 관리한다.<br> 우선순위 큐를 정의하고 우선순위 큐를 구현하는 대표적인 자료구조로 힙이 있다.
* 우선순위를 가진 원소를 삽입할 수 있고, 우선순위가 가장 큰 원소를 빼내줄 수 있으면 **우선순위 큐 (Priority Queue)** 라고 한다.

> ADT 우선순위 큐

    원소를 삽입한다.
    최대 원소를 알려주면서 삭제한다.
    최대 원소를 알려준다.
    우선순위 큐가 비어 있는지 확인한다.
    우선순위 큐를 깨끗이 비운다.
## 📍 힙과 완전이진트리
* 힙은 대표적인 우선순위 큐로, 완전 이진 트리 라는 구조를 사용한다.
* 이진 트리(Binary Tree) : 모든 노드가 2개 이하의 자식을 갖는 트리
  + 포화 이진 트리(Complete Binary Tree) : 루트로부터 시작해 모든 노드가 정확히 자식 노드를 2개씩 가지면서 꽉 채워진 트리 (2^k-1)
  + 완전 이진 트리(Full Binary Tree) : 노드 수가 맞지 않아 포화 이진 트리를 만들 수 없을 때 최대한 포화 이진 트리에 가깝게 만든 것이 완전 이진 트리 이다.
## 📍 힙의 조건
* 힙은 다음의 두 가지 조건을 만족 해야한다.
  + 완전 이진 트리
  + 힙 특성 : 모든 노드는 값을 갖고, 자식 노드(들) 값보다 크거나 같다.
* 최대힙(Max heap) : 위와 같이 자식 노드(들) 값보다 크거나 같다면 최대힙
* 최소힙(Min heap) : 위와 대조 되게 자식 노드(들) 값보다 작거나 
같다면 최소 힙
>배열은 그 자체로 완전 이진 트리로 볼 수 있다
(배열에 저장한다는 사실로 완전 이진 트리 조건(조건 1)은 자동 만족<br>
> 파이썬 내장 리스트도 배열로 간주할 수 있다.<br>
단, 배열은 현재 원소가 총 몇 개인지 사용자가 관리해야 하지만
파이썬 내장 리스트는 파이썬에서 자동 관리해준다
## 📍 힙 작업 알고리즘과 구현
### head의 class 구조
```python
class Heap:
    def __init__(self, list):
        if list = None:
        self.__A = []
    else:
        self.__A = list
```
### 원소 삽입 (insert)
1. 삽입 원소를 리스트의 맨 끝에 추가
2. Heap 특성을 만족하도록 삽입 원소의 위치를 교환(스며올리기)
```python
#힙에 원소 삽입 함수
def insert(self,x): 
    self.__A.append(x)
    self.__percolateUp(len(self.__A)-1)

# 스며오르기
def __percolateUp(self, i:int):
	parent = (i - 1) // 2
	if i > 0 and self.__A[i] > self.__A[parent]:
		self.__A[i], self.__A[parent] = self.__A[parent], self.__A[i]
		self.__percolateUp(parent)
```
### 원소 삭제 (deleteMax)
1. 루트 원소를 리턴
2. 맨끝 원소를 루트로 이동
3. 힙 특성을 만족하도록 스며내리기
```python
# 힙의 원소 삭제 하기
def deleteMax(self):
	# heap is in self.__A[0...len(self.__A)-1]
	if (not self.isEmpty()):
		max = self.__A[0]
		self.__A[0] = self.__A.pop()
		self.__percolateDown(0)
		return max
	else:
		return None

	# 스며내리기
def __percolateDown(self, i:int):
	# Percolate down w/ self.__A[i] as the root
	child = 2 * i + 1  # left child
	right = 2 * i + 2  # right child
	if (child <= len(self.__A)-1):
		if (right <= len(self.__A)-1 and self.__A[child] < self.__A[right]):
			child = right  # index of larger child
		if self.__A[i] < self.__A[child]:
			self.__A[i], self.__A[child] = self.__A[child], self.__A[i]
			self.__percolateDown(child)
```
### 힙 생성하기
```python
	def buildHeap(self):
		for i in range((len(self.__A) - 2) // 2, -1, -1):
			self.__percolateDown(i)
```
### 기타 작업
```python
	def max(self):
		return self.__A[0]

	# 힙이 비었는지 확인하기
	def isEmpty(self) -> bool:
		return len(self.__A) == 0

	def clear(self):
		self.__A = []

	def size(self) -> int:
		return len(self.__A)
```

## 📍 힙 수행 시간
* Heap의 크기가 n일 때 (buildHeap( ))에  Θ(𝑛)의 시간이 소요
* Heap에 원소를 삽입하는 작업(insert( ))은 한 번의 percolateUp( )이 전부이므로 
O(log n), 운이 좋은 경우 한 번의 비교로 끝날 수도 있으므로 Θ(1)
* Heap에서 원소를 삭제하는 작업 (deleteMax())는 A[0]에서 한 번의 percolateDown( )이 전부이므로 O(log n)의 시간이 걸린다.  운이 좋으면 Θ(1)
***
🔺 2022. 11. 02.

