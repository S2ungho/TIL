package ch16;

public class EmployeeTest {
    public static void main(String[] args) {
        Employee employeeLee = new Employee();
        employeeLee.setEmployeeName("이씨");

        Employee employeeKim = new Employee();
        employeeKim.setEmployeeName("김씨");

        System.out.println(employeeLee.getEmployeeName() + "님" +employeeLee.getEmployeeId());
        System.out.println(employeeKim.getEmployeeName() + "님" +employeeKim.getEmployeeId());

    }
}
