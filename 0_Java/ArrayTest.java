import java.util.*;

public class ArrayTest {
    public static void main(String[] args){
        int[] array = { 9,4,5,6,2,1};
        Arrays.sort(array); // 배열 정렬
        printArray(array);
        System.out.println(Arrays.binarySearch(array,9)); // 9를 탐색
        Arrays.fill(array,8); // 배열을 특정한 값으로 채움
        printArray(array);
    }
    private static void printArray(int[] array){
        System.out.print("[");
        for(int i = 0; i < array.length; i++){
            System.out.print(array[i]+" ");
        }
        System.out.println("]");
    }
}
