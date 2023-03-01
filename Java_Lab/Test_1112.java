interface Flyable { void fly(); }

class Car{
    int speed;
    void setSpeed(int speed){ this.speed = speed; }
}

public class Test_1112 extends Car implements Flyable{
    @Override
    public void fly() {
        System.out.println("Fly");
    }
    public static void main(String args[]){
        Test_1112 f = new Test_1112();
        f.setSpeed(300);
        System.out.println(f.speed);
        f.fly();
    }
}
