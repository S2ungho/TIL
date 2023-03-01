abstract class Shape{
    int x, y;
    public void translate(int x, int y){
        this.x = x;
        this.y = y;
    }
    public abstract void draw();
}

class Rectangle extends Shape{
    int width, height;
    public void draw(){ System.out.println("rectangle draw"); }
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
        s2.x;
    }

}
