import Bicycle.*;
public class BikeTest{
    public static void main(String args[]){
        Bicycle[] arrayBike;
        arrayBike = new Bicycle[3];

        arrayBike[0] = new MountainBike(10,10,2);
        arrayBike[1] = new Cycle(false,10,2);
        arrayBike[2] = new ElectricalBike(20,10,2);

        for(int i = 0; i <arrayBike.length; i++){
            arrayBike[i].SpeedDown(10);
        }
        for(int i = 0; i <arrayBike.length; i++){
            arrayBike[i].print();
        }
    }
}
