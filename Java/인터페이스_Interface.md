# ✏️ 인터페이스 (Interface)
    여러 프로그래머들이 독립적으로 클래스를 작성하고, 이 클래스들을 합쳐서 하나의 소프트웨어를 완성하는 상황을 가정했을 때, 각자 클래스를 다른 사람의 클래스와 연결하려면 클래스 간의 상호작용을 기술하는 일종의 규격이 있어야하는데 이 규격을 인터페이스(Interface)로 정의할 수 있다.
* 인터페이스는 상속 관계가 아닌, 클래스 간의 유사성을 인코딩하는 데 사용된다.
> Ex) 예를 들어, 사람(Human)과 자동차(Car)는 둘 다 달릴 수 있다. 그렇다고 부모 클래스로 Runner를 작성하고, Human과 Car를 Runner 클래스의 자식 클래스로 나타내는 것은 약간 이치에 맞지 않는다.
<br>이런 경우에 Runnable 인터페이스를 만들고 이 인터페이스를 양쪽 클래스가 구현하게 하면 된다
* 인터페이스 정의

```java
public interface 인터페이스_이름 {
    반환형  추상메소드1(...);
    반환형  추상메소드2(...);
    ...
}
```
* 인터페이스 예시
```java
public interface RemoteControl{
    //추상 메소드 정의
    public void turnOn();
    public void turnOff();
    // 인터페이스 안에서 언언되는 메소드들은 모두 묵시적으로 public abstract이다.
}
```
## 인터페이스 구현
* 인터페이스 만으로는 객체를 생성할 수 없다. (컴파일 에러) <br>인터페이스 안에는 구현되지 않은 메소드가 존재하기 때문이다.
* 인터페이스는 다른 클래스에 의하여 구현(implement)될 수 있다. 인터페이스를 구현한다는 말은 인터페이스에 정의된 추상 메소드의 몸체를 정의한다는 의미이다.
* 클래스가 인터페이스를 구현하기 위해서는 implement 키워드를 사용한다.
```java
class Television implements RemoteControl{
    boolean on;
    public void turnOn(){
        on = true;
        System.out.println("TV On");
    }
    public void turnOff(){
        on = false;
        System.out.println("TV Off");
    }
}
```
```java
Television t = new Television();
t.turnOn();
t.turnOff();
```
***
🔺 2022. 11. 08.