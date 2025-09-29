package lab4;
public class EmpleadoTiempoCompleto extends Empleado {
    private double salario_anual;
    public EmpleadoTiempoCompleto(String nombre, double salario_anual) {
        super(nombre);
        this.salario_anual = salario_anual;
    }
    @Override
    public double CalcularSalarioMensual() {
        return salario_anual / 12;
    }
    @Override
    public String toString() {
        return super.toString() + ", salario anual: " + salario_anual;
    }
}