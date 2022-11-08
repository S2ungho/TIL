# ✏️ 추상 클래스 (Abstract Class)
* 추상 클래스는 완전하게 구현되어 있지 않은 메소드를 가지고 있는 클래스를 의미한다. 
* 메소드가 미완성되어 있으므로 추상 클래스로는 객체를 생성할 수 없다.
* 추상 클래스는 주로 상속 계층에서 추상적인 개념을 나타내기 위한 용도로 사용된다.

> 자바의 다형성 부분에서 했던 Bicycle 클래스를 추상 클래스로 변경한다면 아래와 같다.
```java
abstract public class Bicycle{ //클래스를 추상 클래스로 변경
    protected int gear;
    protected  int speed;

    Bicycle(){ // 추상 메소드가 아닌 보통의 메소드도 가질 수 있음을 유의
    }

    Bicycle(int gear, int speed){
        this.gear = gear;
        this.speed = speed;
    }

    abstract public void SpeedUp(int a); // 속도 상향, 하향 추상 메소드 구현
    //(int a){
        //speed += a;
    //}
    abstract public void SpeedDown(int a);//(int a){
        //speed -= a;
    //}
    public void GearUp(int a){
        gear += a;
    }
    public void GearDown(int a){
        gear -= a;
    }
    public void setSpeed(int speed){
        if (speed < 0)
            this.speed = 0;
        else
            this.speed = speed;
    }
    public void print(){
        System.out.println(this.speed);
    }
}
```

* 추상 클래스 (Bicycle) 라고 하더라도 추상 메소드가 아닌 보통의 메소드도 가질 수 있음을 유의하여야 한다.
* 추상 메소드 (속도 상향, 하향 메소드) 를 하나라도 가지면 추상 클래스가 된다. (추상 메소드가 있지만 추상 클래스로 바꾸지 않으면 에러 발생)
* 상속된 자식 메소드 에서 부모 메소드에서 선언한 추상 메소드를 구현해주지 않으면 컴파일 에러 발생
* 추상 클래스로 객체를 생성할 수 없다.

```java
abstract class Shape{ //추상 클래스 ( 객체 생성 불가 )
    int x, y;
    public void translate(int x, int y){
        this.x = x;
        this.y = y;
    }
    public abstract void draw(); //추상 메소드
}

class Rectangle extends Shape{
    int width, height;
    public void draw(){ System.out.println("rectangle draw"); } // 자식 메소드 에서 부모 메소드에서 선언한 추상 메소드를 구현해주지 않으면 컴파일 에러 발생
}

class Circle extends Shape{
    int radius;
    public void draw(){ System.out.println("circle draw"); }
}

public class AbstractTest {
    public static void main(String args[]){
        //Shape s1 = new Shape();
        Shape s2 = new Circle();
        s2.draw();
    }

}
```

## 추상 클래스의 용도
* 추상 메소드로 정의되면(draw메소드) 자식 클래스에서 반드시 오버라이드 하여야한다. 하지않으면 오류 발생!
```java
abstract class Shape{
    public abstract void draw();
}
```
* 일반 메소드로 정의되면 자식 클래스에서 오버라이드 하지 않아도 컴파일러가 체크할 방법이 없다.
```java
class Shape{
    public void draw();
}
```
***
🔺 2022. 11. 08.