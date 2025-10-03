
package Introduccion_POO;

public class testMascota {
  public static void main(String[] args) {
        Mascota m1 = new Mascota("beto");
        Mascota m2 = new Mascota("esperanza");

        m1.alimentar();
        m1.jugar();
        m2.alimentar();
        m2.jugar();
        m1.mostrarEnergia();
        m2.mostrarEnergia();
    }
}
