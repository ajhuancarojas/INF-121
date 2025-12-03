import tkinter as tk
from tkinter import messagebox, Toplevel, simpledialog, scrolledtext
from datetime import date

class Pagina:

    def __init__(self, numero, contenido):
        self.numero = numero
        self.contenido = contenido

    def mostrar_pagina(self):
        return f"Página {self.numero}: {self.contenido}"


class Libro:

    def __init__(self, titulo, isbn, paginas_contenido):
        self.titulo = titulo
        self.isbn = isbn

        self.paginas = [Pagina(i + 1, contenido) for i, contenido in enumerate(paginas_contenido)]

    def leer(self):
        return [p.mostrar_pagina() for p in self.paginas]


class Autor:

    def __init__(self, nombre, nacionalidad):
        self.nombre = nombre
        self.nacionalidad = nacionalidad

    def mostrar_info(self):
        return f"Autor: {self.nombre} ({self.nacionalidad})"


class Estudiante:

    def __init__(self, codigo, nombre):
        self.codigo = codigo
        self.nombre = nombre

    def mostrar_info(self):
        return f"Estudiante: {self.nombre} (Código: {self.codigo})"


class Prestamo:

    def __init__(self, estudiante, libro):
        self.estudiante = estudiante
        self.libro = libro
        self.fecha_prestamo = date.today()
        self.fecha_devolucion = None

    def devolver(self):
        self.fecha_devolucion = date.today()

    def esta_devuelto(self):
        return self.fecha_devolucion is not None

    def mostrar_info(self):
        return (
            f"{self.libro.titulo} - {self.estudiante.nombre} - "
            f"Prestado: {self.fecha_prestamo} - "
            f"Devolución: {self.fecha_devolucion if self.fecha_devolucion else 'No devuelto'}"
        )


class Horario:
    def __init__(self, dias_apertura, hora_apertura, hora_cierre):
        self.dias_apertura = dias_apertura
        self.hora_apertura = hora_apertura
        self.hora_cierre = hora_cierre

    def mostrar_horario(self):
        return f"{self.dias_apertura}, de {self.hora_apertura} a {self.hora_cierre}"


class Biblioteca:

    def __init__(self, nombre):
        self.nombre = nombre
        self.libros = []
        self.autores = []
        self.prestamos = []
        self.horario = Horario("Lunes a Viernes", "08:00", "18:00")

    def agregar_libro(self, libro):
        self.libros.append(libro)

    def agregar_autor(self, autor):
        self.autores.append(autor)

    def prestar_libro(self, estudiante, libro):

        for p in self.prestamos:
            if p.libro == libro and not p.esta_devuelto():
                return False
        prest = Prestamo(estudiante, libro)
        self.prestamos.append(prest)
        return True

    def devolver_libro(self, libro):
        for prestamo in self.prestamos:
            if prestamo.libro == libro and not prestamo.esta_devuelto():
                prestamo.devolver()
                return True
        return False

    def prestamos_activos(self):
        return [p for p in self.prestamos if not p.esta_devuelto()]

    def mostrar_estado(self):
        estado = f"Biblioteca '{self.nombre}'\n"
        estado += "Horario: " + self.horario.mostrar_horario() + "\n\n"
        estado += "Libros disponibles:\n"
        for libro in self.libros:
            estado += f" - {libro.titulo} (ISBN: {libro.isbn})\n"
        estado += "\nPréstamos (activos):\n"
        activos = self.prestamos_activos()
        if not activos:
            estado += " No hay préstamos activos.\n"
        else:
            for p in activos:
                estado += " " + p.mostrar_info() + "\n"
        return estado

    def cerrar_biblioteca(self):

        self.prestamos.clear()
        return "La biblioteca se ha cerrado. NO HAY  préstamos han sido finalizados."


# ------------------ INTERFAZ GRÁFICA (Tkinter) ------------------

class BibliotecaApp:
    def __init__(self, root, biblioteca):
        self.root = root
        self.biblioteca = biblioteca
        self.root.title("Biblioteca UMSA")
        self.root.geometry("700x520")
        self.root.configure(bg="#E9EEF6")

        self.center_window(700, 520)

        titulo = tk.Label(root, text="Biblioteca UMSA",
                          font=("Arial", 22, "bold"),
                         bg="#E9EEF6", fg="#800000")
        titulo.pack(pady=20)

        # MARCO DEL MENÚ CENTRAL
        menu_frame = tk.Frame(root, bg="#E9EEF6")
        menu_frame.pack(pady=10)

        style_btn = {
            "bg": "#34495E", "fg": "white",
            "font": ("Arial", 12),
            "width": 22, "height": 2,
            "bd": 0, "activebackground": "#1ABC9C"
        }

        botones = [
            ("Biblioteca", self.mostrar_estado),
            ("Autor", self.ventana_autor),
            ("Libro", self.ventana_libro),
            ("Estudiante", self.ventana_estudiante),
            ("Página", self.ventana_pagina),
            ("Horario", self.ventana_horario),
            ("Préstamo", self.ventana_prestamo),
            ("Devolver Libro", self.ventana_devolver),
            ("Leer Libro", self.ventana_leer_libro),
            ("Cerrar Biblioteca", self.ventana_cerrar_biblioteca),
        ]

        # organizar botones en dos columnas para mejor aspecto
        left_col = tk.Frame(menu_frame, bg="#E9EEF6")
        right_col = tk.Frame(menu_frame, bg="#E9EEF6")
        left_col.grid(row=0, column=0, padx=10)
        right_col.grid(row=0, column=1, padx=10)

        for i, (texto, comando) in enumerate(botones):
            col = left_col if i % 2 == 0 else right_col
            tk.Button(col, text=texto, command=comando, **style_btn).pack(pady=6)

        # AREA INFERIOR: Lista de libros (resumen rápido)
        footer = tk.Frame(root, bg="#E9EEF6")
        footer.pack(fill="both", expand=True, pady=8)
        tk.Label(footer, text="Lista de Libros Disponibles:", bg="#E9EEF6",
                 font=("Arial", 12, "bold")).pack(anchor="nw", padx=14)
        list_frame = tk.Frame(footer, bg="#E9EEF6")
        list_frame.pack(padx=14, pady=6, anchor="nw")

        scrollbar = tk.Scrollbar(list_frame)
        scrollbar.pack(side="right", fill="y")

        self.libros_listbox = tk.Listbox(
            list_frame, width=60, height=6,
            font=("Arial", 11), yscrollcommand=scrollbar.set
        )
        self.libros_listbox.pack()
        scrollbar.config(command=self.libros_listbox.yview)

        self.actualizar_libros_listbox()

    def center_window(self, w, h):
        # posicion aproximada centrada
        ws = self.root.winfo_screenwidth()
        hs = self.root.winfo_screenheight()
        x = (ws // 2) - (w // 2)
        y = (hs // 2) - (h // 2)
        self.root.geometry(f"{w}x{h}+{x}+{y}")

    # ---------- FUNCIONES DE INTERFAZ Y UTILIDADES ----------
    def actualizar_libros_listbox(self):
        self.libros_listbox.delete(0, tk.END)
        for libro in self.biblioteca.libros:
            self.libros_listbox.insert(tk.END, f"{libro.titulo}  |  ISBN: {libro.isbn}")

    def mostrar_estado(self):
        messagebox.showinfo("Estado de la Biblioteca", self.biblioteca.mostrar_estado())

    # ------------------ VENTANAS: AUTORES ------------------
    def ventana_autor(self):
        win = Toplevel(self.root)
        win.title("Autores - Biblioteca UMSA")
        win.geometry("420x420")
        win.configure(bg="#DDE6F2")

        tk.Label(win, text="Autores registrados", font=("Arial", 14, "bold"), bg="#DDE6F2").pack(pady=12)

        lista = tk.Listbox(win, width=48, height=10, font=("Arial", 11))
        lista.pack(pady=8)
        for a in self.biblioteca.autores:
            lista.insert(tk.END, f"{a.nombre} ({a.nacionalidad})")

        # agregar autor
        def agregar_autor():
            nombre = simpledialog.askstring("Nombre", "Nombre del autor:", parent=win)
            if not nombre:
                return
            nacionalidad = simpledialog.askstring("Nacionalidad", "Nacionalidad:", parent=win)
            if not nacionalidad:
                return
            autor = Autor(nombre, nacionalidad)
            self.biblioteca.agregar_autor(autor)
            lista.insert(tk.END, f"{autor.nombre} ({autor.nacionalidad})")
            messagebox.showinfo("Listo", f"Autor {autor.nombre} agregado.")

        tk.Button(win, text="Agregar Autor", bg="#34495E", fg="white",
                  font=("Arial", 12), width=18, command=agregar_autor).pack(pady=10)

    # ------------------ VENTANAS: LIBROS ------------------
    def ventana_libro(self):
        win = Toplevel(self.root)
        win.title("Libros - Biblioteca UMSA")
        win.geometry("520x520")
        win.configure(bg="#DDE6F2")

        tk.Label(win, text="Libros registrados", font=("Arial", 14, "bold"), bg="#DDE6F2").pack(pady=10)

        lista = tk.Listbox(win, width=60, height=10, font=("Arial", 11))
        lista.pack(pady=6)
        for libro in self.biblioteca.libros:
            lista.insert(tk.END, f"{libro.titulo}  |  ISBN: {libro.isbn}")

        # área para agregar libro
        tk.Label(win, text="Agregar nuevo libro", font=("Arial", 13, "bold"), bg="#DDE6F2").pack(pady=8)
        form = tk.Frame(win, bg="#DDE6F2")
        form.pack(pady=6)

        tk.Label(form, text="Título:", bg="#DDE6F2").grid(row=0, column=0, sticky="w")
        title_entry = tk.Entry(form, width=40, font=("Arial", 11))
        title_entry.grid(row=0, column=1, pady=4)

        tk.Label(form, text="ISBN:", bg="#DDE6F2").grid(row=1, column=0, sticky="w")
        isbn_entry = tk.Entry(form, width=40, font=("Arial", 11))
        isbn_entry.grid(row=1, column=1, pady=4)

        tk.Label(win, text="Contenido de páginas (una página por línea):", bg="#DDE6F2").pack(pady=6)
        paginas_text = scrolledtext.ScrolledText(win, width=60, height=8, font=("Arial", 11))
        paginas_text.pack(pady=4)

        def agregar_libro():
            titulo = title_entry.get().strip()
            isbn = isbn_entry.get().strip()
            contenido = paginas_text.get("1.0", tk.END).strip().splitlines()
            contenido = [c.strip() for c in contenido if c.strip()]
            if not titulo or not isbn or not contenido:
                return messagebox.showwarning("Error", "Completa título, ISBN y al menos una página.")
            nuevo = Libro(titulo, isbn, contenido)
            self.biblioteca.agregar_libro(nuevo)
            lista.insert(tk.END, f"{nuevo.titulo}  |  ISBN: {nuevo.isbn}")
            self.actualizar_libros_listbox()
            title_entry.delete(0, tk.END)
            isbn_entry.delete(0, tk.END)
            paginas_text.delete("1.0", tk.END)
            messagebox.showinfo("Listo", f"Libro '{nuevo.titulo}' agregado.")

        tk.Button(win, text="Agregar Libro", bg="#34495E", fg="white",
                  font=("Arial", 12), width=18, command=agregar_libro).pack(pady=10)

    # ------------------ VENTANAS: ESTUDIANTES ------------------
    def ventana_estudiante(self):
        win = Toplevel(self.root)
        win.title("Estudiantes - Biblioteca UMSA")
        win.geometry("420x380")
        win.configure(bg="#DDE6F2")

        tk.Label(win, text="Registrar Estudiante", font=("Arial", 14, "bold"), bg="#DDE6F2").pack(pady=12)

        tk.Label(win, text="Nombre:", bg="#DDE6F2").pack()
        nombre_entry = tk.Entry(win, width=40, font=("Arial", 11))
        nombre_entry.pack(pady=4)

        tk.Label(win, text="Código:", bg="#DDE6F2").pack()
        codigo_entry = tk.Entry(win, width=40, font=("Arial", 11))
        codigo_entry.pack(pady=4)

        def registrar_estudiante():
            nombre = nombre_entry.get().strip()
            codigo = codigo_entry.get().strip()
            if not nombre or not codigo:
                return messagebox.showwarning("Error", "Completa nombre y código.")
            est = Estudiante(codigo, nombre)
            messagebox.showinfo("Listo", f"Estudiante {est.nombre} registrado (temporal).")
            win.destroy()

        tk.Button(win, text="Registrar", bg="#34495E", fg="white",
                  font=("Arial", 12), width=16, command=registrar_estudiante).pack(pady=12)

        # Mostrar préstamos actuales (informativo)
        tk.Label(win, text="Préstamos activos (resumen):", font=("Arial", 12, "bold"), bg="#DDE6F2").pack(pady=6)
        lista = tk.Listbox(win, width=55, height=6, font=("Arial", 10))
        lista.pack(pady=4)
        for p in self.biblioteca.prestamos_activos():
            lista.insert(tk.END, p.mostrar_info())

    # ------------------ VENTANA: PÁGINAS ------------------
    def ventana_pagina(self):
        win = Toplevel(self.root)
        win.title("Páginas - Biblioteca UMSA")
        win.geometry("520x420")
        win.configure(bg="#DDE6F2")

        tk.Label(win, text="Selecciona un libro para ver sus páginas", font=("Arial", 13, "bold"), bg="#DDE6F2").pack(pady=12)
        lista = tk.Listbox(win, width=60, height=10, font=("Arial", 11))
        lista.pack(pady=6)
        for libro in self.biblioteca.libros:
            lista.insert(tk.END, f"{libro.titulo}  |  ISBN: {libro.isbn}")

        def ver_paginas():
            idx = lista.curselection()
            if not idx:
                return messagebox.showwarning("Error", "Selecciona un libro.")
            libro = self.biblioteca.libros[idx[0]]
            paginas = "\n".join(libro.leer())
            # Mostrar en ventana con scrollbar
            pv = Toplevel(win)
            pv.title(f"Páginas - {libro.titulo}")
            pv.geometry("520x420")
            pv.configure(bg="#F7F9FC")
            txt = scrolledtext.ScrolledText(pv, width=70, height=25, font=("Arial", 11))
            txt.pack(padx=8, pady=8)
            txt.insert(tk.END, paginas)
            txt.config(state="disabled")

        tk.Button(win, text="Ver Páginas", bg="#34495E", fg="white",
                  font=("Arial", 12), width=16, command=ver_paginas).pack(pady=12)

    # ------------------ VENTANA: HORARIO ------------------
    def ventana_horario(self):
        win = Toplevel(self.root)
        win.title("Horario - Biblioteca UMSA")
        win.geometry("420x280")
        win.configure(bg="#DDE6F2")

        tk.Label(win, text="Horario Actual", font=("Arial", 14, "bold"), bg="#DDE6F2").pack(pady=10)
        horario_label = tk.Label(win, text=self.biblioteca.horario.mostrar_horario(),
                                 font=("Arial", 12), bg="#DDE6F2")
        horario_label.pack(pady=8)

        tk.Label(win, text="Editar horario (opcional):", font=("Arial", 12), bg="#DDE6F2").pack(pady=6)
        dias_entry = tk.Entry(win, width=36, font=("Arial", 11))
        dias_entry.insert(0, self.biblioteca.horario.dias_apertura)
        dias_entry.pack(pady=2)
        apertura_entry = tk.Entry(win, width=36, font=("Arial", 11))
        apertura_entry.insert(0, self.biblioteca.horario.hora_apertura)
        apertura_entry.pack(pady=2)
        cierre_entry = tk.Entry(win, width=36, font=("Arial", 11))
        cierre_entry.insert(0, self.biblioteca.horario.hora_cierre)
        cierre_entry.pack(pady=2)

        def guardar_horario():
            dias = dias_entry.get().strip()
            ap = apertura_entry.get().strip()
            ci = cierre_entry.get().strip()
            if not dias or not ap or not ci:
                return messagebox.showwarning("Error", "Completa todos los campos del horario.")
            # Reemplazamos el objeto horario (composición) por uno nuevo
            self.biblioteca.horario = Horario(dias, ap, ci)
            horario_label.config(text=self.biblioteca.horario.mostrar_horario())
            messagebox.showinfo("Listo", "Horario actualizado.")

        tk.Button(win, text="Guardar Horario", bg="#34495E", fg="white",
                  font=("Arial", 12), width=18, command=guardar_horario).pack(pady=10)

    # ------------------ VENTANA: PRESTAMO ------------------
    def ventana_prestamo(self):
        win = Toplevel(self.root)
        win.title("Prestar Libro - Biblioteca UMSA")
        win.geometry("520x460")
        win.configure(bg="#DDE6F2")

        tk.Label(win, text="Registrar un préstamo", font=("Arial", 14, "bold"), bg="#DDE6F2").pack(pady=10)

        tk.Label(win, text="Nombre del estudiante:", bg="#DDE6F2").pack(pady=4)
        nombre_entry = tk.Entry(win, width=40, font=("Arial", 11))
        nombre_entry.pack()

        tk.Label(win, text="Código del estudiante:", bg="#DDE6F2").pack(pady=6)
        codigo_entry = tk.Entry(win, width=40, font=("Arial", 11))
        codigo_entry.pack()

        tk.Label(win, text="Selecciona un libro:", bg="#DDE6F2").pack(pady=8)
        lb_frame = tk.Frame(win, bg="#DDE6F2")
        lb_frame.pack()
        lista = tk.Listbox(lb_frame, width=58, height=8, font=("Arial", 11))
        lista.pack(side="left")
        sb = tk.Scrollbar(lb_frame, orient="vertical")
        sb.pack(side="right", fill="y")
        lista.config(yscrollcommand=sb.set)
        sb.config(command=lista.yview)
        for libro in self.biblioteca.libros:
            lista.insert(tk.END, f"{libro.titulo}  |  ISBN: {libro.isbn}")

        def confirmar_prestamo():
            nombre = nombre_entry.get().strip()
            codigo = codigo_entry.get().strip()
            if not nombre or not codigo:
                return messagebox.showwarning("Error", "Completa nombre y código del estudiante.")
            idx = lista.curselection()
            if not idx:
                return messagebox.showwarning("Error", "Selecciona un libro.")
            libro = self.biblioteca.libros[idx[0]]
            est = Estudiante(codigo, nombre)
            ok = self.biblioteca.prestar_libro(est, libro)
            if not ok:
                return messagebox.showerror("No disponible", f"El libro '{libro.titulo}' ya está prestado.")
            messagebox.showinfo("Éxito", f"Libro '{libro.titulo}' prestado a {est.nombre}.")
            self.actualizar_libros_listbox()
            win.destroy()

        tk.Button(win, text="Confirmar Préstamo", bg="#34495E", fg="white",
                  font=("Arial", 12), width=20, command=confirmar_prestamo).pack(pady=12)

    # ------------------ VENTANA: DEVOLVER ------------------
    def ventana_devolver(self):
        activos = self.biblioteca.prestamos_activos()
        if not activos:
            return messagebox.showinfo("No hay préstamos", "No existen libros prestados actualmente.")
        win = Toplevel(self.root)
        win.title("Devolver Libro - Biblioteca UMSA")
        win.geometry("520x420")
        win.configure(bg="#DDE6F2")

        tk.Label(win, text="Seleccione préstamo a devolver", font=("Arial", 14, "bold"), bg="#DDE6F2").pack(pady=10)
        lista = tk.Listbox(win, width=70, height=12, font=("Arial", 11))
        lista.pack(pady=6)
        for p in activos:
            lista.insert(tk.END, f"{p.libro.titulo}  →  {p.estudiante.nombre}  (Prestado: {p.fecha_prestamo})")

        def devolver_seleccionado():
            idx = lista.curselection()
            if not idx:
                return messagebox.showwarning("Error", "Selecciona un préstamo.")
            prestamo = activos[idx[0]]
            self.biblioteca.devolver_libro(prestamo.libro)
            messagebox.showinfo("Devuelto", f"El libro '{prestamo.libro.titulo}' ha sido devuelto.")
            self.actualizar_libros_listbox()
            win.destroy()

        tk.Button(win, text="Devolver", bg="#1ABC9C", fg="white",
                  font=("Arial", 12), width=18, command=devolver_seleccionado).pack(pady=10)

    # ------------------ VENTANA: LEER LIBRO ------------------
    def ventana_leer_libro(self):
        win = Toplevel(self.root)
        win.title("Leer Libro - Biblioteca UMSA")
        win.geometry("520x420")
        win.configure(bg="#DDE6F2")

        tk.Label(win, text="Selecciona un libro para leer", font=("Arial", 13, "bold"), bg="#DDE6F2").pack(pady=12)
        lista = tk.Listbox(win, width=60, height=10, font=("Arial", 11))
        lista.pack(pady=6)
        for libro in self.biblioteca.libros:
            lista.insert(tk.END, f"{libro.titulo}  |  ISBN: {libro.isbn}")

        def leer_seleccionado():
            idx = lista.curselection()
            if not idx:
                return messagebox.showwarning("Error", "Selecciona un libro.")
            libro = self.biblioteca.libros[idx[0]]
            paginas = "\n".join(libro.leer())
            pv = Toplevel(win)
            pv.title(f"Leyendo: {libro.titulo}")
            pv.geometry("520x420")
            pv.configure(bg="#F7F9FC")
            txt = scrolledtext.ScrolledText(pv, width=70, height=25, font=("Arial", 11))
            txt.pack(padx=8, pady=8)
            txt.insert(tk.END, paginas)
            txt.config(state="disabled")

        tk.Button(win, text="Leer", bg="#34495E", fg="white",
                  font=("Arial", 12), width=16, command=leer_seleccionado).pack(pady=12)

    # ------------------ VENTANA: CERRAR BIBLIOTECA ------------------
    def ventana_cerrar_biblioteca(self):
        resp = messagebox.askyesno("Cerrar Biblioteca",
                                   "¿Estás segura/o que deseas cerrar la biblioteca?\nEsto finalizará todos los préstamos.")
        if not resp:
            return
        resultado = self.biblioteca.cerrar_biblioteca()
        self.actualizar_libros_listbox()
        messagebox.showinfo("Cerrada", resultado)

# ------------------ DATOS INICIALES Y ARRANQUE ------------------

def crear_datos_demo(biblioteca):
    # Autores demo (agregación)
    autores = [
        ("Gabriel García Márquez", "Colombiano"),
        ("Julio Cortázar", "Argentino"),
        ("Isabel Allende", "Chilena"),
        ("Mario Vargas Llosa", "Peruano"),
    ]
    for n, nat in autores:
        biblioteca.agregar_autor(Autor(n, nat))

    # Libros demo (cada uno crea sus Páginas - composición)
    biblioteca.agregar_libro(Libro("Cien Años de Soledad", "123-ABC",
                                   ["Prólogo: La familia Buendía",
                                    "Capítulo 1: José Arcadio Buendía y la fundación de Macondo",
                                    "Capítulo 2: La historia de Aureliano Buendía"]))
    biblioteca.agregar_libro(Libro("Rayuela", "456-XYZ",
                                   ["Capítulo 1: Del lado de allá",
                                    "Capítulo 2: Del lado de acá",
                                    "Capítulo 3: La Maga y Horacio"]))
    biblioteca.agregar_libro(Libro("La casa de los espíritus", "789-DEF",
                                   ["Capítulo 1: Los Trueba",
                                    "Capítulo 2: Esteban y Clara"]))

root = tk.Tk()
biblioteca = Biblioteca("Biblioteca Central UMSA")
crear_datos_demo(biblioteca)
app = BibliotecaApp(root, biblioteca)
root.mainloop()
