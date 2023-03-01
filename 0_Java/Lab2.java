/** * A short description of the program.
 * @author Ham SeungHo
 * @assignment JAVAProgramming- LABX
 * @date 2022.09.20
 * s60191982_hamseungho_Lab2.java
 * else라인 추가
 **/
import java.util.Random; //Random 클래스 사용
import java.util.*;

public class Lab2 {
    public static void main(String[] args){
        int num;
        double temp1, temp2;
        Scanner sc = new Scanner(System.in);

        for(;;) { //or while(true){}
            System.out.println("========================\n1. 화씨 -> 섭씨\n2. 섭씨 -> 화씨\n3. 프로그램 종료\n========================");
            System.out.print("번호를 선택하시오 : ");
            num = sc.nextInt();

            if (num == 1) {
                System.out.print("화씨 온도를 입력하세요 : ");
                temp1 = sc.nextDouble();
                temp2 = (temp1 - 32) * 5 / 9;
                System.out.println("섭씨 온도는 " + temp2);
            } else if (num == 2) {
                System.out.print("섭씨 온도를 입력하세요 : ");
                temp1 = sc.nextDouble();
                temp2 = (temp1 * 9 / 5) + 32;
                System.out.println("화씨 온도는 " + temp2);
            } else if (num == 3){
                System.out.println("반복을 종료합니다.");
                break;
            }
            else{
                System.out.println("잘못 입력되었습니다. 다시 입력해주세요.");
            }
        }
    }
}