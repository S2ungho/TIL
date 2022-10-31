# TIL_1
# 첫 TIL작성입니다.
> 잘부탁드립니다.
## 자바의 장점
* 바이트코드를 활용한다
* JVM응 사용한다
<br>

## JAVA
```java
public class Main {
    public static void main(String[] args) {
        // 배열 선언
        int[] numbers1 = new int[5];
        // 배열 초기화
        for (int i = 0; i < numbers1.length; i++) {
            numbers1[i] = i;
        }
        // 배열 선언 및 초기화
        int[] numbers2 = {0, 1, 2, 3, 4};
        String[] weeks = {"월", "화", "수", "목", "금", "토", "일"};
        // 배열에 요소 추가
        // numbers2[5] = 5; ArrayIndewOutOfBoundsException 에러발생
        // 새로운 더 큰 배열을 만든다.
        numbers2 = Arrays.copyOf(numbers2, numbers2.length + 1);
        // 배열에 요소 추가
        numbers2[5] = 5;
        // 결과 출력
        System.out.println("배열에 요소 추가: " + Arrays.toString(numbers2));
    }
}
```
