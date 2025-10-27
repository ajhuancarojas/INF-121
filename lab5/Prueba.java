package lab5;
import java.util.ArrayList;
import java.util.Date;

class Pagina {
    private int numero;
    private String contenido;
    public Pagina(int numero, String contenido) {
        this.numero = numero;
        this.contenido = contenido;
    }
    public void mostrarContenido() {
        System.out.println("Pagina " + numero + ": " + contenido);
    }
}

class Autor {
    private String nombre;
    private String nacionalidad;
    public Autor(String nombre, String nacionalidad) {
        this.nombre = nombre;
        this.nacionalidad = nacionalidad;
    }
    public void mostrarInfo() {
        System.out.println("Autor: " + nombre + " - " + nacionalidad);
    }
    public String getNombre() {
        return nombre;
    }
}

class Estudiante {
    private String codigo;
    private String nombre;
    public Estudiante(String codigo, String nombre) {
        this.codigo = codigo;
        this.nombre = nombre;
    }
    public void mostrarInfo() {
        System.out.println("Estudiante: " + nombre + " - Código: " + codigo);
    }
    public String getNombre() {
        return nombre;
    }
}

class Horario {
    private String diasApertura;
    private String horaApertura;
    private String horaCierre;
    public Horario(String diasApertura, String horaApertura, String horaCierre) {
        this.diasApertura = diasApertura;
        this.horaApertura = horaApertura;
        this.horaCierre = horaCierre;
    }
    public void mostrarHorario() {
        System.out.println("Horario: " + diasApertura + " de " + horaApertura + " a " + horaCierre);
    }
}

class Libro {
    private String titulo;
    private String isbn;
    private ArrayList<Pagina> paginas;
    public Libro(String titulo, String isbn, ArrayList<Pagina> paginas) {
        this.titulo = titulo;
        this.isbn = isbn;
        this.paginas = paginas;
    }
    public void leer() {
        System.out.println("Leyendo: " + titulo);
        for (Pagina pagina : paginas) {
            pagina.mostrarContenido();
        }
    } 
    public String getTitulo() {
        return titulo;
    }
}

class Prestamo {
    private Date fechaPrestamo;
    private Date fechaDevolucion;
    private Estudiante estudiante;
    private Libro libro;
    public Prestamo(Estudiante estudiante, Libro libro) {
        this.estudiante = estudiante;
        this.libro = libro;
        this.fechaPrestamo = new Date();
        long tiempo = 15L * 24 * 60 * 60 * 1000;
        this.fechaDevolucion = new Date(fechaPrestamo.getTime() + tiempo);
    }
    public void mostrarInfo() {
        System.out.println("Prestamo: " + estudiante.getNombre() + " - " + libro.getTitulo());
    }
}

class Biblioteca {
    private String nombre;
    private ArrayList<Libro> libros;
    private ArrayList<Autor> autores;
    private ArrayList<Prestamo> prestamosActivos;
    private Horario horario;
    public Biblioteca(String nombre) {
        this.nombre = nombre;
        this.libros = new ArrayList<Libro>();
        this.autores = new ArrayList<Autor>();
        this.prestamosActivos = new ArrayList<Prestamo>();
        this.horario = new Horario("Lunes a Sabado", "08:00", "16:00");
    }
    public void agregarLibro(Libro libro) {
        libros.add(libro);
    }
    public void agregarAutor(Autor autor) {
        autores.add(autor);
    }
    public void prestarLibro(Estudiante estudiante, Libro libro) {
        Prestamo prestamo = new Prestamo(estudiante, libro);
        prestamosActivos.add(prestamo);
    }
    public void mostrarEstado() {
        System.out.println("-------------------------------------------");
        System.out.println("Biblioteca: " + nombre);
        horario.mostrarHorario();
        System.out.println("Libros: " + libros.size());
        System.out.println("Autores: " + autores.size());
        System.out.println("Prestamos: " + prestamosActivos.size());
        System.out.println("-------------------------------------------");   
    }
    public void cerrarBiblioteca() {
        prestamosActivos.clear();
    }
}

public class Prueba {
    public static void main(String[] args) {
        Biblioteca b = new Biblioteca(" INFORMATICA UMSA ");
        Autor autor1 = new Autor("Victor Chungara Castro", "Boliviano");
        Autor autor2 = new Autor("Jorge Luis Borges", "Mexicano");
        Autor autor3 = new Autor("Lucieno Cerrati", "Peruano");
        ArrayList<Pagina> pag1 = new ArrayList<Pagina>();
        pag1.add(new Pagina(5, "Contenido pagina 5"));
        pag1.add(new Pagina(40, "Contenido pagina 40"));
        ArrayList<Pagina> pag2 = new ArrayList<Pagina>();
        pag2.add(new Pagina(1, "Contenido pagina 1"));
        pag2.add(new Pagina(2, "Contenido pagina 2"));
        ArrayList<Pagina> pag3 = new ArrayList<Pagina>();
        pag1.add(new Pagina(4, "Contenido pagina 4"));
        pag1.add(new Pagina(70, "Contenido pagina 70"));
        Libro libro1 = new Libro("Calculo ", "IUMSA-001", pag1);
        Libro libro2 = new Libro("Ficciones", "IUMSA-002", pag2);
        Libro libro3 = new Libro("novela", "IUMSA-020", pag3);
        Estudiante est1 = new Estudiante("1886004", "Alejadnra Huanca");
        Estudiante est2 = new Estudiante("1885999", "Carla Fernandes");
        b.agregarAutor(autor1);
        b.agregarAutor(autor2);
        b.agregarAutor(autor3);
        b.agregarLibro(libro1);
        b.agregarLibro(libro2);
        b.agregarLibro(libro3);
        b.prestarLibro(est1, libro1);
        b.prestarLibro(est2, libro3);
        b.mostrarEstado();
        libro1.leer();
        autor1.mostrarInfo();
  
        b.cerrarBiblioteca();
        b.mostrarEstado();
    }
}