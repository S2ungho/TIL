package ch14;

public class Taxi {
    String taxiName;
    String studentName;
    int money;
    public Taxi(String taxiName){
        this.taxiName = taxiName;
    }
    public void take(int money){
        this.money += money;
    }
    public void showTaxiInfo(){
        System.out.println(taxiName +" 운수의 수입은 "+money+"원 입니다.");
    }
}
