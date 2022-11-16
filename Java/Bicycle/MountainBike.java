package Bicycle;

public class MountainBike extends Bicycle{
    int seatHeight;
    public MountainBike(int startHeight, int startSpeed, int startGear){
        super(startGear, startSpeed);
        seatHeight = startHeight;
    }
    public void setHeight(int height){
        if (height < 0)
            seatHeight = 0;
        else
            seatHeight = height;
    }
    public int getHeight(){
        return seatHeight;
    }
    public void SpeedDown(int per){
        speed -= speed*per/100;
    }
    public void SpeedUp(int per){
        speed += speed*per/100;
    }
    public void print(){
        System.out.println(this.speed);
    }
}