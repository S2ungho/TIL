package ch14;

public class TakeTransTest {
    public static void main(String[] args) {
        Student person1 = new Student("james", 5000);
        Student person2 = new Student("tomas", 10000);
        Student person3 = new Student("Edward", 20000);

        Bus bus100 = new Bus(100);
        Bus bus500 = new Bus(500);

        person1.takeBus(bus100);

        Subway greenSub = new Subway(2);
        Subway blueSub = new Subway(1);
        person2.takeSubway(blueSub);

        person1.showInfo();
        person2.showInfo();
        blueSub.showSubwayInfo();

        Taxi zalTaxi = new Taxi("잘나간다");
        person3.takeTaxi(zalTaxi);

        person3.showInfo();
        zalTaxi.showTaxiInfo();

        //앞의 예제에서 에드워드는 지각을 해서 택시를 타야했습니다
        //이만원을 가지고 있었는데 만원을 택시비로 사용했습니다
        //택시는 잘나간다운수 회사 택시를 탔습니다
        //출력결과 : 에드워드님의 남은 돈은 만원입니다
        // 잘나간다 운수택시의 수입은 만원 입니다.
    }
}
