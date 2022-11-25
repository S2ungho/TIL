import java.lang.*;

/*public class Box {
    private Object data;

    public void set(Object data) {
        this.data = data;
    }

    public Object get() {
        return data;
    }

    public static void main(String[] args){
        Box b = new Box();

        b.set("Hello"); // 문자열 객체를 저장
        String s = (String)b.get(); //Object 타입을 String 타입으로 형변환
        System.out.println(b);

        b.set(new Integer(10)); //정수 객체를 저장
        Integer i = (Integer)b.get(); // Object 타입을 Integer 타입으로 형변환
        System.out.println(i);
    }
}
//Box@2f92e0f4
//10
// 위와 같은 값 출력
*/
public class Box<T> {
    private T data;
    public void set(T data){ this.data = data; }
    public T get(){ return data; }
    public static void main(String[] args){
        Box<String> b = new Box<String>();
        b.set("Hello");
        String s = b.get();
        System.out.println(s);
    }
}
