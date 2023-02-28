package ch10;

public class Birthday {
    private int day;
    private int month;
    private int year;
    private boolean isValid;

    public int getDay() {
        return day;
    }

    public void setDay(int day) {
        this.day = day;
    }

    public int getMonth() {
        return month;
    }

    public void setMonth(int month) {
        if(month > 0 && month < 13){
            isValid = true;
            this.month = month;
        }
    }

    public int getYear() {
        return year;
    }

    public void setYear(int year) {
        this.year = year;
    }
    public void showDate(){
        if(isValid){
            System.out.println(year + "년 "+month+"월 " + day + "일");
        }else{
            System.out.println("Error");
        }
    }
}
