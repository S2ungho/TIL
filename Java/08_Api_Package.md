# ✏️ 자바 API 패키지
    자바가 제공하는 패키지들은 자바의 API 문서에 나열되어 있다.
    자바의 기본 패키지는 java로 시작하며 확장 패키지는 javax로 시작한다.
## 📍Object 클래스
* Object 클래스는 java.lang 패키지에 들어 있으며 자바 클래스 계층 구조에서 맨 위에 위치하는 클래스
* Object 의 메소드
  + **public boolean equal(Object obj)** : obj가 이 객체와 같은지를 검사한다.
  + **public String toString()** : 객체의 문자열 표현을 반환한다.
  + **protected Object clone()** : 객체 자신의 복사본을 생성하여 반환한다.
  + **public int hashCode()** : 객체에 대한 해쉬코드를 반환한다.
  + **protected void finalize()** : 가비지 콜렉터에 의하여 호툴된다.
  + **public final Class getClass()** : 객체의 클래스 정보를 반환한다.

### getClass() 메소드
> getClass()는 객체가 어떤 클래스로 생성되었는지에 대한 정보를 반환한다.
```java
class Circle{ }

public class CircleTest {
    public static void main(String[] args){
        Circle obj = new Circle();
        System.out.println("obj is of type : " + obj.getClass().getName());
        System.out.println("obj의 해쉬 코드 : " + obj.hashCode());
    }
}
```

### toString() 메소드
> Object 클래스의 toString() 메소드를 객체의 상태를 몇 줄의 문자열로 요약하여 반환하는 함수이다. <br>우리가 println()을 사용하여 객체를 출력하면 객체의 toString() 메소드가 자동으로 호출된다.
```java
class Circle{
    int radius;
    public Circle(int radius){ this.radius = radius; }
    public String toString(){ return "Circle(r="+radius+")"; }
}

public class CircleTest {
    public static void main(String[] args){
        Circle obj = new Circle(10);
        System.out.println(obj);
    }
}
```
### equals() 메소드
> 두개의 A 객체가 동일한 값을 가진지 검사하기 위해서는 equals()를 재정의하고 equals()을 호출하여야한다.
```java
class Circle{
    int radius;
    public Circle(int radius){ this.radius = radius; }
}

public class CircleTest {
    public static void main(String[] args){
        Circle obj1 = new Circle(10);
        Circle obj2 = new Circle(10);
        if(obj1 == obj2) System.out.println("2개의 원은 같습니다.");
        else System.out.println("2개의 원은 같지 않습니다."); // 같지 않다는 문구 출력
    }
}
```
* **== 연산자는 참조 값을 비교하고, .equals() 는 내용을 비교한다.**
```java
class Circle{
    int radius;
    public Circle(int radius){ this.radius = radius; }
    public boolean equals(Circle c1) {
        if (radius == c1.radius) return true;
        else return false;
    }
}

public class CircleTest {
    public static void main(String[] args){
        Circle obj1 = new Circle(10);
        Circle obj2 = new Circle(10);
        if(obj1.equals(obj2)) System.out.println("2개의 원은 같습니다.");
        else System.out.println("2개의 원은 같지 않습니다."); // 같지 않다는 문구 출력

        
    }
}
```

### finalize() 메소드
* Object 클래스는 finalize() 라는 콜백 메소드를 정의한다. 이것은 객체가 소멸되기 직전에 호출된다. Object 클래스의 finalize()에서는 아무 것도 하지 않지만 자식 클래스에서 재정의하여서 자원을 반납하는 등의 정리 과정을 실행할 수 있다.

## 📍 랩퍼 클래스(Wrqpper Class)
    정수와 같은 기초 자료형도 객체로 포장하고 싶은 경우가 있다. 이때 사용되는 클래스가 랩퍼클래스 이다.


```java
int i = 100
Integer obj = new Integer(i);
```
```java
// 랩퍼 객체 안에 포장된 정수 100을 꺼내려면 intValue() 함수를 사용
Integer obj = new Integer(100);
int value = obj.intValue(); // value는 정수 100
```
```java
//정수 100을 문자열로 변환하고 싶다면 Integer 클래스의 toString() 메소드 이용
String s = Integer.toString(100); // s는 "100"
```
```java
//문자열 "100"을 정수 100으로 변환하려면 Integer 클래스의 parseInt() 메소드를 사용한다.
int i = Integer.parseInt("100");
```

### 오토박싱(auto-boxxing)
    자바는 랩퍼 객체와 기초 자료형 사이의 변환을 자동으로 해주는 기능이 있는데 이것을 오토박싱 이라고 한다.

```java
Integer obj;

obj = 10; // 정수  ->  integer 객체
System.out.println(obj + 1); // integer 객체  ->  정수
// int형 정수는 Integer 객체로 자동으로 변환된다, 그리고 Integer 객체는 자동으로 int형 정수로 변환된다.
```

## 📍String 클래스
    String 클래스는 문자열을 구성하는 문자들을 내부에 저장한다.

### 객체 생성
> 자바에서 객체를 생성하는 유일한 방법은 new를 사용하는 것이다. <br>하지만 문자열은 프로그래밍에서 아주 많이 사용되기 때문에 다음과 같이 2가지 방법으로 String 객체를 생성할 수 있고 의미가 약간 다른다.
```java
String s1 = "Java"; // 많이 사용되는 방법
String s2 = "Java";
String s3 = new String("Java"); // 원칙
String s4 = new String("Java");
```
* 위와 같이 new를 사용해서 String 객체를 생성하면 문자열이 동일하다고 하여도 새로운 객체를 생성한다.<br>하지만 1,2번째 줄과 같이 문자열 상수로 초기화하면, 문자열 상수 풀을 조사해서 동일한 문자열을 가진 객체가 존재하면 이것을 공유한다.
* 결과적으로 s3,s4는 별도의 객체를 가리키지만 s1,s2는 문자열 상수 풀에 있는 동일한 객체를 가리키게 된다.

### 문자열의 기초 연산
String 의 length() 메소드는 문자열의 길이를 반환한다.
```java
String s = "Hello world!"; // 객체 생성
int size = s.length(); // 12가 반환됨
```
* String 객체 안에 들어 있는 문자를 추출 하려면 charAt()이라는 메소드를 호출하면 된다. ( 문자 번호는 0부터 시작한다. )
```java
String s = "Hello world!"; // 객체 생성
char c = s.charAt(0); // 'H'가 반환된다.
```
* 자바에서 2개의 문자열을 붙이려면 물론 comcat()라는 메소드를 호출해도 되지만 + 연산자를 사용하는 것이 더 편리하다.
```java
String result = "A chain" + " is only as strong" + " as its weakest link";
```

### 문자열 비교하기
    2개의 문자열이 동일한지 검사하려면 equals()을 호출하여야한다.
    == 연산자를 사용하는 것이 아니다.
```java
String s1 = "Java"; // 많이 사용되는 방법
String s2 = "Java";
String s3 = new String("Java"); // 원칙
String s4 = new String("Java");

System.out.prinln(s1.equals(s2)); // true 올바른 방법
System.out.prinln(s1.equals(s3)); // true 올바른 방법
System.out.prinln(s1 == s2); // true 이지만 올바르지 않은 방법
System.out.prinln(s1 == s3); // false 이며 올바르지 않은 방법
```

### 문자열 안에서 단어 찾기
    문자열에서 단어를 찾을 때는 indexOf()를 사용하는 것이 가장 쉽다.
    단어의 시작 위치가 반환된다.
```java
String s = "The cat is on the table";
int index = s.indexOf("table");

if(index == -1){
  System.out.println("table은 없습니다.");
}
else{
  System.out.println("table의 위치 : " + index);
}
// table 위치는 18이라고 출력된다.
```
### 문자열을 단어로 분리할 때
    String 클래스가 제공하는 Split() 메소드를 사용하면 훨씬 쉽게 문자열을 단어로 분리할 수 있다.
```java
String[] tokens = "I am a boy.".split(" ");
for(String token : tokens){
  System.out.println(token);
}
// I, am, a, boy 출력
```

### StringBuffer 클래스
    String 클래스의 경우, 빈번하게 문자열을 변경할 때는 비효율적일 수 있다.
    왜냐하면 문자열의 내용을 변경하는 String 클래스 메소드릐 경우, 새로운 String 객체를 생성하고 기존의 내용을 복사해야 하기 때문이다.

* 따라서 자바는 변경 가능한 문자열을 위하여 String 클래스의 대안으로 StringBuffer 클래스를 제공한다.
```java
StringBuffer s = new StringBuffer("Happiness depends upon ourselves");
```
* StringBuffer만이 제공하는 가장 중요한 메소드는 append()와 insert()이다. 이 두 메소드를 어떤 타입의 데이터도 받을 수 있도록 중복 정의되어 있다.

## 📍 Math 클래스
    Math 클래스는 지수나 로그, 제곱근, 삼각함수와 같은 기본적인 수치 연산을 위한 메소드들을 제공한다.
```java
public class MathTest{
  public static void main(String[] args){
    double x = Math.PI;
    System.out.println(Math.sin(x));
    System.out.println(Math.random());
  }
}
```

## 📍 Random 클래스
    Random 클래스의 객체는 난수를 발생하는 데 사용된다.
```java
import java.util.*;
public class RandomTest{
  public static void main(String[] args){
    Random random = new Random();
    for ( int i = 0; i < 10; i++){
      System.out.print(random.nextInt(100)+",");
    }
  }
}
```

## 📍 Array 클래스
```java
import java.util.*;

public class ArrayTest {
    public static void main(String[] args){
        int[] array = { 9,4,5,6,2,1};
        Arrays.sort(array); // 배열 정렬
        printArray(array);
        System.out.println(Arrays.binarySearch(array,9)); // 9를 탐색
        Arrays.fill(array,8); // 배열을 특정한 값으로 채움
        printArray(array);
    }
    private static void printArray(int[] array){
        System.out.print("[");
        for(int i = 0; i < array.length; i++){
            System.out.print(array[i]+" ");
        }
        System.out.println("]");
    }
}
//[1 2 4 5 6 9 ]
//5
//[8 8 8 8 8 8 ]
```