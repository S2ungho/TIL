package Bicycle;

abstract public class Bicycle{
    protected int gear;
    protected  int speed;

    Bicycle(){
    }

    Bicycle(int gear, int speed){
        this.gear = gear;
        this.speed = speed;
    }

    public abstract void SpeedUp(int a);//(int a){
        //speed += a;
    //}
    public abstract void SpeedDown(int a);//(int a){
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
