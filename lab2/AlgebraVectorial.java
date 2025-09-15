package lab2;
public class AlgebraVectorial {
    private double x;
    private double y;

    public AlgebraVectorial() {
        this.x = 0;
        this.y = 0;
    }
    public AlgebraVectorial(double x, double y) {
        this.x = x;
        this.y = y;
    }

    public boolean Perpendicular(AlgebraVectorial b) {
        double suma = Math.sqrt(Math.pow(this.x + b.x, 2) + Math.pow(this.y + b.y, 2));
        double resta = Math.sqrt(Math.pow(this.x - b.x, 2) + Math.pow(this.y - b.y, 2));
        return Math.abs(suma - resta) < 1e-6;
    }

    public boolean Perpendicular(AlgebraVectorial b, int t) {
        double A = Math.sqrt(this.x * this.x + this.y * this.y);
        double B = Math.sqrt(b.x * b.x + b.y * b.y);
        return Math.abs(A - B) < 1e-6;
    }

    public boolean Perpendicular(AlgebraVectorial b, double d) {
        double po = this.x * b.x + this.y * b.y;
        return Math.abs(po) < 1e-6;
    }

    public boolean Perpendicular(AlgebraVectorial b, String t) {
        double ns = Math.pow(this.x + b.x, 2) + Math.pow(this.y + b.y, 2);
        double nac = this.x * this.x + this.y * this.y;
        double nbc = b.x * b.x + b.y * b.y;
        return Math.abs(ns - (nac + nbc)) < 1e-6;
    }

    public boolean Paralela(AlgebraVectorial b) {
        if (b.x == 0 && b.y == 0)
            return false;
        Double rX = (b.x != 0) ? this.x / b.x : null;
        Double rY = (b.y != 0) ? this.y / b.y : null;
        if (rX == null) 
            return true;
        if (rY == null) 
            return true;
        return Math.abs(rX - rY) < 1e-6;
    }

    public boolean Paralela(AlgebraVectorial b, boolean pc) {
        double f = this.x * b.y - this.y * b.x;
        return Math.abs(f) < 1e-6;
    }

    public AlgebraVectorial Proyeccion(AlgebraVectorial b) {
        double pp = this.x * b.x + this.y * b.y;
        double normaBCuadrado = b.x * b.x + b.y * b.y;
        double escalar = pp / normaBCuadrado;
        return new AlgebraVectorial(escalar * b.x, escalar * b.y);
    }

    public double Componente(AlgebraVectorial b) {
        double pp = this.x * b.x + this.y * b.y;
        double normaB = Math.sqrt(b.x * b.x + b.y * b.y);
        return pp / normaB;
    }
    public String toString() {
        return "(" + x + ", " + y + ")";
    }
}
