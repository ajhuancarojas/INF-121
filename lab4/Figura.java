package lab4;
public abstract class Figura {
    public String color; 
    public void setColor(String color) {
        this.color = color;
    }
    public String getColor() {
        return color;
    }
    @Override
    public String toString() {
        return "Figura color: " + color;
    }
    public abstract double area();
    public abstract double perimetro();
}

