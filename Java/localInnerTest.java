class localInner{
    private int data = 30;

    void display(){
        final String msg = "current data : ";

        class Local{
            void printMSG(){
                System.out.println(msg + data);
            }
        }
        Local obj = new Local();
        obj.printMSG();
    }
}
public class localInnerTest{
    public static void main(String args[]){
        localInner obj = new localInner();
        obj.display();
    }
}