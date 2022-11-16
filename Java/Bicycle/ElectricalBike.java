package Bicycle;

public class ElectricalBike extends Bicycle{
    private int battery;
    public ElectricalBike(int startbattery, int startSpeed, int startGear){
        super(startGear, startSpeed);
        battery = startbattery;
    }
    public void setBattery(int bat){
        battery = bat;
    }
    public int  getBattery(){
        return battery;
    }
    public void SpeedDown(int per){
        speed = speed - battery * per/100;
    }
    public void SpeedUp(int per){
        speed = speed - battery * per/100;
    }
    public void print(){
        System.out.println(this.speed);
    }
}