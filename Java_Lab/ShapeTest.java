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