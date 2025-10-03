package Introduccion_POO;

public class testCartaBuzon {
    public static void main(String[] args) {

        Buzon b1 = new Buzon(101, 5);
        Buzon b2 = new Buzon(102, 3);
        Buzon b3 = new Buzon(103, 7);
        System.out.println("Buzón 1: = " + b1.getNro() + ", Cantidad = " + b1.getCantidad());
        System.out.println("Buzón 2: = " + b2.getNro() + ", Cantidad = " + b2.getCantidad());
        System.out.println("Buzón 3: = " + b3.getNro() + ", Cantidad = " + b3.getCantidad());
         Carta c1 = new Carta("C123", "Juan", "Inan Chaves", "envio de documentos");
        Carta c2 = new Carta("C456", "Pepe", "Cesar Perez", "invitacion a evento");
        Carta c3 = new Carta("C789", "Paty", "Amanda Mujica", "Respuesta oficial");
        System.out.println("\nCarta 1: Código = " + c1.getCodigo() + ", Remitente = " + c1.getRemitente() +
                           ", Destinatario = " + c1.getDestinatario() + ", Descripción = " + c1.getDescripcion());
        System.out.println("Carta 2: Código = " + c2.getCodigo() + ", Remitente = " + c2.getRemitente() +
                           ", Destinatario = " + c2.getDestinatario() + ", Descripción = " + c2.getDescripcion());
        System.out.println("Carta 3: Código = " + c3.getCodigo() + ", Remitente = " + c3.getRemitente() +
                           ", Destinatario = " + c3.getDestinatario() + ", Descripción = " + c3.getDescripcion());

        int cartasRecibidas = 0;
        if (c1.getDestinatario().equals("Juan")) cartasRecibidas++;
        if (c2.getDestinatario().equals("Juan")) cartasRecibidas++;
        if (c3.getDestinatario().equals("Juan")) cartasRecibidas++;
        System.out.println("\nCartas recibidas por Juan: " + cartasRecibidas);
        boolean remitenteRecibio = false;
        for (Carta c : new Carta[]{c1, c2, c3}) {
            for (Carta ca : new Carta[]{c1, c2, c3}) {
                if (c.getRemitente().equals(ca.getDestinatario())) {
                    System.out.println("El remitente " + c.getRemitente() + " ha recibido una carta de " + ca.getRemitente());
                    remitenteRecibio = true;
                }
            }
        }
        if (!remitenteRecibio) {
            System.out.println("ningun remitente ha recibido carta.");
        }

      System.out.println("\nCoincidencias de remitentes como destinatarios:");
        for (Carta c : new Carta[]{c1, c2, c3}) {
            for (Carta ca : new Carta[]{c1, c2, c3}) {
                if (c.getRemitente().equals(ca.getDestinatario())) {
                    System.out.println("Código: " + ca.getCodigo() + ", Remitente: " + ca.getRemitente() + ", Destinatario: " + ca.getDestinatario());
                }
            }
        }
    }
}