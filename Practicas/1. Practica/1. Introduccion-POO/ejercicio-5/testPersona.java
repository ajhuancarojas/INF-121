package Introduccion_POO;
public class testPersona {
     public static void main(String[] args) {
        Persona p1 = new Persona("PEDRO", "HUANCA", "QUISPE", 20, "1234567");
        Persona p2 = new Persona("MARIA", "HUANCA", "LOPEZ", 17, "8335588");
        p1.mostrarDatos();
        System.out.println("Es mayor de edad: " + p1.mayorEdad());
        p2.mostrarDatos();
        System.out.println("Es mayor de edad: " + p2.mayorEdad());
        System.out.println();
        System.out.println(p1.nombre + " y " + p2.nombre + " tienen el mismo paterno? " + p1.mismoPaterno(p1));
        p2.modificarEdad(18);
        System.out.println(p2.nombre + " es mayor de edad ahora? " + p2.mayorEdad());
    }
}
