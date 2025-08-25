package lab1;
import java.util.Scanner;
public class mainEcuaciones1 {
    public static void main(String[] args) {
        Scanner sc=new Scanner(System.in);
        System.out.println("ingresa a, b, c, d, e, f =");
        double a= Double.parseDouble(sc.nextLine());
        double b= Double.parseDouble(sc.nextLine());
        double c= Double.parseDouble(sc.nextLine());
        double d= Double.parseDouble(sc.nextLine());
        double e= Double.parseDouble(sc.nextLine());
        double f= Double.parseDouble(sc.nextLine());
        
        EcuacionLineal ecua =new EcuacionLineal(a,b,c,d,e,f);//llama al constrictor
        if(ecua.gettieneSolucion()){
            System.out.println("X = "+ ecua.getX()+" ,  Y = "+ ecua.getY() );
        }
        else
            System.out.println("la ecuacion no tiene solucion ");
        
        
    }
    
}
