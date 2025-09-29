package lab4;
public class Circulo extends Figura {
    private double radio;
    public Circulo(double radio) {
        this.radio = radio;
        this.color = "amarillo";
    }
    @Override
    public double area() {
        return Math.PI * radio * radio;
    }
    @Override
    public double perimetro() {
        return 2 * Math.PI * radio;
    }
    @Override
    public String toString() {
        return "circulo - radio: " + radio + ", " + super.toString();
    }
}

