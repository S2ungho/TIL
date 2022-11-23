# ✏️ 중첩 클래스
```java
// 중첩 클래스의 정의
class OuterClass{
    ...
    class NestedClass{
        ...
    }
}
```
* 중첩 클래스
  + 정적 중첩 클래스 : 앞에 static이 붙어서 내장되는 클래스
  + 비정적 중첩 클래스 : 앞에 static이 붙지 않은 일반적인 중첩 클래스
    + 내부 클래스(inner class) : 클래스의 멤버처럼 선언되는 중첩 클래스
    + 지역 클래스(local class) :  메소드의 몸체 안에서 선언되는 중첩 클래스
    + 익명 클래스(anonymouse class) : 수식의 중간에서 선언되고 바로 객체화 되는 클래스

    ## 내부 클래스 (가장 많이 사용되는 클래스)
    * 클래스 안에 클래스를 선언하는 경우이다.
    * 내부 클래스의 접근 지정자는 public, private, protected 또는 package(default) 일 수 있다.
    * 내부 클래스는 외부 클래스의 인스턴스 변수와 메소드를 전부 사용할 수 있다.
    * private로 선언되어 있어도 접근이 가능하다. (내부 클래스의 최대 장점)
```java
class OuterClass{
    private int value = 10;

    class InnerClass{
        public void myMethod(){
            System.out.println("외부 클래스의 프라이빗 변수 값: " + value);
        }
    }

    OuterClass(){
        InnerClass obj = new InnerClass();
        obj.myMethod();
    }
}

public class InnerClassTest{
    public static void main(String[] args){
        OuterClass outer = new OuterClass();
    }
}
```
* 외부 클래스의 생성자에서 내부 클래스의 객체를 생성하였다. (그냥 내부 클래스 이름 그대로 사용하면 된다.)
* 만약 외부 클래스의 바깥에서 내부 클래스의 객체를 생성하려면 다음과 같이 약간 생소한 문법을 사용하여야한다.
* 내부 클래스의 객체는 외부 클래스의 객체가 먼저 생성되어 있어야 생성할 수 있다.
```java
...
OuterClass outer = new OuterClass(); // 외부 클래스 객체가 먼저 생성되어 있어야
OuterClass.InnerClass inner = outer.new InnerClass(); //outer 객체 안에 정의된 InnerClass 라는 의미
...
```

# ✏️ 지역 클래스(Local Class)
* 지역 클래스는 메소드 안에 정의되는 클래스이다.
* 이 메소드를 접근 제어 지정자를 가질 수 없다.
* 지역 클래스는 abstract 또는 final로만 지정할 수 있다.
```java
class localInner{
    private int data = 30;

    void display(){
        final String msg = "current data : ";

        class Local{
            void printMSG(){
                System.out.println(msg + data);
            }
        }
        Local obj = new Local();
        obj.printMSG();
    }
}
public class localInnerTest{
    public static void main(String args[]){
        localInner obj = new localInner();
        obj.display();
    }
}
```
* 지역 클래스는 외부 클래스의 인스턴스 변수뿐만 아니라 메소드의 지역 변수에도 접근할 수 있다. 하지만 지역 변수는 반드시 final로 선언 되어야 한다. ( 지역 클래스 인스턴스가 메소드 호출보다 더 오랜 기간 동안 존재할 수도 있기 때문이다.)

## 중첩 클래스를 사용하는 이유
* 내부 클래스는 외부 클래스의 private 멤버도 접근할 수 있다.
* 외부에서 보이지 않는다.
* 익명 클래스는 콜백 메소드를 작성할 때 아주 편리하다.

# ✏️ 익명 클래스(Anonymous Class)
* 클래스 몸체는 정의되지만 이름이 없는 클래스이다.
* 클래스를 정의하면서 동시에 객체를 생성하게 된다.
* 이름이 없기 때문에 한번만 사용이 가능하다.
* 코드의 양을 줄일 수 있는 장점도 있지만 반먼에 표기법이 상당히 난해하다.
* 하나의 객체만 생성하면 되는 경우에 많이 사용한다.
```java
부모클래스 참조변수 = new 부모클래스(){
    ... // 클래스 구현
}
```
* 이름이 있는 클래스와 익명의 클래스 비교
  + 이름이 있는 클래스
  ``` java
  class Car extends Vehicle{
    ...
  }
  Car obj = new Car();
  ```
  + 익명 클래스
  ```java
  Vehicle obj = new Vehicle(){ ... };
  ```
```java
interface RemoteControl{
    void turnOn();
    void turnOff();
}

public class AnonymousClassTest {
    public static void main(String args[]){
        RemoteControl ac = new RemoteControl(){
            public void turnOn(){
                System.out.println("Tv on");
            }
            public void turnOff(){
                System.out.println("Tv Off");
            }
        };
        ac.turnOn();
        ac.turnOff();
    }
}
```
* 익명의 클래스도 내부 클래스와 같이 필드와 다른 메소드들을 정의할 수 있다.<br>하지만 메소드 안에 정의 되는 지역 변수 중에서는 final로 선언된 변수만 사용이 가능하다.
***
🔺 2022. 11. 16.