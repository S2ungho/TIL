# ✏️ 선택 정렬 (selection Sort)
    단위 순환 
      최대 원소를 찾는다
      최대 원소와 맨 오른쪽 원소를 자리 바꾼다
      맨 오른쪽 자리를 관심 대상에서 제외한다
    원소가 1 개 남을 때까지 위의 순환을 반복
```python
def selectionSort(A):
	for last in range(len(A)-1, 0, -1):
		k = theLargest(A, last)	# A[0...last] 중 가장 큰 수 A[k] 찾기
		A[k], A[last] =  A[last], A[k]

def theLargest(A, last:int) -> int:	# A[0...last]에서 가장 큰 수의 인덱스를 리턴한다
	largest = 0
	for i in range(last+1):
		if A[i] > A[largest]:
			largest = i
	return largest
```
# ✏️ 버블 정렬
    단위 순환
		맨 앞부터 한 칸씩 이동하면서, 
             두 원소가 순서대로 되어 있지 않으면 자리 바꾼다
		맨 오른쪽 자리를 관심 대상에서 제외한다
	원소가 1 개 남을 때까지 위의 순환을 반복
```python
def bubbleSort(A):
	for numElements in range(len(A), 0, -1):
		for i in range(numElements-1):
			if A[i] > A[i+1]:
				A[i], A[i+1] = A[i+1], A[i]
```
# ✏️ 삽입 정렬
```python
def insertionSort(A):
	for i in range(1, len(A)):
		loc = i-1
		newItem = A[i]
		while loc >= 0 and newItem < A[loc]:
			A[loc+1] = A[loc]
			loc -= 1
		A[loc+1] = newItem
```