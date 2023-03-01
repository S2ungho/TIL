# ✏️ 제네릭(Generic)
    제네릭 프로그래밍(generic programming)은 다양한 종류의 데이터를 처리할 수 있는 클래스와 메소드를 작성하는 기법이다.

## 기존의 방법
  + 일반적인 객체를 처리하려면 Object 참조 변수를 사용
  + Object 참조 변수는 어떤 객체이던지 참조할 수 있다.
```java
import java.lang.*;

public class Box {
    private Object data;

    public void set(Object data) {
        this.data = data;
    }

    public Object get() {
        return data;
    }

    public static void main(String[] args){
        Box b = new Box();

        b.set("Hello"); // 문자열 객체를 저장
        String s = (String)b.get(); //Object 타입을 String 타입으로 형변환
        System.out.println(b);

        b.set(new Integer(10)); //정수 객체를 저장
        Integer i = (Integer)b.get(); // Object 타입을 Integer 타입으로 형변환
        System.out.println(i);
    }
}
//Box@2f92e0f4
//10
// 위와 같은 값 출력
```
## 제네릭을 이용한 방법
```java
public class Box<T> {
    private T data;
    public void set(T data){ this.data = data; }
    public T get(){ return data; }
    public static void main(String[] args){
        Box<String> b = new Box<String>();
        b.set("Hello");
        String s = b.get();
        System.out.println(s);
    }
}
```

## 📍 제네릭 메소드(Generic Method)
    일반 클래스의 메소드에서도 타입 매개 변수를 사용하여 제네릭 메소드를 정의할 수 있다.
    이 경우에는 타입 매개 변수의 범위가 메소드 내부로 제한된다.
```java
class MyArrayAlg{
    public static <T> T getLast(T[] a){
        return a[a.length - 1];
    }
}
public class MyArrayTest{
    public static void main(String[] args){
        String[] language = {"C","A","B"};
        String last = MyArrayAlg.getLast(language);
        System.out.println(last);
    }
}
//B 출력
```

> ex) 정수 배열, 실수 배열, 문자 배열을 모두 출력할 수 있는 제네릭 메소드 printArray()를 작성해보기
```java
public class GenericMethodTest {
    public static <T> void printArray(T[] array) {
        for (T element : array) {
            System.out.printf("%s ", element);
        }
        System.out.println();
    }

    public static void main(String args[]) {
        Integer[] iArray = {10, 20, 30, 40, 50};
        Double[] dArray = {1.1, 1.2, 1.3, 1.4, 1.5};
        Character[] cArray = {'S', 'E', 'U', 'N', 'G'};

        printArray(iArray);
        printArray(dArray);
        printArray(cArray);
    }
}
```
***
🔺 2022. 11. 24.