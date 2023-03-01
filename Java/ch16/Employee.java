package ch16;

public class Employee {
    private static int serialNum = 1000;
    private int employeeId;
    private String employeeName;
    private String department;
    public Employee(){
        serialNum++;
        employeeId = serialNum;

    }

    public static int getSerialNum() {
        int i = 0;
        //employeeName = "Lee"; //정적 변수 안에서 일반 멤버 사용 불가능, 지역 변수는 가능
        return serialNum;
    }

    public int getEmployeeId() {
        return employeeId;
    }

    public void setEmployeeId(int employeeId) {
        this.employeeId = employeeId;
    }

    public String getEmployeeName() {
        return employeeName;
    }

    public void setEmployeeName(String employeeName) {
        this.employeeName = employeeName;
    }

    public String getDepartment() {
        return department;
    }

    public void setDepartment(String department) {
        this.department = department;
    }
}
