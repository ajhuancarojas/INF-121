package lab4;
import java.util.Scanner;
public class Prueba {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        Empleado[] t = new Empleado[5];
         System.out.println(" TIEMPO COMPLETO");
        for (int i = 0; i < 3; i++) {
            System.out.print("Nombre: ");
            String nom= scanner.nextLine();
            System.out.print("Salario Anual: ");
            double salarioAnual = scanner.nextDouble();
            scanner.nextLine();  
            t[i] = new EmpleadoTiempoCompleto(nom, salarioAnual);
        }
        System.out.println("TIEMPO HORARIO");
        for (int i = 3; i < 5; i++) {
            System.out.print("Nombre: ");
            String nom = scanner.nextLine();
            System.out.print("Horas Trabajadas: ");
            double horas = scanner.nextDouble();
            System.out.print("Tarifa por Hora: ");
            double tarifa = scanner.nextDouble();
            scanner.nextLine();
            t[i] = new EmpleadoTiempoHorario(nom, horas, tarifa);
        }
        System.out.println("--- ************ ---");
        for (int i = 0; i < t.length; i++) {
        Empleado emp = t[i];
        System.out.println(emp.toString());
    }
    }
}


