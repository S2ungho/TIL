/** * A short description of the program.
 * @author Seungho HAM
 * @SID 60191982
 * @assignment java - lab8
 * @date 2022.11.15
 */
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
    int weight = 20, height = 15;
    public void getArea(){
        System.out.println("Rectangle\t: Weight = " + (weight + x) + ",\tHeight = " + (height + y));
    }
}
class Triangle extends Shape{
    int base = 10, height = 10;
    public void getArea(){
        System.out.println("Triangle\t: Base = " + (base + x) + ",\tHeight = " + (height + y)  );
    }
}
class Circle extends Shape{
    int radius = 3;
    public void getArea(){
        System.out.println("Circle\t\t: Radius = " + (radius + x + y));
    }
}

public class ShapeTest {
    public static void main(String args[]) {
        Shape[] arrayOfShapes;
        arrayOfShapes = new Shape[3];
        arrayOfShapes[0] = new Rectangle();
        arrayOfShapes[1] = new Triangle();
        arrayOfShapes[2] = new Circle();
        for(int i = 0;i < 3;i++){
            arrayOfShapes[i].move(10,10);
            arrayOfShapes[i].getArea();
        }
    }
}