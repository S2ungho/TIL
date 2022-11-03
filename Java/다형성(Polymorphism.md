# ✏️ 다형성(Polymorphism)
>다형성이란 많은(Poly)+모양(morph)이라는 의미로써 주로 프로그래밍 언어에서 하나의 식별자로 여러 개의 작업을 처리하는 것을 말한다.

## 업캐스팅
* 부모 클래스 변수로 자식 클래스 객체를 참조할 수 있다.<br>이것을 업캐스팅(upcasting, 상형 형변환)이라고 한다.
```java
class Shape{
    protected int x,y;
    public void draw(){ System.out.println("Shape draw"); }
}

class Rectangle extends Shape{
    private int width, height;
    public void draw(){ System.out.println("Rectangle draw") }
}

class Triangle extends Shape{
    private int base, height;
    public void draw(){ System.out.println("Triangle draw") }
}

class Circle extends Shape{
    private int radius;
    public void draw(){ System.out.println("Circle draw") }
}

public class ShapeTest{
    public static void main(String args[]){
        Shape s1, s2;
        s1 = new Shape();
        s2 = new Tectangle(); // Rextangle객제를 Shape변수로 가리키기(가능)
    }
}
```
* 위와 같은 문장은 자식 클래스 객체는 부모 클래스 객체를 포함하고 있기 때문에 적법하지만, 부모 클래스 변수로 자식 클래스의 객체를 참조했을 경우에 자식 클래스의 모든 필드와 메소드를 사용할 수 없다.<br>즉, 자식 클래스 중에서 부모 클래스로부터 상속받을 부분만을 사용할 수 있고 나머지는 사용할 수 없다.
* 중요한 것은 자식, 부모의 멤버 중 어떤 멤버를 사용할 수 있느냐는 변수의 타입에 의하여 결정된다는 것이다.
## 업캐스팅 vs 다운캐스팅
* 업캐스팅(Upcasting) : 자식 객체를 부모 참조 변수조 참조하는 것이다. 업캐스팅은 묵시적으로 수행될 수 있다. 업캐스팅을 사용하면 부모 클래스의 멤버에 접근할 수 있다. 하지만 자식 클래스의 멤버는 접근이 불가능하다.
* 다운캐스팅(Downcasting) : 부모 객체를 자식 참조 변수로 참조하는 것이다. 이것은 묵시적으로는 안되고 명시적으로 하여야한다.
```java
class Parent{
    void print(){ System.out.println("Parent 메소드 호출"); }
}

class Child extends Parent{
    @Override void print(){ System.out.println("child 메소드 호출"); }
}

public class Casting{
    public static void main(String arg[]){
        Parent p = new Child();
        p.print();

        Child c = (Child)p;
        c.print();
    }
}
```
## 동적 바인딩(dynamic binding)
* 자바 가상머신 JVM은 실행 단계에서 변수가 참조하는 객체의 실제 타입을 보고 적절한 메소드를 호출하게 된다. 이것을 동적 바인딩 이라고 한다.
* 오버라이드된 메소드 호출이 컴파일 시간이 나닌 실행 시간에 결정되는 메커니즘을 의미한다.
* 오버라이드된 메소드가 부모 클래스 참조를 통하여 호출되는 경우에 객체의 타입에 따라서 서로 다른 메소드가 호출되게 하는 메커니즘이다.<br>즉, 객체의 실제 타입이 호출되는 메소드를 결정하는 것이다.
> "부모 참조 변수를 가지고 자식 객체를 참조하는 것은 어디에 쓰이나요?"
* 여러가지 타입의 객체를 하나의 자료 구조 안에 모아서 처리하려는 경우에 필요하다.
### 동적 바인딩의 장점
> ㅁ

***
🔺 2022. 11. 03.