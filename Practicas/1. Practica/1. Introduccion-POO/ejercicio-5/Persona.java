package Introduccion_POO;
public class Persona {
    public  String nombre;
    public String paterno;
    public String materno;
    private int edad;
    private String ci;
    public Persona(String nombre, String paterno, String materno, int edad, String ci) {
        this.nombre = nombre;
        this.paterno = paterno;
        this.materno = materno;
        this.edad = edad;
        this.ci = ci;
    }
    public void mostrarDatos() {
        System.out.println("Nombre: " + nombre);
        System.out.println("Paterno: " + paterno);
        System.out.println("Materno: " + materno);
        System.out.println("Edad: " + edad);
        System.out.println("CI: " + ci);
    }
    public boolean mayorEdad() {
        return edad >= 18;
    }
    public void modificarEdad(int nuevaEdad) {
        if (nuevaEdad >= 0) {
            edad = nuevaEdad;
            System.out.println("Edad modificada: " + edad);
        } else {
            System.out.println("error...");
        }
    }
    public boolean mismoPaterno(Persona otraPersona) {
        return this.paterno.equals(otraPersona.paterno);
    }
   
}
