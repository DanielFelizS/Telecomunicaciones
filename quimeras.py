import tkinter as tk
from tkinter import messagebox
from tkinter import ttk


class Empleado:
    def __init__(self, nombre, apellidos, sexo, cargo, sueldo, telefono, direccion, cedula, fecha_nac):
        self.nombre = nombre
        self.apellidos = apellidos
        self.sexo = sexo
        self.cargo = cargo
        self.sueldo = sueldo
        self.telefono = telefono
        self.direccion = direccion
        self.cedula = cedula
        self.fecha_nac = fecha_nac


class RegistroEmpleados:
    def __init__(self, app):
        self.app = app
        self.app.title('Telecomunicaciones')
        self.app.geometry("1000x1000")
        self.elementos()

    def elementos(self):
        # Frame de datosde empleado
        datos_frame = tk.Frame(self.app)
        datos_frame.pack(pady=20)

        tk.Label(datos_frame, text="Nombre").grid(
            row=0, column=0, padx=10, pady=10)
        self.nombre_var = tk.StringVar()
        tk.Entry(datos_frame, width=35, textvariable=self.nombre_var).grid(
            row=0, column=1, padx=10, pady=10)

        tk.Label(datos_frame, text="Apellidos").grid(
            row=1, column=0, padx=10, pady=10)
        self.apellidos_var = tk.StringVar()
        tk.Entry(datos_frame, width=35, textvariable=self.apellidos_var).grid(
            row=1, column=1, padx=10, pady=10)

        tk.Label(datos_frame, text="Sexo").grid(
            row=2, column=0, padx=10, pady=10)
        self.sexo_var = tk.StringVar()
        tk.Entry(datos_frame, width=35, textvariable=self.sexo_var).grid(
            row=2, column=1, padx=10, pady=10)

        tk.Label(datos_frame, text="Cargo").grid(
            row=3, column=0, padx=10, pady=10)
        self.cargo_var = tk.StringVar()
        tk.Entry(datos_frame, width=35, textvariable=self.cargo_var).grid(
            row=3, column=1, padx=10, pady=10)
        tk.Label(datos_frame, text="Sueldo").grid(
            row=4, column=0, padx=10, pady=10)
        self.sueldo_var = tk.StringVar()
        tk.Entry(datos_frame, width=35, textvariable=self.sueldo_var).grid(
        row=4, column=1, padx=10, pady=10)
        tk.Label(datos_frame, text="Teléfono").grid(
        row=5, column=0, padx=10, pady=10)
        self.telefono_var = tk.StringVar()
        tk.Entry(datos_frame, width=35, textvariable=self.telefono_var).grid(
        row=5, column=1, padx=10, pady=10)
        tk.Label(datos_frame, text="Dirección").grid(
        row=6, column=0, padx=10, pady=10)
        self.direccion_var = tk.StringVar()
        tk.Entry(datos_frame, width=35, textvariable=self.direccion_var).grid(
        row=6, column=1, padx=10, pady=10)
        tk.Label(datos_frame, text="Cédula").grid(
        row=7, column=0, padx=10, pady=10)
        self.cedula_var = tk.StringVar()
        tk.Entry(datos_frame, width=35, textvariable=self.cedula_var).grid(
        row=7, column=1, padx=10, pady=10)
        tk.Label(datos_frame, text="Fecha de nacimiento").grid(
        row=8, column=0, padx=10, pady=10)
        self.fecha_var = tk.StringVar()
        tk.Entry(datos_frame, width=35, textvariable=self.fecha_var).grid(
        row=8, column=1, padx=10, pady=10)
    # Botones de acción
        botones_frame = tk.Frame(self.app)
        botones_frame.pack()
        tk.Button(botones_frame, text="Agregar empleado", command=self.agregar_empleado).pack(side=tk.LEFT, padx=10, pady=10)
        tk.Button(botones_frame, text="Eliminar empleado", command=self.eliminar_empleado).pack(side=tk.LEFT, padx=10, pady=10)
        tk.Button(botones_frame, text="Modificar empleado", command=self.modificar_empleado).pack(side=tk.LEFT, padx=10, pady=10)
        tk.Button(botones_frame, text="Buscar empleado", command=self.buscar_empleado).pack(side=tk.LEFT, padx=10, pady=10)
    # ScrolledTreeView de empleados
        tabla_frame = tk.Frame(self.app)
        tabla_frame.pack(pady=20)
        self.tabla = ttk.Treeview(tabla_frame, columns=("Nombre", "Apellidos", "Sexo", "Cargo", "Sueldo", "Teléfono", "Dirección", "Cédula", "Fecha de nacimiento"), height=20)
        self.tabla.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        self.scrollbar = ttk.Scrollbar(tabla_frame, orient="vertical", command=self.tabla.yview)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.tabla.configure(yscrollcommand=self.scrollbar.set)


    def agregar_empleado(self):
        nombre = self.nombre_var.get()
        apellidos = self.apellidos_var.get()
        sexo = self.sexo_var.get()
        cargo = self.cargo_var.get()
        sueldo = self.sueldo_var.get()
        telefono = self.telefono_var.get()
        direccion = self.direccion_var.get()
        cedula = self.cedula_var.get()
        fecha_nac = self.fecha_var.get()

        empleado = Empleado(nombre, apellidos, sexo, cargo, sueldo, telefono, direccion, cedula, fecha_nac)

    # Insertar empleado en el TreeView
        self.tabla.insert('', tk.END, values=(empleado.nombre, empleado.apellidos, empleado.sexo, empleado.cargo,empleado.sueldo, empleado.telefono, empleado.direccion, empleado.cedula, empleado.fecha_nac))
        messagebox.showinfo("Información", "Empleado agregado correctamente")


    def eliminar_empleado(self):
    # Obtener el elemento seleccionado en el TreeView
        item = self.tabla.selection()[0]

    # Eliminar el elemento seleccionado del TreeView
        self.tabla.delete(item)

        messagebox.showinfo("Información", "Empleado eliminado correctamente")


    def modificar_empleado(self):
    # Obtener el elemento seleccionado en el TreeView
        item = self.tabla.selection()[0]

    # Actualizar los valores del elemento seleccionado en el TreeView
        self.tabla.item(item, values=(self.nombre_var.get(), self.apellidos_var.get(), self.sexo_var.get(), self.cargo_var.get(
        ), self.sueldo_var.get(), self.telefono_var.get(), self.direccion_var.get(), self.cedula_var.get(), self.fecha_var.get()))

        messagebox.showinfo("Información", "Empleado modificado correctamente")

    def buscar_empleado(self):
        nombre = self.nombre_var.get()

    # Buscar el empleado por nombre en el TreeView
        for item in self.tabla.get_children():
            if self.tabla.item(item)['values'][0] == nombre:
            # Seleccionar el elemento encontrado en el TreeView
                self.tabla.selection_set(item)
                messagebox.showinfo("Información", "Empleado encontrado")
                return

                messagebox.showwarning("Advertencia", "Empleado no encontrado")

obj = RegistroEmpleados(tk.Tk())
obj.app.mainloop()
