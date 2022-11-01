# 상속 (Inheritance)
>상속은 기존에 존재하는 클래스로부터 필드와 메소드를 이어받고, 필요한 기능을 추가할 수 있는 기법이다.
## 상속의 형식
* 자바에서는 extends 키워드를 이용하여 상속을 나타낸다.
```java
class ElectricCar extends Car{
    int batteryLevel;
    public void charge(int amount){
        batteryLevel += amount;
    }
}
```
* 자식클래스 또는 서브클래스 **ElectricCar** 는 부모클래스 또는 슈퍼클래스인 **Car** 가 가지고 있는 모든 멤버들을 전부 상속받고 <br>자신이 필요한 멤버를 추가하기 때문에 항상 자식 클래스가 부모클래스를 포함하게 된다.
## 왜 상속을 사용하는가?
* 만약 우리가 원하는 코드를 가진 클래스가 이미 존재한다면 이 클래스를 상속받아서 이미 존재하는 클래스의 필드와 메소드를 재사용할 수 있다.
* 상속을 사용하면 중복되는 코드를 줄일 수 있다.
## 자바 상속의 특징
* 다중 상속을 지원하지 않는다.<br> 다중 상속이란 여러 개의 클래스로부터 상속받는 것이다. **자바에서는 금지되어있다.**
* 상속의 횟수에는 제한이 없다.
* 상속 계층 구조의 최상위에는 **java.lang.Object 클래스**가 있다.
## 상속 - 접근 지정자
* 자식 클래스는 부모 클래스의 **public 멤버, protected 멤버, 디폴트 멤버**(부모 클래스와 자식 클래스가 같은 패키지에 있다면)를 상속 받는다. <br> 하지만 부모클래스의 **private 멤버**는 상속되지 않는다.
> protected 예시
```java
class Shape{
    protected int x, y; // x와 y는 protected로 선언되었기 때문에 Shape 와 Rectangle에서만 사용가능, 외부 클래스 접근 불가
    void print(){
        System.out.println("x : " + x + " y : " + y);
    }
}

public class Rectangle extends Shape{
    int width, height;

    double calcArea(){
        return width * height;
    }
    void draw(){
        System.out.println("(" + x + "," + y + ") width : " + width + "height" + height);
    }
}
```

> private 예시
```java
class Person{
    private String regnumber; // 자식 클래스 접근불가
    private double weight; // 자식 클래스 접근불가
    protected int age; // 자식 클래스 접근가능
    String name // 어디서나 접근가능

    public double getWeight(){
        return weight;
    }
    public void setWeight(double weight){
        this.weight = weight;
    }
}

class Student extends Person{
    int id;
}

public class StudentTest{
    public static void main(String args[]){
        Student obj = new Student();
        //obj.regnumber = "123-123"; // error
        //obj.weight = 75.0; // error
        obj.age = 21;
        obj.name = "Kim";
        obj.setWeight(75.0);
    }
}
```
## 상속 - 생성자
* 자식 클래스의 객체 안에는 부모 클래스에서 상속된 부분이 들어있다. <br> 따라서 자식 클래스 안의 **부모 클래스 부분을 초기화하기 위하여 부모 클래스의 생성자도 호출되는 것**이다.
> 부모 클래스의 생성자도 호출 됨을 보여주는 예시
```java
class Base{
    public Base(){
        System.out.println("Base() 생성자");
    }
}
class Derived extends Base{
    public Derived(){
        System.out.println("Derived() 생성자");
    }
}
public class Test{
    public static void main(String args[]){
        Derived r = new Derived();
    }
}
// 출력 결과
// Base() 생성자
// Derived() 생성자
```
* 생성자의 호출 순서는 [부모 클래스의 생성자] -> [자식 클래스의 생성자] 순으로 된다는 것을 알 수 있다.
### 명시적인 호출 ( super( ) )
> 자식 클래스의 생성자에서 명시적으로 부모 클래스의 생성자를 호출할 수 있음. 이 때 super라는 키워드를 사용
```java
class Base{
    public Base(){
        System.out.println("Base() 생성자");
    }
}
class Derived extends Base{
    public Derived(){
        super(); // But 없어도 컴파일러는 부모 클래스의 기본 생성자가 자동으로 호출 되도록 함. (묵시적인 호출)
        System.out.println("Derived() 생성자");
    }
}
```
* 오류가 발생하는 경우
    + 묵시적인 부모 클래스 생성자 호출을 사용하려면 부모 클래스에 기본 생성자(매개변수가 없는 생성자)가 반드시 정의되어 있어야한다.
    + 생성자의 매개변수에 맞게 super()에 인수 값을 넣어줘야한다.
    + super()의 인수의 형태에 따라 적절한 생성자가 선택된다.
# 메소드 오버라이딩 (method overriding)
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

