package lab1;
public class EcuacionCuadratica {
    private float a ;
    private float b ;
    private float c ;
    
    public EcuacionCuadratica(float a,float b, float c){
    this.a=a;
    this.b=b;
    this.c=c;
    }
    
    public float getDiscriminante()  {
        return (b * b) - (4 *a * c);
    }
    public float getRaiz1(){
        double dis = getDiscriminante();
        return (float)((-b + Math.sqrt(dis)) / (2 * a));
    }
    public float getRaiz2(){
        double dis= getDiscriminante();
        return (float)((-b - Math.sqrt(dis)) / (2 * a));
    }
}

