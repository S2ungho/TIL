# ✏️ 메소드 오버라이딩 (method overriding)
* 메소드 오버라이딩은 자식 클래스가 부모 클래스의 메소드를 자신이 필요에 맞춰서 재정의하는 것이다.
* 이때 메소드의 이름이나 매개변수, 반환형은 동일하여야 한다.
> 메소드 오버라이딩 예시
```java
class Shape{
    public void draw(){
        System.out.println("Shape");
    }
}

class Circle extends Shape{
@override
    public void draw(){
        System.out.println("draw Circle");
    }
}

class Rectangle extends Shape{
@override
    public void draw(){
        System.oit.println("draw Rectangle");
    }
}

class Triangle extends Shape{
@override
    public void draw(){
        System.out.println("draw Triangle");
    }
}

public class ShapeTest{
    public static void main(String args[]){
        Rectangle s = Rectangle();
        s.draw()
    }
}
// 출력 결과
// draw Rectangle
```
 ### 메소드 오버라이딩 시 주의할 점
 * 부모 클래스의 메소ㅗ드와 자식 클래스의 메소드가 완벽하게 일치하여야 오버라이딩으로 처리된다. <br> 만약 완벽하게 일치하지 않으면 메소드 오버로딩으로 처리되어 버린다.
 * 오타가 난 경우 컴파일러는 새로운 메소드 이름으로 인식하기 때문에<br>오버라이딩 된 메소드 이름 앞에는 **@Override 어노테이션**을 붙이는 것이 좋다<br>만약 부모 클래스에 그런 이름의 메소드가 없다면 컴파일러가 오류를 발생한다.

 ### 키워드 super를 사용하여 부모 클래스 멤버 접근
 * 키워드 super는 상속 관계에서 부모 클래스의 메소드나 필드를 명시적으로 참조하기 위해 사용된다.
 * 만약 부모 클래스의 메소드를 오버라이딩한 경우에 super를 사용하면 부모 클래스의 메소드를 호출할 수 있다.
 ```java
class Shape{
    public void draw(){
        System.out.println("Shape 중의 하나를 그릴 예정입니다.");
    }
}

class Circle extends Shape{
@Override
    public void draw(){
        super.draw();
        System.out.println("Circle을 그립니다.");
    }
}

public class ShapeTest{
    public static void main(String args[]){
        Circle s = new Circle();
        s.draw();
    }
}
// 출력 결과
// Shape 중의 하나를 그릴 예정입니다.
// Circle 을 그립니다.
 ```
## 오버라이딩과 오버로딩 혼동하지 말기
* 오버로딩 : 같은 메소드명을 가진 여러 개의 메소드를 작성하는 것
* 오버라이딩 : 부모 클래스의 메소드를 자식 클래스가 다시 정의하는 것

>오버로딩은 **컴파일 시간**에서의 다형성을 지원하며<br>메소드 오버라이딩을 하면 **실행 시간**에서의 다형성을 지원할 수 있다.

## 정적 메소드를 오버라이드 하면 어떻게 될까?
* 자식 클래스가 부모 클래스의 정적 메소그와 동일한 정적 메소드를 정의하는 경우, 어떤 참조 변수를 통하여 호출 되는지에 따라 달라진다.
```java
class Animal{
    public static void A(){
        System.out.println("static method in Animal");
    }
}

public class Dog extends Animal{
    public static void A(){
        System.out.println("static method in Dog");
    }
    public static void main(String args[]){
        Dog dog = new Dog();
        Animal a = dog;
        a.A();
        dog.A();
    }
}
// 출력 결과
// static method in Animal
// static method in Dog
```
> Dog 참조 변수를 통하여 정적 메소드를 호출하면 자식 클래스의 정적 메소드가 호출 된다. <br>Animal 참조 변수를 통하여 정적 메소드를 호출하면 부모 클래스의 정적 메소드가 호출된다.