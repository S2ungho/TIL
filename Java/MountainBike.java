/** * A short description of the program.
 * @author Ham SeungHo
 * @SID 60191982
 * @assignment java - lab6
 * @date 2022.11.01
 */
import java.util.*;

class Bicycle{
        protected int gear;
        protected int speed;

        Bicycle(){
        }

        Bicycle(int gear, int speed){
                this.gear = gear;
                this.speed = speed;
        }

        void SpeedUp(int su){
                speed += su;
        }
        void SpeedDown(int sd){
                speed -= sd;
        }
        void GearUp(int gu){
                gear += gu;
        }
        void GearDown(int gd){
               gear -= gd;
        }
        public void setSpeed(int speed){
                if (speed < 0)
                        this.speed = 0;
                else
                        this.speed = speed;
        }
}

public class MountainBike extends Bicycle{
    int seatHeight;
    public MountainBike(int startHeight, int startSpeed, int startGear){
            super(startGear, startSpeed);
            seatHeight = startHeight;
    }
    public void setHeight(int height){
            if (height < 0)
                    seatHeight = 0;
            else
                    seatHeight = height;
    }

    public static void main(String args[]){
            MountainBike mbike = new MountainBike(10,10,2);
            System.out.println("\nstartspeed : " + mbike.speed + " , startgear: " + mbike.gear + " , startHeight : " + mbike.seatHeight+"\n");
            //mbike.setSpeed(-10); //Speed Setter
            //mbike.setHeight(50); //Height Setter
            //System.out.println("seatHeight : "+ mbike.seatHeight);
            for(int i = 0; i<3; i++){
                    mbike.SpeedUp(5);
                    System.out.println("speedup : " + mbike.speed);
            }
            for(int i = 0; i<5; i++){
                    mbike.GearUp(1);
                    System.out.println("gearup : " + mbike.gear);
            }
            System.out.println("\nspeed : " + mbike.speed + " , gear: " + mbike.gear + " , Height : " + mbike.seatHeight+"\n");
    }
}
