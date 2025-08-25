package lab1;
import java.util.Scanner;
public class mainEstadistica {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        double[] num = new double[10];

        System.out.println("ingresa 10 numeros:");
        for (int i = 0; i < 10; i++) {
            num[i] = sc.nextDouble();
        }

        Estadistica est = new Estadistica(num);

        System.out.printf("El promedio es %.2f\n", est.promedio());
        System.out.printf("La desviacion estandar es %.5f\n", est.desviacion());
    }
}
