import java.util.*;
import java.lang.*;

public class Generic{
    public static void main(String[] args){
            int a = 100;
            double b = 200;
            Integer i = new Integer(9);
            Double d = new Double(11);
            System.out.println(a);
            System.out.println(b);
            System.out.println(i);
            System.out.println(d);
            i.compareTo(a);
            System.out.println(i.compareTo(a));
            System.out.println(d.compareTo(b));
    }
}