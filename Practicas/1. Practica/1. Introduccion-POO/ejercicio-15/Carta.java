/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package Introduccion_POO;

public class Carta {
    private String codigo;
    private String remitente;
    private String destinatario;
    private String descripcion;

    // Constructor
    public Carta(String codigo, String remitente, String destinatario, String descripcion) {
        this.codigo = codigo;
        this.remitente = remitente;
        this.destinatario = destinatario;
        this.descripcion = descripcion;
    }

    public String getCodigo() {
        return codigo;
    }

    public String getRemitente() {
        return remitente;
    }

    public String getDestinatario() {
        return destinatario;
    }

    public String getDescripcion() {
        return descripcion;
    }
}