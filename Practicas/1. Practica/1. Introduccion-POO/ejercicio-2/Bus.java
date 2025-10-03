public class Bus {
    private int capacidad;
    private int pasajero;
    private double costo;
    public Bus(int capacidad) {
        this.capacidad = capacidad;
        this.pasajero = 0;
        this.costo = 1.50; 
    }

    public void subirPasajeros(int cantidad) {
        if (pasajero + cantidad <= capacidad) {
            pasajero += cantidad;
            System.out.println(cantidad + "  subieron al bus");
        } else {
            System.out.println("No hay asientos suficientes.");
        }
    }

    public double cobrarPasaje() {
        return pasajero * costo;
    }
    public int asientosDisponibles() {
        return capacidad - pasajero;
    }
    
}
