# 상속 (Inheritance)
>상속은 기존에 존재하는 클래스로부터 필드와 메소드를 이어받고, 필요한 기능을 추가할 수 있는 기법이다.
## 상속의 형식
* 자바에서는 extends 키워드를 이용하여 상속을 나타낸다.
```java
class ElectricCar extends Car{
    int batteryLevel;
    public void charge(int amount){
        batteryLevel += amount;
    }
}
```
* 자식클래스 또는 서브클래스 **ElectricCar** 는 부모클래스 또는 슈퍼클래스인 **Car** 가 가지고 있는 모든 멤버들을 전부 상속받고 자신이 필요한 멤버를 추가하기 때문에 항상 자식 클래스가 부모클래스를 포함하게 된다.
