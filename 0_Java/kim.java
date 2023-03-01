import java.util.Scanner;

public class kim {

    public static void main(String[] args) {
        System.out.println("김가희/60192896/과제 #1-1");
        Scanner scanner = new Scanner(System.in);

        float result=0;
        System.out.print("num1>>");
        float number1 = scanner.nextFloat();
        System.out.print("cal>>");
        String calculation = scanner.next();
        System.out.print("num2>>");
        float number2 = scanner.nextFloat();

        if(calculation.equals("/") == true && number2 == 0.0) {
            System.out.print("0으로 나눌 수 없음");
        }
        else {
            if (calculation.equals("+"))
                result += number1 + number2;
            else if (calculation.equals("-"))
                result += number1 - number2;
            else if (calculation.equals("*"))
                result += number1 * number2;
            else if (calculation.equals("/"))
                result += number1 / number2;
            else if (calculation.equals("%"))
                result += number1 % number2;
            else
                System.out.print("해당없음");
            System.out.print(number1 + calculation + number2 + "의 계산결과는" + result);
        }
        scanner.close();


    }

}