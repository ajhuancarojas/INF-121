package lab1;
import java.util.Scanner;
public class mainEcuaciones2 {
    public static void main(String[] args) {
        Scanner sc=new Scanner(System.in);
        System.out.println("ingresa a, b, c =");
        float a= Float.parseFloat(sc.nextLine());
        float b= Float.parseFloat(sc.nextLine());
        float c= Float.parseFloat(sc.nextLine());

        
        EcuacionCuadratica ecuacion =new EcuacionCuadratica(a,b,c);//llama al constrictor
        if(ecuacion.getDiscriminante() >0){
            System.out.println("la ecuacion tiene dos raices :"+ecuacion.getRaiz1()+" y "+ecuacion.getRaiz2());    
        }
        else if(ecuacion.getDiscriminante()==0){
            System.out.println("la ecuacion tiene solo una raiz :"+ ecuacion.getRaiz1());
        }
        else
            System.out.println("la ecuacion no tiene raices reales ");
        
        
    }
    
}
