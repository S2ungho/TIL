# ✏️ 인터페이스 (Interface)
    여러 프로그래머들이 독립적으로 클래스를 작성하고, 이 클래스들을 합쳐서 하나의 소프트웨어를 완성하는 상황을 가정했을 때, 각자 클래스를 다른 사람의 클래스와 연결하려면 클래스 간의 상호작용을 기술하는 일종의 규격이 있어야하는데 이 규격을 인터페이스(Interface)로 정의할 수 있다.
* 인터페이스는 상속 관계가 아닌, 클래스 간의 유사성을 인코딩하는 데 사용된다.
> Ex) 예를 들어, 사람(Human)과 자동차(Car)는 둘 다 달릴 수 있다. 그렇다고 부모 클래스로 Runner를 작성하고, Human과 Car를 Runner 클래스의 자식 클래스로 나타내는 것은 약간 이치에 맞지 않는다.
<br>이런 경우에 Runnable 인터페이스를 만들고 이 인터페이스를 양쪽 클래스가 구현하게 하면 된다
* 인터페이스 정의

```java
public interface 인터페이스_이름 {
    반환형  추상메소드1(...);
    반환형  추상메소드2(...);
    ...
}
```
* 인터페이스 예시
```java
public interface RemoteControl{
    //추상 메소드 정의
    public void turnOn();
    public void turnOff();
    // 인터페이스 안에서 언언되는 메소드들은 모두 묵시적으로 public abstract이다.
}
```
## 인터페이스 구현
* 인터페이스 만으로는 객체를 생성할 수 없다. (컴파일 에러) <br>인터페이스 안에는 구현되지 않은 메소드가 존재하기 때문이다.
* 인터페이스는 다른 클래스에 의하여 구현(implement)될 수 있다. 인터페이스를 구현한다는 말은 인터페이스에 정의된 추상 메소드의 몸체를 정의한다는 의미이다.
* 클래스가 인터페이스를 구현하기 위해서는 implement 키워드를 사용한다.
```java
class Television implements RemoteControl{
    boolean on;
    public void turnOn(){
        on = true;
        System.out.println("TV On");
    }
    public void turnOff(){
        on = false;
        System.out.println("TV Off");
    }
}
```
```java
Television t = new Television();
t.turnOn();
t.turnOff();
```
***
🔺 2022. 11. 08.

# ✏️ 인터페이스를 이용한 다중 상속
* 다중상속(Multiple inheritance) : 하나의 클래스가 여러 개의 부모 클래스를 가지는 것
1. 여러개의 인터페이스를 동시에 구현
```java
interface Drivable{ void drive(); }
interface Flyable{ void fly(); }

public class FlyingCar1 implements Drivable, Flyable{
    @Override
    public void drive() {
        System.out.println("driving");
    }
    @Override
    public void fly() {
        System.out.println("flying");
    }
    public static void main(String args[]){
        FlyingCar1 obj = new FlyingCar1();
        obj.drive();
        obj.fly();
    }
}

```

2. 하나의 클래스를 상속받고 또 하나의 인터페이스를 구현
```java
interface Flyable{ void fly(); }
class Car{
    int speed;
    void setSpeed(int speed){ this.speed = speed; }
}
public class FlyingCar1 extends Car implements Flyable{
    @Override
    public void fly() {
        System.out.println("flying");
    }
    public static void main(String args[]){
        FlyingCar1 obj = new FlyingCar1();
        obj.setSpeed(100);
        obj.fly();
    }
}
```
## 상수 정의
* 인터페이스에 상수는 정의할 수 있다. 인터페이스에서 정의된 변수는 자동적으로 public static final 이 되어 상수가 된다.

* 인터페이스 및 다중상속 예제
```java
/** * A short description of the program.
 * author Seungho HAM
 * SID 60191982
 * assignment java - lab8
 * @date 2022.11.15
 * + construct
 */
interface Area{
    void getArea();
}
interface Movable{
    void move(int dx, int dy);
}
class Shape implements Movable, Area{
    int x, y;
    public void move(int dx, int dy){
        x = dx;
        y = dy;
    }
    public void getArea(){
        System.out.println(x + " " + y);
    }
}
class Rectangle extends Shape{
    int weight, height;
    public Rectangle(){}
    public Rectangle(int w, int h){
        weight = w;
        height = h;
    }
    public void getArea(){
        System.out.println("Rectangle\t: " + (weight + x) * (height + y) );
    }
}
class Triangle extends Shape{
    int base, height;
    public Triangle(){}
    public Triangle(int b, int h){
        base = b;
        height = h;
    }
    public void getArea(){
        System.out.println("Triangle\t: " + (base + x) * (height + y) / 2 );
    }
}
class Circle extends Shape{
    int radius;
    public Circle(){}
    public Circle(int r){
        radius = r;
    }
    public void getArea(){
        System.out.println("Circle\t\t: " + 3.14 * (radius + x + y) * (radius + x + y));
    }
}

public class ShapeTest {
    public static void main(String args[]) {
        Shape[] arrayOfShapes;
        arrayOfShapes = new Shape[3];
        arrayOfShapes[0] = new Rectangle(2,2);
        arrayOfShapes[1] = new Triangle(3,3);
        arrayOfShapes[2] = new Circle(5);
        for(int i = 0;i < 3;i++){
            arrayOfShapes[i].move(10,10);
            arrayOfShapes[i].getArea();
        }
    }
}
```

***
🔺 2022. 11. 16.