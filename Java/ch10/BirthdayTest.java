package ch10;

public class BirthdayTest {
    public static void main(String[] args){
        Birthday date = new Birthday();
        date.setYear(2000);
        date.setMonth(1);
        date.setDay(6);

        date.showDate();
    }
}
