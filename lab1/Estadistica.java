package lab1;
public class Estadistica {
    private double[] n;
    public Estadistica(double[] n) {
        this.n = n;
    }
    public double promedio() {
        double s = 0;
        for (int i = 0; i < n.length; i++) {
            s = s+ n[i];
        }
        return s / n.length;
    }
    public double desviacion() {
        double prom = promedio();
        double s=0;
        for (int i = 0; i < n.length; i++) {
            s= s+ Math.pow(n[i] - prom, 2);
        }
        return Math.sqrt(s / (n.length - 1));
    }
}
