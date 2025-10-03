public class testBus {
     public static void main(String[] args) {
        Bus c = new Bus(50);
        c.subirPasajeros(15); 
        c.subirPasajeros(25); 
        System.out.println("Asientos disponibles: " + c.asientosDisponibles());
        System.out.println("Total a cobrar: Bs. " + c.cobrarPasaje());
    }
}
