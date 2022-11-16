package Bicycle;

public class Cycle extends Bicycle{
    private boolean isbasket;
    public Cycle(boolean startBasket, int startSpeed, int startGear){
        super(startGear, startSpeed);
        isbasket = startBasket;
    }
    public boolean getBasket(){
        return isbasket;
    }
    public void setBasket(boolean b){
        isbasket = b;
    }
    public void SpeedDown(int per){
        speed = speed - speed*per/100 +10;
    }
    public void SpeedUp(int per){
        speed = speed + speed*per/100 +10;
    }
    public void print(){
        System.out.println(this.speed);
    }
}