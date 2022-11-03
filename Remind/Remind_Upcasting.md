# ⭐️ 업캐스팅
* 헷갈린 내용 : 아래와 같은 코드에서 객체 s를 Shape 타입으로 선언 후 Rectangle 인스턴스를 생성하면, 객체 s가 Shape타입으로 선언 되어서 Rectangle 의 정수 x는 s.x 와 같이 불러올 수 없지만 Shape 클래스와 Rectangle 클래스에 모두 오버라이딩으로 정의 된 draw 메소드는 오버라이딩 된 Rectangle의 draw 메소드의 값인 "draw Rectangle"이 출력 된다는 것을 알 수 있었다.
```java
class Shape{
    public void draw(){
        System.out.println("Shape");
    }
}

class Circle extends Shape{
//@override
    public void draw(){
        System.out.println("draw Circle");
    }
}

class Rectangle extends Shape{
        int x;
//@override
    public void draw(){
        System.out.println("draw Rectangle");
    }
}

class Triangle extends Shape{
//@override
    public void draw(){
        System.out.println("draw Triangle");
    }
}

public class ShapeTest{
    public static void main(String args[]){
        Shape s =new Rectangle();
        s.draw();
        //s.x = 0;
        //System.out.println(s.x);
    }
}
```