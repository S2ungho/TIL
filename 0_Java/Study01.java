/** * A short description of the program.
 * @author Ham SeungHo
 * @assignment Study java
 * @date 2022.09.23
 */
import java.io.InputStream;
import java.util.Scanner;

public class Study01 {
    public static void main(String[] args) {
        for (int i = 1; i < 6; i+=2) {
            for(int k =0; k < 6-i; k+=2){
                System.out.print(" ");
            }
            for (int j = 0; j < i; j++) {
                System.out.print("*");
            }
        System.out.println();
        }
        for (int i = 7; i > 0; i-=2) {
            for(int k =6-i; k > 0; k-=2){
                System.out.print(" ");
            }
            for (int j = 0; j < i; j++) {
                System.out.print("*");
            }
            System.out.println();
        }
    }
}
/* 다이아몬드 */

