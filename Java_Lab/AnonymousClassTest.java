interface RemoteControl{
    void turnOn();
    void turnOff();
}

public class AnonymousClassTest {
    public static void main(String args[]){
        RemoteControl ac = new RemoteControl(){
            public void turnOn(){
                System.out.println("Tv on");
            }
            public void turnOff(){
                System.out.println("Tv Off");
            }
        };
        ac.turnOn();
        ac.turnOff();
    }
}
