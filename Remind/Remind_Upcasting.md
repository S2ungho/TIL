# ⭐️ 업캐스팅 (Upcasting)
* 헷갈린 내용 : 아래와 같은 코드에서 객체 s를 Shape 타입으로 선언 후 Rectangle 인스턴스를 생성하면,<br>객체 s가 Shape 타입으로 선언 되어서 Rectangle 의 정수 x는 s.x 와 같이 불러올 수 없었다.<br> 하지만 왜 draw 메소드는 Rectangle 의 draw 메소드가 실행되는지 궁금했다.
<br>
1. Shape 클래스에 draw()가 정의 되어있으며, 객체 s가 실제 가리키는 값은 Rectangle 이기 때문에 Rectangle의 draw() 메소드 실행

2. 객체 s 의 타입은 Shape이지만 실제로 가리키고 있는 객체의 타입은 Rectangle 이기 때문.
> 결론 : 부모 클래스인 Shape 클래스에 draw 메소드가 우선적으로 정의되어 있었기 때문에 객체 s가 가리키는 Rectangle 클래스에 **오버라이딩으로 정의 된 draw 메소드의 값인 "draw Rectangle"이 우선적으로 출력** 된다는 것을 알 수 있다.

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

***
🔺 2022. 11. 03.