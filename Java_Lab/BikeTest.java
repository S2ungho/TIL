/** * A short description of the program.
 * @author Ham SeungHo
 * @SID 60191982
 * @assignment java - lab7
 * @date 2022.11.03
 */
import java.util.*;

class Bicycle{
        protected int gear;
        protected  int speed;

        Bicycle(){
        }

        Bicycle(int gear, int speed){
                this.gear = gear;
                this.speed = speed;
        }

        public void SpeedUp(int a){
                speed += a;
        }
        public void SpeedDown(int a){
                speed -= a;
        }
        public void GearUp(int a){
                gear += a;
        }
        public void GearDown(int a){
               gear -= a;
        }
        public void setSpeed(int speed){
                if (speed < 0)
                        this.speed = 0;
                else
                        this.speed = speed;
        }
	public void print(){
		System.out.println(this.speed);
	}
}


class MountainBike extends Bicycle{
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
	public int getHeight(){
		return seatHeight;
	}
	public void SpeedDown(int per){
		speed = speed - speed*per/100;
	}
	public void SpeedUp(int per){
		speed = speed + speed*per/100;
	}
	public void print(){
                System.out.println(this.speed);
        }
}

class Cycle extends Bicycle{
	private boolean isbasket;
	public Cycle(boolean startBasket, int startSpeed, int startGear){
		super(startGear, startSpeed);
		isbasket = startBasket;
	}
	public boolean getBasket(){
                return isbasket;
        }
	public void setBasket(boolean b){
		isbasket = b;
	}
	public void SpeedDown(int per){
                speed = speed - speed*per/100 +10;
        }
        public void SpeedUp(int per){
                speed = speed + speed*per/100 +10;
        }
	public void print(){
                System.out.println(this.speed);
        }
}

class ElectricalBike extends Bicycle{
	private int battery;
	public ElectricalBike(int startbattery, int startSpeed, int startGear){
			super(startGear, startSpeed);
			battery = startbattery;
	}
	public void setBattery(int bat){
			battery = bat;
	}
	public int  getBattery(){
			return battery;
	}
	public void SpeedDown(int per){
			speed = speed - battery * per/100;
	}
	public void SpeedUp(int per){
			speed = speed - battery * per/100;
	}
	public void print(){
			System.out.println(this.speed);
	}
}



public class BikeTest{
	public static void main(String args[]){
		//MountainBike mbike = new MountainBike(10,10,2);
		//Cycle cbike = new Cycle(1,10,2);
		//ElectricalBike ebike = new ElectricalBike(0,10,2);
		//System.out.println("\nstartspeed : " + mbike.speed + " , startgear: " + mbike.gear + " , startHeight : " + mbike.seatHeight+"\n");
		//System.out.println("\nstartspeed : " + cbike.speed + " , startgear: " + cbike.gear + " , basket : " + getBasket()+"\n");
		//System.out.println("\nstartspeed : " + ebike.speed + " , startgear: " + ebike.gear + " , battery : " + getBattery()+"\n");
		
		Bicycle[] arrayBike;
		arrayBike = new Bicycle[3];

		arrayBike[0] = new MountainBike(10,10,2);
		arrayBike[1] = new Cycle(false,10,2);
		arrayBike[2] = new ElectricalBike(10,10,2);

		for(int i = 0; i <arrayBike.length; i++){
			arrayBike[i].SpeedDown(10);
			arrayBike[i].print();
		}

		/*System.out.println("\nstartspeed : " + mbike.speed + " , startgear: " + mbike.gear + " , startHeight : " + mbike.seatHeight+"\n");
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
*/
	}
}
