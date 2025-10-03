package Introduccion_POO;
public class Mascota {
    private String nombre;
    private int energia;

    public Mascota(String nombre) {
        this.nombre = nombre;
        this.energia = 50;
    }

    public void alimentar() {
        energia += 20;
        if (energia > 100) {
            energia = 100;
        }
        System.out.println(nombre + " ha sido alimentado. energia actual: " + energia);
    }

    public void jugar() {
        if (energia >= 15) {
            energia -= 15;
            System.out.println(nombre + " a jugado.actual: " + energia);
        } else {
            System.out.println(nombre + " no tiene suficiente energia para jugar.");
        }
    }
    public void mostrarEnergia() {
        System.out.println("energia de " + nombre + ": " + energia);
    }
    
}
