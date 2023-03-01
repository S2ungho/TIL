interface Area{
    void getArea();
}
interface Movable extends Area{
    void move(int dx, int dy);
}
class Shape implements Movable{
    int x, y;
    public void move(int dx, int dy){
        x += dx;
        y += dy;
    }
    public void getArea(){
        System.out.println(x + " " + y);
    }
}
class Rectangle extends Shape{
    int weight, height;
    public void getArea(){
        System.out.println(x + " " + y);
    }
}
class Triangle extends Shape{
    int base, height;
    public void getArea(){
        System.out.println(x + " " + y);
    }
}
class Circle extends Shape{
    int radius;
    public void getArea(){
        System.out.println(x + " " + y);
    }
}

public class Lab8 {
    public static void main(String args[]) {
//        Shape s = new Shape();
//        s.move(10,10);
//        System.out.println(s.a+" "+s.b);
        Movable[] arrayOfShapes;
        arrayOfShapes = new Movable[3];
        arrayOfShapes[0] = new Rectangle();
        arrayOfShapes[1] = new Triangle();
        arrayOfShapes[2] = new Circle();
        for(int i = 0;i < 3;i++){
            arrayOfShapes[i] = new Shape();
            arrayOfShapes[i].move(10,10);
            arrayOfShapes[i].getArea();
        }
    }
}