from tkinter import *
from tkinter import messagebox, filedialog, ttk
from PIL import Image, ImageTk
from tkcalendar import DateEntry
import empleados
import clientes
import servicios
import equipos
import facturas 
from cs import clase
from database_controller import DatabaseController
from database_controller import GUIController

class interfaz:
    def __init__(self, app):
        self.app = app
        self.app.title('Telecomunicaciones')
        self.app.geometry("{0}x{1}+0+0".format(app.winfo_screenwidth(), app.winfo_screenheight()))
        self.image_label = Label(self.app)
        self.image_label.grid(column=6, row=3, rowspan=2)
        self.elementos()
        self.empleado = []
        self.filtrar_cedula = []
        # self.mostrar_grafico_barras()
        # self.actualizar_campos()
        # self.database_controller = DatabaseController("localhost", "Telecomunicaciones")

    def actualizar_campos(self, event):
        # Obtener los valores de la fila seleccionada
        item = self.tabla_reportes.selection()[0]
        valores = self.tabla_reportes.item(item, 'values')

        # Actualizar las entradas de texto
        self.Nombre.delete(0, END)
        self.Nombre.insert(0, valores[0])
        self.Apellido.delete(0, END)
        self.Apellido.insert(0, valores[1])
        self.Cargo.delete(0, END)
        self.Cargo.insert(0, valores[2])

        # Actualizar los menús de opciones
        self.sexo_seleccion.set(valores[3])
        self.opcion_estado_civil.set(valores[4])

        # Actualizar la entrada de fecha
        fecha = datetime.strptime(valores[5], '%Y-%m-%d').date()
        self.fecha_nacimiento.set_date(fecha)

        # Enlazar el evento <<TreeviewSelect>> con la función actualizar_campos()
        self.tabla_reportes.bind("<<TreeviewSelect>>", self.actualizar_campos)

    def elementos(self):
        self.notebook = ttk.Notebook(self.app)
        self.notebook.grid(row=0, column=0, padx=10, pady=10)   
    #pestañas
        tab1 = Frame(self.notebook)
        tab2 = Frame(self.notebook)
        tab3 = Frame(self.notebook)
        tab4 = Frame(self.notebook)
        tab5 = Frame(self.notebook)
        tab6 = Frame(self.notebook)
        
        self.notebook.add(tab1, text="Empleados")
        self.notebook.add(tab2, text="Clientes")
        self.notebook.add(tab3, text="Servicios")
        self.notebook.add(tab4, text="Equipos")
        self.notebook.add(tab5, text="Facturas")
        self.notebook.add(tab6, text="Reportes")
# Empleados
        Titulo = Label(tab1, text="Gestión de Empleados", fg='#1e90ff', padx=20, pady=20)
        Titulo.grid(column=2, row=0)
        self.buscar = Entry(tab1, width=35)
        self.buscar.grid(column=4, row=0)
        self.buscar.bind("<<KeyRelease>>", self.buscar_empleado)
        label_1 = Label(tab1, text="Nombre")
        label_1.grid(column=0, row=1, padx=10, pady=10)
        self.Nombre = Entry(tab1, width=35)
        self.Nombre.grid(column=1, row=1, padx=10, pady=10)
        label_2 = Label(tab1, text="Apellidos")
        label_2.grid(column=2, row=1, padx=10, pady=10)
        self.Apellido = Entry(tab1, width=35)
        self.Apellido.grid(column=3, row=1, padx=10, pady=10)
        label_3 = Label(tab1, text="Sexo")
        label_3.grid(column=0, row=3, padx=10, pady=10)
        self.sexo_seleccion = StringVar(tab1)
        self.sexo_seleccion.set('Elija su sexo')
        self.Sexo = OptionMenu(tab1, self.sexo_seleccion, 'M', 'F')
        self.Sexo.grid(column=1, row=3, padx=10, pady=10)
        label_4 = Label(tab1, text="Cargo")
        label_4.grid(column=2, row=3, padx=10, pady=10)
        self.Cargo = Entry(tab1, width=35)
        self.Cargo.grid(column=3, row=3, padx=10, pady=10)
        label_5 = Label(tab1, text="Sueldo")
        label_5.grid(column=0, row=4, padx=10, pady=10)
        self.Sueldo = Entry(tab1, width=35)
        self.Sueldo.grid(column=1, row=4, padx=10, pady=10)
        label_6 = Label(tab1, text="Teléfono")
        label_6.grid(column=2, row=4, padx=10, pady=10)
        self.Tele = Entry(tab1, width=35)
        self.Tele.grid(column=3, row=4, padx=10, pady=10)
        label_7 = Label(tab1, text="Dirección")
        label_7.grid(column=0, row=5, padx=10, pady=10)
        self.Dire = Entry(tab1, width=35)
        self.Dire.grid(column=1, row=5, padx=10, pady=10)
        label_8 = Label(tab1, text="Cédula")
        label_8.grid(column=2, row=5, padx=10, pady=10)
        self.Cedula = Entry(tab1, width=35)
        self.Cedula.grid(column=3, row=5, padx=10, pady=10)
        label_9 = Label(tab1, text="Fecha de nacimiento")
        label_9.grid(column=0, row=6, padx=10, pady=10)
        self.Fecha_Na = DateEntry(tab1, width=35, background='darkblue', foreground='white', borderwidth=2)
        self.Fecha_Na.grid(column=1, row=6, padx=10, pady=10)
        label_10 = Label(tab1, text="Correo")
        label_10.grid(column=2, row=6, padx=10, pady=10)
        self.Correo = Entry(tab1, width=35)
        self.Correo.grid(column=3, row=6)
        label_11 = Label(tab1, text="Fecha de contratación")
        label_11.grid(column=0, row=7, padx=10, pady=10)
        self.Fecha_con = DateEntry(tab1, width=35, background='darkblue', foreground='white', borderwidth=2)
        self.Fecha_con.grid(column=1, row=7, padx=10, pady=10)
        label_12 = Label(tab1, text="Nacionalidad")
        label_12.grid(column=2, row=7, padx=10, pady=10)
        self.Nacionalidad = Entry(tab1, width=35)
        self.Nacionalidad.grid(column=3, row=7)

    # Botones
        Agregar_empleado = Button(tab1, text="Agregar empleado", command=self.agregar_empleado, padx=6, pady=6)
        Agregar_empleado.grid(column=1, row=8)
        Eliminar_empleado = Button(tab1, text="Eliminar empleado", command=self.eliminar_empleado, padx=6, pady=6)
        Eliminar_empleado.grid(column=2, row=8)
        Modificar_empleado = Button(tab1, text="Modificar empleado",command=self.actualizar_empleado, padx=6, pady=6)
        Modificar_empleado.grid(column=3, row=8)
        Buscar_empleado = Button(tab1, text="Buscar por cédula", command=self.buscar_empleado, padx=6, pady=6)
        Buscar_empleado.grid(column=6, row=0)
        # Subir_imagen_empleado = Button(tab1, text="Subir imagen", command=self.open_image, padx=6, pady=6)
        # Subir_imagen_empleado.grid(column=5, row=8)
        Ver_empleado = Button(tab1, text="Ver empleados", command = self.ver_empleado, padx=6, pady=6)
        Ver_empleado.grid(column = 4, row = 8)
        Ver_grafico = Button(tab1, text="Ver Gráfico", command= self.mostrar_grafico_barras, padx=6, pady=6)
        Ver_grafico.grid(column = 5, row = 8)
    # tabla de empleados
        self.tabla_empleados = ttk.Treeview(tab1, columns=("Id", "Nombre", "Apellidos", "Sexo", "Cargo", "Sueldo", "Teléfono", "Dirección", "Cédula", "Fecha_Na", "Correo", "Fecha_con", "Nacionalidad"), height=20)
        self.tabla_empleados.heading("Id", text="Id")
        self.tabla_empleados.heading("Nombre", text="Nombre")
        self.tabla_empleados.heading("Apellidos", text="Apellidos")
        self.tabla_empleados.heading("Sexo", text="Sexo")
        self.tabla_empleados.heading("Cargo", text="Cargo")
        self.tabla_empleados.heading("Sueldo", text="Sueldo")
        self.tabla_empleados.heading("Teléfono", text="Teléfono")
        self.tabla_empleados.heading("Dirección", text="Dirección")
        self.tabla_empleados.heading("Cédula", text="Cédula")
        self.tabla_empleados.heading("Fecha_Na", text="Fecha_Na")
        self.tabla_empleados.heading("Correo", text="Correo")
        self.tabla_empleados.heading("Fecha_con", text="Fecha_con")
        self.tabla_empleados.heading("Nacionalidad", text="Nacionalidad")
        self.tabla_empleados.grid(row=9, column=0, columnspan=10, padx=10, pady=10)
        self.tabla_empleados.column("#0", width=0, anchor = CENTER)
        self.tabla_empleados.column("Id", width=50, anchor = CENTER)
        self.tabla_empleados.column("Nombre", width=60, anchor = CENTER)
        self.tabla_empleados.column("Apellidos", width=110, anchor = CENTER)
        self.tabla_empleados.column("Sexo", width=40, anchor = CENTER)
        self.tabla_empleados.column("Cargo", width=120, anchor = CENTER)
        self.tabla_empleados.column("Sueldo", width=80, anchor = CENTER)
        self.tabla_empleados.column("Teléfono", width=80, anchor = CENTER)
        self.tabla_empleados.column("Dirección", width=150, anchor = CENTER)
        self.tabla_empleados.column("Cédula", width=110, anchor = CENTER)
        self.tabla_empleados.column("Fecha_Na", width=110, anchor = CENTER)
        self.tabla_empleados.column("Correo", width=110, anchor = CENTER)
        self.tabla_empleados.column("Fecha_con", width=110, anchor = CENTER)
        self.tabla_empleados.column("Nacionalidad", width=100, anchor = CENTER)
# Clientes
        Titulo_1 = Label(tab2, text="Gestión de Clientes", fg='#1e90ff', padx=20, pady=20)
        Titulo_1.grid(column=2, row=0)
        self.Buscar_cliente = Entry(tab2, width=35)
        self.Buscar_cliente.grid(column=4, row=0)
        label_1 = Label(tab2, text="Nombre")
        label_1.grid(column=0, row=1, padx=10, pady=10)
        self.Nombre_cliente = Entry(tab2, width=35)
        self.Nombre_cliente.grid(column=1, row=1, padx=10, pady=10)
        label_2 = Label(tab2, text="Apellidos")
        label_2.grid(column=2, row=1, padx=10, pady=10)
        self.Apellidos_cliente = Entry(tab2, width=35)
        self.Apellidos_cliente.grid(column=3, row=1, padx=10, pady=10)
        label_3 = Label(tab2, text="Sexo")
        label_3.grid(column=0, row=3, padx=10, pady=10)
        self.sexo_cliente_seleccion = StringVar(tab2)
        self.sexo_cliente_seleccion.set('Elija su sexo')
        self.Sexo_cliente = OptionMenu(tab2, self.sexo_cliente_seleccion, 'M', 'F')
        self.Sexo_cliente.grid(column=1, row=3, padx=10, pady=10)
        label_4 = Label(tab2, text="Fecha de nacimiento")
        label_4.grid(column=2, row=3, padx=10, pady=10)
        self.Fecha_cliente = DateEntry(tab2, width=35, background='darkblue', foreground='white', borderwidth=2)
        self.Fecha_cliente.grid(column=3, row=3, padx=10, pady=10)
        label_5 = Label(tab2, text="Direccion")
        label_5.grid(column=0, row=4, padx=10, pady=10)
        self.Dirección_cliente = Entry(tab2, width=35)
        self.Dirección_cliente.grid(column=1, row=4, padx=10, pady=10)
        label_6 = Label(tab2, text="Sector")
        label_6.grid(column=2, row=4, padx=10, pady=10)
        self.Sector_cliente = Entry(tab2, width=35)
        self.Sector_cliente.grid(column=3, row=4, padx=10, pady=10)
        label_7 = Label(tab2, text="Municipio")
        label_7.grid(column=0, row=5, padx=10, pady=10)
        self.Municipio_cliente_seleccion = StringVar(tab2)
        self.Municipio_cliente_seleccion.set('Elija el municipio')
        self.Municipio_cliente = OptionMenu(tab2, self.Municipio_cliente_seleccion,'Santo Domingo Norte', 'Santo Domingo Sur', 'Santo Domingo Este')
        self.Municipio_cliente.grid(column=1, row=5, padx=10, pady=10)
        label_8 = Label(tab2, text="Provincia")
        label_8.grid(column=2, row=5, padx=10, pady=10)
        self.Provincia_cliente = Entry(tab2, width=35)
        self.Provincia_cliente.grid(column=3, row=5, padx=10, pady=10)
        label_9 = Label(tab2, text="Cédula")
        label_9.grid(column=0, row=6, padx=10, pady=10)
        self.Cedula_cliente = Entry(tab2, width=35)
        self.Cedula_cliente.grid(column=1, row=6, padx=10, pady=10)
        label_10 = Label(tab2, text="Correo")
        label_10.grid(column=2, row=6, padx=10, pady=10)
        self.Correo_cliente = Entry(tab2, width=35)
        self.Correo_cliente.grid(column=3, row=6, padx=10, pady=10)
        label_11 = Label(tab2, text="Teléfono")
        label_11.grid(column=0, row=7, padx=10, pady=10)
        self.Telefono_cliente = Entry(tab2, width=35)
        self.Telefono_cliente.grid(column=1, row=7, padx=10, pady=10)
    # Botones
        Agregar_cliente = Button(tab2, text="Agregar Cliente", command=self.agregar_cliente, padx=6, pady=6)
        Agregar_cliente.grid(column=1, row=8)
        Eliminar_cliente = Button(tab2, text="Eliminar Cliente", command=self.eliminar_cliente, padx=6, pady=6)
        Eliminar_cliente.grid(column=2, row=8)
        Modificar_cliente = Button(tab2, text="Modificar Cliente", command=self.actualizar_cliente, padx=6, pady=6)
        Modificar_cliente.grid(column=3, row=8)
        Buscar_cliente = Button(tab2, text="Buscar por cédula", command=self.buscar_cliente, padx=6, pady=6)
        Buscar_cliente.grid(column=6, row=0)
        Ver_cliente = Button(tab2, text="Ver clientes", command=self.ver_cliente, padx=6, pady=6)
        Ver_cliente.grid(column=4, row=8)
    # tabla de clientes
        self.tabla_cliente = ttk.Treeview(tab2, columns=("Id", "Nombre", "Apellidos", "Sexo", "Fecha_Na","Dirección", "Sector", "Municipio", "Provincia", "Correo", "Cédula", "Teléfono"), height=20)
        self.tabla_cliente.heading("Id", text="Id")
        self.tabla_cliente.heading("Nombre", text="Nombre")
        self.tabla_cliente.heading("Apellidos", text="Apellidos")
        self.tabla_cliente.heading("Sexo", text="Sexo")
        self.tabla_cliente.heading("Fecha_Na", text="Fecha_Na")
        self.tabla_cliente.heading("Dirección", text="Dirección")
        self.tabla_cliente.heading("Sector", text="Sector")
        self.tabla_cliente.heading("Municipio", text="Municipio")
        self.tabla_cliente.heading("Provincia", text="Provincia")
        self.tabla_cliente.heading("Cédula", text="Cédula")
        self.tabla_cliente.heading("Correo", text="Correo")
        self.tabla_cliente.heading("Teléfono", text="Teléfono")
        self.tabla_cliente.grid(row=10, column=0, columnspan=10, padx=10, pady=20)
        self.tabla_cliente.column("#0", width=0, anchor = CENTER)
        self.tabla_cliente.column("Id", width=50, anchor = CENTER)
        self.tabla_cliente.column("Nombre", width=120, anchor = CENTER)
        self.tabla_cliente.column("Apellidos", width=120, anchor = CENTER)
        self.tabla_cliente.column("Sexo", width=50, anchor = CENTER)
        self.tabla_cliente.column("Fecha_Na", width=120, anchor = CENTER)
        self.tabla_cliente.column("Dirección", width=120, anchor = CENTER)
        self.tabla_cliente.column("Sector", width=120, anchor = CENTER)
        self.tabla_cliente.column("Municipio", width=100, anchor = CENTER)
        self.tabla_cliente.column("Provincia", width=100, anchor = CENTER)
        self.tabla_cliente.column("Cédula", width=140, anchor = CENTER)
        self.tabla_cliente.column("Correo", width=140, anchor = CENTER)
        self.tabla_cliente.column("Teléfono", width=100, anchor = CENTER)
# Servicios
        Titulo_servicios = Label(tab3, text="Gestión de Servicios", fg='#1e90ff', padx=20, pady=20)
        Titulo_servicios.grid(column=2, row=0)
        self.entry_buscar = Entry(tab3, width=35)
        self.entry_buscar.grid(column=4, row=0)
        label_nombre_cliente_servicios = Label(tab3, text="Nombre del cliente")
        label_nombre_cliente_servicios.grid(column=0, row=1, padx=10, pady=10)
        self.Nombre_cliente_servicios = Entry(tab3, width=35)
        self.Nombre_cliente_servicios.grid(column=1, row=1, padx=10, pady=10)
        label_nombre_empleado_servicios = Label(tab3, text="Nombre del empleado")
        label_nombre_empleado_servicios.grid(column=2, row=1, padx=10, pady=10)
        self.Nombre_empleado_servicios = Entry(tab3, width=35)
        self.Nombre_empleado_servicios.grid(column=3, row=1, padx=10, pady=10)
        label_nombre_equipo_servicios = Label(tab3, text="Nombre del equipo")
        label_nombre_equipo_servicios.grid(column=0, row=2, padx=10, pady=10)
        self.Nombre_equipos_servicios = Entry(tab3, width=35)
        self.Nombre_equipos_servicios.grid(column=1, row=2, padx=10, pady=10)
        label_nombre_servicios = Label(tab3, text="Nombre del servicio")
        label_nombre_servicios.grid(column=2, row=2, padx=10, pady=10)
        self.Nombre_servicio = Entry(tab3, width=35)
        self.Nombre_servicio.grid(column=3, row=2)
        label_descripcion_servicios = Label(tab3, text="Descripción")
        label_descripcion_servicios.grid(column=0, row=3, padx=10, pady=10)
        self.Descripción_servicio = Entry(tab3, width=35)
        self.Descripción_servicio.grid(column=1, row=3)
        label_precio_servicio = Label(tab3, text = "Precio")
        label_precio_servicio.grid(column = 2, row  = 3 )
        self.Precio_servicio = Entry(tab3, width = 35)
        self.Precio_servicio.grid(column = 3 , row = 3)
        label_tipo_plan = Label(tab3, text="Tipo de plan")
        label_tipo_plan.grid(column=0, row=4)
        self.tipo_plan_seleccion = StringVar(tab3)
        self.tipo_plan_seleccion.set('Elija un plan')
        self.Tipo_plan = OptionMenu(tab3, self.tipo_plan_seleccion, 'Móvil', 'Teléfono residencial', 'Cable/Satélite', 'Internet')
        self.Tipo_plan.grid(column=1, row=4, padx=10, pady=10)
    # Botones
        Agregar_servicio = Button(tab3, text="Agregar Servicio", command = self.agregar_servicio, padx=6, pady=6)
        Agregar_servicio.grid(column=1, row=6)
        Eliminar_servicio = Button(tab3, text="Eliminar Servicio", command = self.eliminar_servicio, padx=6, pady=6)
        Eliminar_servicio.grid(column=2, row=6)
        Modificar_servicio = Button(tab3, text="Modificar Servicio",command=self.actualizar_servicio, padx=6, pady=6)
        Modificar_servicio.grid(column=3, row=6)
        Buscar_servicio = Button(tab3, text="Buscar por cliente", command = self.buscar_servicio, padx=6, pady=6)
        Buscar_servicio.grid(column=6, row=0)
        Ver_servicio = Button(tab3, text = "Ver servicios", command = self.ver_servicio, padx = 6, pady = 6)
        Ver_servicio.grid(column = 4, row = 6)
    # tabla de servicios
        self.tabla_servicios = ttk.Treeview(tab3, columns=("Id", "Nombre_cliente", "Nombre_empleado", "Nombre_equipos", "Nombre_servicio", "Descripción", "Precio", "Tipo_plan"), height=20)
        self.tabla_servicios.heading("Id", text="Id")
        self.tabla_servicios.heading("Nombre_cliente", text="Nombre_cliente")
        self.tabla_servicios.heading("Nombre_empleado", text="Nombre_empleado")
        self.tabla_servicios.heading("Nombre_equipos", text="Nombre_equipos")
        self.tabla_servicios.heading("Nombre_servicio", text="Nombre_servicio")
        self.tabla_servicios.heading("Descripción", text="Descripción")
        self.tabla_servicios.heading("Precio", text="Precio")
        self.tabla_servicios.heading("Tipo_plan", text="Tipo_plan")
        self.tabla_servicios.grid(row=10, column=0, columnspan=10, padx=10, pady=20)
        self.tabla_servicios.column("#0", width = 0, anchor = CENTER)
        self.tabla_servicios.column("Id", width=50, anchor = CENTER)
        self.tabla_servicios.column("Nombre_cliente", width=140, anchor = CENTER)
        self.tabla_servicios.column("Nombre_empleado", width=140, anchor = CENTER)
        self.tabla_servicios.column("Nombre_equipos", width=140, anchor = CENTER)
        self.tabla_servicios.column("Nombre_servicio", width=140, anchor = CENTER)
        self.tabla_servicios.column("Descripción", width=200, anchor = CENTER)
        self.tabla_servicios.column("Precio", width=130, anchor = CENTER)
        self.tabla_servicios.column("Tipo_plan", width=200, anchor = CENTER)
# Equipos
        Titulo_equipo = Label(tab4, text="Gestión de Equipos", fg='#1e90ff', padx=20, pady=20)
        Titulo_equipo.grid(column=2, row=0)
        self.bucar_equipo = Entry(tab4, width=35)
        self.bucar_equipo.grid(column=4, row=0)
        label_tipo_equipo = Label(tab4, text="tipo")
        label_tipo_equipo.grid(column=0, row=1, padx=10, pady=10)
        self.tipo_equipo_seleccion = StringVar(tab4)
        self.tipo_equipo_seleccion.set('Elija el tipo equipo')
        self.tipo_equipo = OptionMenu(tab4, self.tipo_equipo_seleccion, 'Antena', 'Router', 'Teléfono', 'Celular')
        self.tipo_equipo.grid(column=1, row=1, padx=10, pady=10)
        label_fecha_equipo = Label(tab4, text="Fecha de fabricación")
        label_fecha_equipo.grid(column=2, row=1, padx=10, pady=10)
        self.Fecha_fabricación_equipo = DateEntry(tab4, width=35, background='darkblue', foreground='white', borderwidth=2)
        self.Fecha_fabricación_equipo.grid(column=3, row=1, padx=10, pady=10)

    # Botones
        Agregar_equipo = Button(tab4, text="Agregar Equipo", command=self.agregar_equipo, padx=6, pady=6)
        Agregar_equipo.grid(column=1, row=6)
        Eliminar_equipo = Button(tab4, text="Eliminar Equipo", command=self.eliminar_equipo, padx=6, pady=6)
        Eliminar_equipo.grid(column=2, row=6)
        Modificar_equipo = Button(tab4, text="Modificar Equipo", command=self.actualizar_equipo, padx=6, pady=6)
        Modificar_equipo.grid(column=3, row=6)
        Buscar_equipo = Button(tab4, text="Buscar Equipo", command=self.buscar_equipo, padx=6, pady=6)
        Buscar_equipo.grid(column=6, row=0)
        Ver = Button(tab4, text = "Ver Equipos", command = self.ver_equipo, padx = 6, pady = 6)
        Ver.grid(column = 4, row = 6)
    # tabla de equipos
        self.tabla_equipo = ttk.Treeview(tab4, columns=("Id", "tipo", "Fecha_fabricación"), height=20)
        self.tabla_equipo.heading("Id", text="Id")
        self.tabla_equipo.heading("tipo", text="tipo")
        self.tabla_equipo.heading("Fecha_fabricación", text="Fecha_fabricación")
        self.tabla_equipo.grid(row=10, column=1, columnspan=10, padx=10, pady=20)
        self.tabla_equipo.column("#0", width=0, anchor = CENTER)
        self.tabla_equipo.column("Id", width=40, anchor = CENTER)
        self.tabla_equipo.column("tipo", width=300, anchor = CENTER)
        self.tabla_equipo.column("Fecha_fabricación", width=300, anchor = CENTER)
# Facturación
        Titulo_Facturación = Label(tab5, text="Gestión de Facturas", fg='#1e90ff', padx=20, pady=20)
        Titulo_Facturación.grid(column=2, row=0)
        self.entry_factura_buscar = Entry(tab5, width=35)
        self.entry_factura_buscar.grid(column=4, row=0)
        label_nombre_cliente_facturas = Label(tab5, text="Nombre del cliente")
        label_nombre_cliente_facturas.grid(column=0, row=1, padx=10, pady=10)
        self.Nombre_cliente_facturas = Entry(tab5, width=35)
        self.Nombre_cliente_facturas.grid(column=1, row=1, padx=10, pady=10)
        label_nombre_empleado_facturas = Label(tab5, text="Nombre del empleado")
        label_nombre_empleado_facturas.grid(column=2, row=1, padx=10, pady=10)
        self.Nombre_empleado_facturas = Entry(tab5, width=35)
        self.Nombre_empleado_facturas.grid(column=3, row=1, padx=10, pady=10)
        label_nombre_servicios_facturas = Label(tab5, text="Nombre del servicio")
        label_nombre_servicios_facturas.grid(column=0, row=2, padx=10, pady=10)
        self.Nombre_servicios_facturas = Entry(tab5, width=35)
        self.Nombre_servicios_facturas.grid(column=1, row=2, padx=10, pady=10)
        label_nombre_equipo_facturas = Label(tab5, text="Nombre del equipo")
        label_nombre_equipo_facturas.grid(column=2, row=2, padx=10, pady=10)
        self.Nombre_equipo_facturas = Entry(tab5, width=35)
        self.Nombre_equipo_facturas.grid(column=3, row=2)
        label_fecha_factura = Label(tab5, text="Fecha de facturación")
        label_fecha_factura.grid(column=0, row=3, padx=10, pady=10)
        self.Fecha_factura = DateEntry(tab5, width=35, background='darkblue', foreground='white', borderwidth=2)
        self.Fecha_factura.grid(column=1, row=3)
        label_Descripcion = Label(tab5, text="Descripción")
        label_Descripcion.grid(column=2, row=3, padx=10, pady=10)
        self.Descripción_factura = Entry(tab5, width=35)
        self.Descripción_factura.grid(column=3, row=3)
    # Botones
        Agregar_factura = Button(tab5, text="Agregar factura", command = self.agregar_factura, padx=6, pady=6)
        Agregar_factura.grid(column=1, row=6)
        Eliminar_factura = Button(tab5, text="Eliminar factura", command = self.eliminar_factura, padx=6, pady=6)
        Eliminar_factura.grid(column=2, row=6)
        Modificar_factura = Button(tab5, text="Modificar factura", command = self.actualizar_factura, padx=6, pady=6)
        Modificar_factura.grid(column=3, row=6)
        Buscar_factura = Button(tab5, text="Buscar factura", command = self.buscar_factura, padx=6, pady=6)
        Buscar_factura.grid(column=6, row=0)
        Ver_factura = Button(tab5, text="Ver facturas", command = self.ver_facturas, padx=6, pady=6)
        Ver_factura.grid(column = 4 , row = 6)
    # tabla de factura
        self.tabla_factura = ttk.Treeview(tab5, columns=("Id", "Nombre_cliente", "Nombre_empleado", "Nombre_servicios", "Nombre_equipo", "Fecha_Facturación", "Descripción"), height=20)
        self.tabla_factura.heading("Id", text="Id")
        self.tabla_factura.heading("Nombre_cliente", text="Nombre_cliente")
        self.tabla_factura.heading("Nombre_empleado", text="Nombre_empleado")
        self.tabla_factura.heading("Nombre_servicios", text="Nombre_servicios")
        self.tabla_factura.heading("Nombre_equipo", text="Nombre_equipo")
        self.tabla_factura.heading("Fecha_Facturación", text="Fecha_Facturación")
        self.tabla_factura.heading("Descripción", text="Descripción")
        self.tabla_factura.grid(row=10, column=0, columnspan=10, padx=10, pady=10)
        self.tabla_factura.column("#0", width=0)
        self.tabla_factura.column("Id", width=50)
        self.tabla_factura.column("Nombre_cliente", width=140, anchor = CENTER)
        self.tabla_factura.column("Nombre_empleado", width=140, anchor = CENTER)
        self.tabla_factura.column("Nombre_servicios", width=140, anchor = CENTER)
        self.tabla_factura.column("Nombre_equipo", width=140, anchor = CENTER)
        self.tabla_factura.column("Fecha_Facturación", width=200, anchor = CENTER)
        self.tabla_factura.column("Descripción", width=200, anchor = CENTER)
# Reportes
        # gui_controller = GUIController()
        # gui_controller.setup()
        # gui_controller.root.mainloop()

# Funciones empleados
   # Agregar empleado
    def agregar_empleado(self):
        nombre = self.Nombre.get()
        apellidos = self.Apellido.get()
        sexo = self.sexo_seleccion.get()
        cargo = self.Cargo.get()
        sueldo = self.Sueldo.get()
        fecha_nacimiento = self.Fecha_Na.get()
        correo = self.Correo.get()
        telefono = self.Tele.get()
        cedula = self.Cedula.get()
        direccion = self.Dire.get()
        fecha_contratacion = self.Fecha_con.get()
        nacionalidad = self.Nacionalidad.get()

        empleados.agregar_empleado(nombre, apellidos, sexo, cargo, sueldo, telefono, direccion, cedula, fecha_nacimiento, correo, fecha_contratacion, nacionalidad)
        self.tabla_empleados.insert("", "end", values=(nombre, apellidos, sexo, cargo, sueldo, telefono, direccion, cedula, fecha_nacimiento, correo, fecha_contratacion, nacionalidad))

   # Eliminar empleados
    def eliminar_empleado(self):
        Cedul = self.Cedula.get()
        empleados.eliminar_empleado(Cedul)
        selection = self.tabla_empleados.selection()
        if len(selection) > 0:
            item = selection[0]
            self.tabla_empleados.delete(item)
        else:
            messagebox.showinfo("Error", "No se ha seleccionado ningún elemento.")

   # Actualizar empleados
    def actualizar_empleado(self):
        nombre = self.Nombre.get()
        apellidos = self.Apellido.get()
        sexo = self.sexo_seleccion.get()
        cargo = self.Cargo.get()
        sueldo = self.Sueldo.get()
        fecha_nacimiento = self.Fecha_Na.get()
        correo = self.Correo.get()
        telefono = self.Tele.get()
        cedula = self.Cedula.get()
        direccion = self.Dire.get()
        fecha_contratacion = self.Fecha_con.get()
        nacionalidad = self.Nacionalidad.get()

        empleados.actualizar_empleado(nombre, apellidos, sexo, cargo, sueldo, telefono, direccion, cedula, fecha_nacimiento, correo, fecha_contratacion, nacionalidad)
        item = self.tabla_empleados.selection()[0]
        self.tabla_empleados.item(item, values=(nombre, apellidos, sexo, cargo, sueldo, telefono, direccion, cedula, fecha_nacimiento, correo, fecha_contratacion, nacionalidad))

   # Buscar empleado
    def ver_empleadoss(self, empleados):
        self.tabla_empleados.delete(*self.tabla_empleados.get_children())
        for empleado in empleados:
            self.tabla_empleados.insert("", "end", values=(empleado["Id"], empleado["Nombre"], empleado["Apellido"], empleado["Sexo"], empleado["Cargo"], empleado["Sueldo"], empleado["Teléfono"], empleado["Dirección"], empleado["Cédula"], empleado["FechaNacimiento"], empleado["Correo"] , empleado["Fecha_contratación"], empleado["Nacionalidad"]))

    def buscar_empleado(self):
        # Obtener el término de búsqueda de la entrada
        termino_busqueda = self.buscar.get()
        # Buscar los empleados en la base de datos que coinciden con el término de búsqueda
        conexion = empleados.conectar()
        cursor = conexion.cursor()
        cursor.execute("SELECT Id, Nombre, Apellido, Sexo, Cargo, Sueldo, Teléfono, Dirección, Cédula, FechaNacimiento, Correo, Fecha_contratación, Nacionalidad FROM Empleados WHERE Cédula LIKE ?", f"%{termino_busqueda}%")
        rows = cursor.fetchall()

        # Crear una lista de empleados a partir de las filas devueltas por la consulta
        for row in rows:
            empleado = {"Id": row[0], "Nombre": row[1], "Apellido": row[2], "Sexo": row[3], "Cargo": row[4], "Sueldo": row[5], "Teléfono": row[6], "Dirección": row[7], "Cédula": row[8], "FechaNacimiento": row[9], "Correo": row[10], "Fecha_contratación": row[11], "Nacionalidad": row[12]}
            self.filtrar_cedula.append(empleado)
            # Mostrar los empleados filtrados en la tabla
        self.ver_empleadoss(self.filtrar_cedula)

   #Ver datos del empleado
    def ver_empleado(self):
        empleados.ver_empleado(self.tabla_empleados)

   #Seleccionar datos de un treeview y colocarlo en sus respectivos entry
    def select_empleado(self):
        nombre = self.Nombre.get()
        apellidos = self.Apellido.get()
        sexo = self.sexo_seleccion.get()
        cargo = self.Cargo.get()
        sueldo = self.Sueldo.get()
        fecha_nacimiento = self.Fecha_Na.get()
        correo = self.Correo.get()
        telefono = self.Tele.get()
        cedula = self.Cedula.get()
        direccion = self.Dire.get()
        fecha_contratacion = self.Fecha_con.get()
        nacionalidad = self.Nacionalidad.get()

        selected_item = tabla_empleados.selection()[0]
        values = tabla_empleados.item(selected_item)['values']
        nombre.delete(0, END)
        nombre.insert(0, values[0])
        apellidos.delete(0, END)
        apellidos.insert(0, values[1])
        sexo.delete(0, END)
        sexo.insert(0, values[2])
        cargo.delete(0, END)
        cargo.insert(0, values[3])
        sueldo.delete(0, END)
        sueldo.insert(0, values[4])
        fecha_nacimiento.delete(0, END)
        fecha_nacimiento.insert(0, values[5])
        correo.delete(0, END)
        correo.insert(0, values[6])
        telefono.delete(0, END)
        telefono.insert(0, values[7])
        cedula.delete(0, END)
        cedula.insert(0, values[8])
        direccion.delete(0, END)
        direccion.insert(0, values[9])
        fecha_contratacion.delete(0, END)
        fecha_contratacion.insert(0, values[10])
        nacionalidad.delete(0, END)
        nacionalidad.insert(0, values[11])

# Funciones clientes
   # Agregar cliente
    def agregar_cliente(self):
        Nombre = self.Nombre_cliente.get()
        Apellidos = self.Apellidos_cliente.get()
        Sexo = self.sexo_cliente_seleccion.get()
        Fecha_Na = self.Fecha_cliente.get()
        Correo = self.Correo_cliente.get()
        Tele = self.Telefono_cliente.get()
        Cedula = self.Cedula_cliente.get()
        Dire = self.Dirección_cliente.get()
        Sector = self.Sector_cliente.get()
        Provincia = self.Provincia_cliente.get()
        Municipio = self.Municipio_cliente_seleccion.get()

        clientes.agregar_cliente(Nombre, Apellidos, Sexo, Fecha_Na, Dire, Sector, Municipio, Provincia, Cedula, Correo, Tele)
        self.tabla_cliente.insert("", "end", values=(Nombre, Apellidos, Sexo, Fecha_Na, Dire, Sector, Municipio, Provincia, Cedula, Correo, Tele))

   # Eliminar clientes
    def eliminar_cliente(self):
        Cedul = self.Cedula.get()
        clientes.eliminar_cliente(Cedul)
        item = self.tabla_cliente.selection()[0]
        self.tabla_cliente.delete(item)

   # Actualizar clientes
    def actualizar_cliente(self):
        Nombre = self.Nombre_cliente.get()
        Apellidos = self.Apellidos_cliente.get()
        Sexo = self.sexo_cliente_seleccion.get()
        Fecha_Na = self.Fecha_cliente.get()
        Correo = self.Correo_cliente.get()
        Tele = self.Telefono_cliente.get()
        Cedula = self.Cedula_cliente.get()
        Dire = self.Dirección_cliente.get()
        Sector = self.Sector_cliente.get()
        Provincia = self.Provincia_cliente.get()
        Municipio = self.Municipio_cliente_seleccion.get()

        clientes.actualizar_cliente(Nombre, Apellidos, Sexo, Fecha_Na, Dire, Sector, Municipio, Provincia, Cedula, Correo, Tele)
        item = self.tabla_cliente.selection()[0]
        self.tabla_cliente.item(item, values=(Nombre, Apellidos, Sexo, Fecha_Na, Dire, Sector, Municipio, Provincia, Cedula, Correo, Tele))

   # Buscar cliente
    def buscar_cliente(self):
        Cedula = self.Cedula_cliente.get()
        clientes.buscar_cliente(Cedula, self.tabla_clientes)

   #Ver datos del cliente
    def ver_cliente(self):
        clientes.ver_cliente(self.tabla_cliente)

# Funciones Servicios
   # Agregar servicio
    def agregar_servicio(self):
        Cliente = self.Nombre_cliente_servicios.get()
        Empleado = self.Nombre_empleado_servicios.get()
        Equipos = self.Nombre_equipos_servicios.get()
        Nombre_servicio = self.Nombre_servicio.get()
        Descripcion = self.Descripción_servicio.get()
        Precio = self.Precio_servicio.get()
        Tipo_plan = self.tipo_plan_seleccion.get()
        servicios.agregar_servicio(Cliente, Empleado, Equipos, Nombre_servicio, Descripcion, Precio, Tipo_plan)
        self.tabla_servicios.insert("", "end", values=(Cliente, Empleado, Equipos, Nombre_servicio, Descripcion, Precio, Tipo_plan))

   # Eliminar servicios
    def eliminar_servicio(self):
        Cliente = self.Nombre_cliente_servicios.get()
        servicios.eliminar_servicio(Cliente)
        item = self.tabla_servicios.selection()[0]
        self.tabla_servicios.delete(item)

   # Actualizar servicios
    def actualizar_servicio(self):
        Cliente = self.Nombre_cliente_servicios.get()
        Empleado = self.Nombre_empleado_servicios.get()
        Equipos = self.Nombre_equipos_servicios.get()
        Nombre_servicio = self.Nombre_servicio.get()
        Descripcion = self.Descripción_servicio.get()
        Precio = self.Precio_servicio.get()
        Tipo_plan = self.tipo_plan_seleccion.get()
        servicios.actualizar_servicio(Cliente, Empleado, Equipos, Nombre_servicio, Descripcion, Precio, Tipo_plan)
        item = self.tabla_servicios.selection()[0]
        self.tabla_servicios.item(item, values=(Cliente, Empleado, Equipos, Nombre_servicio, Descripcion, Precio, Tipo_plan))

   # Buscar servicio
    def buscar_servicio(self):
        Nombre = self.Nombre_cliente_servicios.get()
        servicios.buscar_servicio(Nombre, self.tabla_servicios)

   # Ver Servicios
    def ver_servicio(self):
        servicios.ver_servicio(self.tabla_servicios)

# Funciones Equipos
   # Agregar Equipos
    def agregar_equipo(self):
        TipoEquipo = self.tipo_equipo_seleccion.get()
        Fecha = self.Fecha_fabricación_equipo.get()
        equipos.agregar_equipo(TipoEquipo, Fecha)
        self.tabla_equipo.insert("", "end", values=(TipoEquipo, Fecha))

   # Eliminar Equipos
    def eliminar_equipo(self):
        Fecha = self.Fecha_fabricación_equipo.get()
        equipos.eliminar_equipo(Fecha)
        item = self.tabla_equipo.selection()[0]
        self.tabla_equipo.delete(item)

   # Actualizar Equipos
    def actualizar_equipo(self):
        TipoEquipo = self.tipo_equipo_seleccion.get()
        Fecha = self.Fecha_fabricación_equipo.get()
        equipos.actualizar_equipo(TipoEquipo, Fecha)
        item = self.tabla_equipo.selection()[0]
        self.tabla_equipo.item(item, values=(TipoEquipo, Fecha))

   # Buscar Equipo
    def buscar_equipo(self):
        Fecha = self.Fecha_fabricación_equipo.get()
        equipos.buscar_equipo(Fecha, self.tabla_equipo)

   # Ver datos de los equipos
    def ver_equipo(self):
        equipos.ver_equipo(self.tabla_equipo)

# Funciones Facturas
   # Agregar Factura
    def agregar_factura(self):
        Cliente = self.Nombre_cliente_facturas.get()
        Empleado = self.Nombre_empleado_facturas.get()
        Servicio = self.Nombre_servicios_facturas.get()
        Equipo = self.Nombre_equipo_facturas.get()
        Fecha = self.Fecha_factura.get()
        Descripcion = self.Descripción_factura.get()
        facturas.agregar_factura(Cliente, Empleado, Servicio, Equipo, Fecha, Descripcion)
        self.tabla_factura.insert("", "end", values=(Cliente, Empleado, Servicio, Equipo, Fecha, Descripcion))

   # Eliminar Factura
    def eliminar_factura(self):
        cliente = self.Nombre_cliente_facturas.get()
        facturas.eliminar_factura(cliente)
        item = self.tabla_factura.selection()[0]
        self.tabla_factura.delete(item)

   # Actualizar Factura
    def actualizar_factura(self):
        Cliente = self.Nombre_cliente_facturas.get()
        Empleado = self.Nombre_empleado_facturas.get()
        Servicio = self.Nombre_servicios_facturas.get()
        Equipo = self.Nombre_equipo_facturas.get()
        Fecha = self.Fecha_factura.get()
        Descripcion = self.Descripción_factura.get()
        facturas.actualizar_factura(Cliente, Empleado, Servicio, Equipo, Fecha, Descripcion)
        item = self.tabla_factura.selection()[0]
        self.tabla_factura.item(item, values=(Cliente, Empleado, Servicio, Equipo, Fecha, Descripcion))

   # Buscar Factura
    def buscar_factura(self):
        Cliente = self.Nombre_cliente_facturas.get()
        facturas.buscar_equipo(Cliente, self.tabla_factura)

   # Ver datos de las facturas
    def ver_facturas(self):
        facturas.ver_facturas(self.tabla_factura)

# subir imagen
    def open_image(self):
        filename = filedialog.askopenfilename(initialdir="/", title="Select file", filetypes=(("jpeg files", "*.jpg"), ("all files", "*.*")))
        imagen = Image.open(filename)
        ancho_actual, alto_actual = imagen.size
        nuevo_tamaño = (ancho_actual // 2, alto_actual // 2)
        imagen_redimensionada = imagen.resize(nuevo_tamaño)
        photo = PhotoImage(imagen_redimensionada)
        self.image_label.config(image=photo)
        self.image_label.image = photo

# Ver grafico de barras
    def mostrar_grafico_barras(self):
        ventana = Toplevel(self.app)
        cs = clase(ventana)
        ventana.mainloop()

obj = interfaz(Tk())
obj.app.mainloop()