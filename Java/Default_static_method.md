# ✏️ 디폴트 메소드 (Defaul Method)
    디폴트 메소드는 인터페이스 개발자가 메소드의 디폴트 구현을 제공할 수 있는 기능이다.
    디폴트 메소드가 정의되어 있으면 인터페이스를 구현하는 클래스가 메소드의 몸체를 구현하지 않아도 메소드를 호출할 수 있다.
```java
interface Myinterface{
    public void myMethod1();

    default void myMethod2(){
        System.out.println("myMethod");
    }
}

public class DefaultMethodTest implements Myinterface{
    public void myMethod1(){
        System.out.println("Mymethod1()");
    }

    public static void main(String args[]){
        Myclass obj = new Myclass();
        obj.myMethod1();
        obj.myMethod2();
    }
}
```
* myMethod1과 2 모두 에러가 나지 않고 출력이 되며 몸체에서 구성하지 않은 2 메소드도 인터페이스 디폴트 메소드를 불러와 출력한다.

# ✏️ 정적 메소드 (Static Method)
    정적 메소드는 용어의 정의 그대로 클래스의 객체에 들어 있는 것이 아니라 클래스에 들어있다.
    정적 메소드를 인터페이스에 추가하려면 메소드 이름 앞에 static 키워드를 붙이면 된다.
```java
interface MyInterface{
    static void print(String msg){
        System.out.println(msg + ": interface");
    }
}

public class StaticMethodTest{
    public static void main(String[] args){
        MyInterface.print("JAVA 8");
    }
}
```
* 객체 생성하지 않고 바로 접근할 수 있다.