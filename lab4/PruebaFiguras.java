package lab4;
import java.util.Random;
public class PruebaFiguras {
    public static void main(String[] args) {
        Random random = new Random();
        Figura[] fig = new Figura[5];
        for (int i = 0; i < fig.length; i++) {
            int tipo = random.nextInt(2) + 1;
            if (tipo == 1) {
                double lado = 1 + random.nextDouble() * 9;
                fig[i] = new Cuadrado(lado);
            } else {
                double radio = 1 + random.nextDouble() * 9; 
                fig[i] = new Circulo(radio);
            }
        }
        System.out.println("---    FIGURAS    ---");
        for (int i = 0; i < fig.length; i++) {
            Figura figura = fig[i];
            System.out.println(figura);
            System.out.println("area: " + figura.area());
            System.out.println("perimetro: " + figura.perimetro());
            if (figura.getClass() == Cuadrado.class) {
                Cuadrado cuadrado = (Cuadrado) figura;
                System.out.println("metodo colorear: " + cuadrado.comoColorear());
            }
        }
    }
}
