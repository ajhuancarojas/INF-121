package lab2;
public class testAlgebra {

    public static void main(String[] args) {
        AlgebraVectorial a = new AlgebraVectorial(3, 4);
        AlgebraVectorial b = new AlgebraVectorial(-4, 3);

        System.out.println("a = " + a);
        System.out.println("b = " + b);

        System.out.println("a) Perpendicular : " + a.Perpendicular(b));
        System.out.println("b) Perpendicular : " + a.Perpendicular(b, 1));
        System.out.println("c) Perpendicular : " + a.Perpendicular(b, 0.0));
        System.out.println("d) Perpendicular : " + a.Perpendicular(b, " "));
        System.out.println("e) Paralela : " + a.Paralela(b));
        System.out.println("f) Paralela : " + a.Paralela(b, true));
        System.out.println("g) Proyeccion : " + a.Proyeccion(b));
        System.out.println("h) Componente : " + a.Componente(b));
    }


}
