/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package javaapplication26;

public class Persona {
    private String nombre;
    private  int edad ;
    private float pesopersona ;
    public void setNombre(String nombre) {
        this.nombre = nombre;
    }

    public void setEdad(int edad) {
        this.edad = edad;
    }

    public void setPesopersona(float pesopersona) {
        this.pesopersona = pesopersona;
    }

    public String getNombre() {
        return nombre;
    }

    public int getEdad() {
        return edad;
    }

    public float getPesopersona() {
        return pesopersona;
    }
    
    public void Persona (String nombre, int edad , float peso) {
        this.nombre=nombre;
        this.edad=edad;
        this.pesopersona =pesopersona;
        
}
    
    
}
