import java.util.ArrayList;

class Persona {
    String nombre;
    int edad;
    float peso;
    
    public Persona(String nombre, int edad, float peso) {
        this.nombre = nombre;
        this.edad = edad;
        this.peso = peso;
    }
}

class Cabina {
    int nroCabina;
    ArrayList<Persona> personasAbordo = new ArrayList<>();
    final int MAX_PERSONAS = 10;
    final float MAX_PESO = 850.0f;
    
    public Cabina(int nroCabina) {
        this.nroCabina = nroCabina;
    }
    
    public boolean agregarPersona(Persona p) {
        if (personasAbordo.size() >= MAX_PERSONAS) return false;
        if (pesoTotal() + p.peso > MAX_PESO) return false;
        personasAbordo.add(p);
        return true;
    }
    
    public float pesoTotal() {
        float total = 0;
        for (Persona p : personasAbordo) total += p.peso;
        return total;
    }
}

class Linea {
    String color;
    ArrayList<Persona> filaPersonas = new ArrayList<>();
    ArrayList<Cabina> cabinas = new ArrayList<>();
    
    public Linea(String color) {
        this.color = color;
    }
    
    public void agregarPersona(Persona p) {
        filaPersonas.add(p);
    }
    
    public void agregarCabina(int nro) {
        cabinas.add(new Cabina(nro));
    }
    
    public float ingresoTotal() {
        float total = 0;
        for (Cabina c : cabinas)
            for (Persona p : c.personasAbordo)
                total += (p.edad >= 25 && p.edad <= 60) ? 1.5f : 3.0f;
        return total;
    }
    
    public float ingresoSoloRegular() {
        int contador = 0;
        for (Cabina c : cabinas)
            for (Persona p : c.personasAbordo)
                if (!(p.edad >= 25 && p.edad <= 60)) contador++;
        return contador * 3.0f;
    }
}

class MiTeleferico {
    ArrayList<Linea> lineas = new ArrayList<>();
    
    public MiTeleferico() {
        lineas.add(new Linea("Amarillo"));
        lineas.add(new Linea("Rojo"));
        lineas.add(new Linea("Verde"));
    }
    
    public void agregarPersonaFila(Persona p, String linea) {
        for (Linea l : lineas)
            if (l.color.equalsIgnoreCase(linea))
                l.agregarPersona(p);
    }
    
    public void agregarCabina(String linea, int nro) {
        for (Linea l : lineas)
            if (l.color.equalsIgnoreCase(linea))
                l.agregarCabina(nro);
    }
    
    public void subirPrimerasPersonas() {
        for (Linea l : lineas) {
            if (!l.filaPersonas.isEmpty() && !l.cabinas.isEmpty()) {
                Persona p = l.filaPersonas.remove(0);
                for (Cabina c : l.cabinas) {
                    if (c.agregarPersona(p)) break;
                }
            }
        }
    }
    
    public boolean verificarReglasTodasCabinas() {
        for (Linea l : lineas)
            for (Cabina c : l.cabinas)
                if (c.personasAbordo.size() > 10 || c.pesoTotal() > 850.0f)
                    return false;
        return true;
    }
    
    public float calcularIngresoTotalTodasLineas() {
        float total = 0;
        for (Linea l : lineas) total += l.ingresoTotal();
        return total;
    }
    
    public String lineaConMayorIngresoTarifaRegular() {
        Linea mejor = null;
        float max = -1;
        for (Linea l : lineas) {
            float ing = l.ingresoSoloRegular();
            if (ing > max) {
                max = ing;
                mejor = l;
            }
        }
        return mejor != null ? mejor.color : "Ninguna";
    }
}

public class TestTeleferico {
    public static void main(String[] args) {
        MiTeleferico tele = new MiTeleferico();
        
        tele.agregarCabina("Amarillo", 1);
        tele.agregarCabina("Rojo", 1);
        tele.agregarCabina("Verde", 1);
        
        tele.agregarPersonaFila(new Persona("Ana", 20, 60), "Amarillo");
        tele.agregarPersonaFila(new Persona("Luis", 30, 80), "Amarillo");
        tele.agregarPersonaFila(new Persona("Rosa", 65, 70), "Rojo");
        tele.agregarPersonaFila(new Persona("Carlos", 12, 45), "Verde");
        
        tele.subirPrimerasPersonas();
        
        System.out.println("Reglas cumplidas: " + tele.verificarReglasTodasCabinas());
        System.out.println("Ingreso total: " + tele.calcularIngresoTotalTodasLineas());
        System.out.println("Línea mayor tarifa regular: " + tele.lineaConMayorIngresoTarifaRegular());
    }
}