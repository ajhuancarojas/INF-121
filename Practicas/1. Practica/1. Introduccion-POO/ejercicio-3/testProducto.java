
package Introduccion_POO;
public class testProducto {
   
    public static void main(String[] args) {
        Producto c = new Producto("CARNE", 50.5, 100);
        System.out.println("Producto: " + c.nombre);
        System.out.println("Precio: " + c.precio + " Bs.");
        System.out.println("Stock: " + c.stock);
        c.vender(50);
        c.reabastecer(7);
        System.out.println("Producto: " + c.nombre);
        System.out.println("Precio: " + c.precio + " Bs.");
        System.out.println("Stock: " + c.stock);

        System.out.println();

        
}
}
