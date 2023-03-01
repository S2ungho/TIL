/** * A short description of the program.
 * @author Ham SeungHo
 * @assignment JAVAProgramming- LABX
 * @date 2022..09.13
 * @delete_
 **/
import java.util.Random; //Random 클래스 사용

public class Lab1 {
    public static void main(String[] args) {
        int x, y;
        int a;
        x = (int) (Math.random() * 100);
        y = (int) (Math.random() * 100);
        a = addition1(x,y);
        System.out.println(a);
        a = addition2(x,y);
        System.out.println(a);
        a = addition3(x,y);
        System.out.println(a);
        a = addition4(x,y);
        System.out.println(a);
    }

    public static int addition1(int i, int j){
        int res1 = i + j;
        return res1;
    }
    public static int addition2(int i, int j) {
        int res2 = i - j;
        return res2;
    }
    public static int addition3(int i, int j){
        int res3 = i * j;
        return res3;
    }
    public static int addition4(int i, int j){
        int res4 = i % j;
        return res4;
    }
}
