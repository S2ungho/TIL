class MyArrayAlg{
    public static <T> T getLast(T[] a){
        return a[a.length - 1];
    }
}
public class MyArrayTest{
    public static void main(String[] args){
        String[] language = {"C","A","B"};
        String last = MyArrayAlg.getLast(language);
        System.out.println(last);
    }
}