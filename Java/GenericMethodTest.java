import java.util.*;
import java.lang.*;

/*public class GenericMethodTest {
    public static void main(String args[]) {
        String s;

        Integer[] iArray = {10, 20, 30, 40, 50};
        Double[] dArray = {1.1, 1.2, 1.3, 1.4, 1.5};
        Character[] cArray = {'K', 'O', 'R', 'E', 'A'};

        List<Integer> list1 = Arrays.asList(iArray);
        List<Double> list2 = Arrays.asList(dArray);
        List<Character> list3 = Arrays.asList(cArray);

        Iterator e = list1.iterator();
        while(e.hasNext()){
            s = (String)e.next();
            System.out.println(s);
        }

        //printArray(iArray);
        //printArray(dArray);
        //printArray(cArray);
    }
}*/
public class GenericMethodTest {
    public static <T> void printArray(T[] array) {
        for (T element : array) {
            System.out.printf("%s ", element);
        }
        System.out.println();
    }

    public static void main(String args[]) {
        Integer[] iArray = {10, 20, 30, 40, 50};
        Double[] dArray = {1.1, 1.2, 1.3, 1.4, 1.5};
        Character[] cArray = {'S', 'E', 'U', 'N', 'G'};

        printArray(iArray);
        printArray(dArray);
        printArray(cArray);
    }
}