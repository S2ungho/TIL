package ch14;

public class Subway {
    int SubwayNumber;
    int passengerCount;
    int money;
    public Subway(int SubwayNumber){
        this.SubwayNumber = SubwayNumber;
    }
    public void take(int money){
        this.money += money;
        passengerCount++;
    }
    public void showSubwayInfo(){
        System.out.println(SubwayNumber +" 번 지하철 "+ passengerCount +" 명," + money +"원" );
    }
}
