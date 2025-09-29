package lab4;
public class Cuadrado extends Figura implements Coloreado {
    private double lado;
    public Cuadrado(double lado) {
        this.lado = lado;
        this.color = "rosadoo ";
    }
    @Override
    public double area() {
        return lado * lado;
    }
    @Override
    public double perimetro() {
        return 4 * lado;
    }
    @Override
    public String comoColorear() {
        return "Colorear los 4 lados";
    }
    @Override
    public String toString() {
        return "Cuadrado - Lado: " + lado + ", " + super.toString();
    }
}

