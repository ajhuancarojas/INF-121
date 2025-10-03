package Introduccion_POO;
public class Producto {
    public String nombre;
    public double precio;
    public int stock;
    public Producto(String nombre, double precio, int stock) {
        this.nombre = nombre;
        this.precio = precio;
        this.stock = stock;
    }
    public void vender(int cantidad) {
        if (cantidad <= stock) {
            stock -= cantidad;
            System.out.println("Venta realizada: " + cantidad + " u");
        } else {
            System.out.println("No hay suficiente stock para vender " + cantidad + " u");
        }
    }
    public void reabastecer(int cantidad) {
        stock += cantidad;
        System.out.println("restablecer: " + cantidad + " u");
    }
}


