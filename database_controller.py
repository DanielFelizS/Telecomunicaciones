import pyodbc
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import tkinter.constants as tkconstants

class DatabaseController:
    def __init__(self, host, database, parent):
        self.host = host
        self.database = database
        self.parent = parent
        self.connection = None
        self.cursor = None

        self.tabla_reportes = ttk.Treeview(self.parent, show="headings", height=20)
        self.tabla_reportes.grid(row=4, column=2, columnspan=10, padx=10, pady=10)
        xscrollbar = ttk.Scrollbar(self.parent, orient=tkconstants.HORIZONTAL, command=self.tabla_reportes.xview)
        xscrollbar.grid(row=5, column=2, columnspan=10, sticky=tkconstants.EW, padx=10, pady=10)
        self.tabla_reportes.configure(xscrollcommand=xscrollbar.set)

    def connect(self):
        try:
            self.connection = pyodbc.connect(f"DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={self.host};DATABASE={self.database};Trusted_Connection=yes")
            return True
        except pyodbc.Error as e:
            messagebox.showerror("Error de conexión", str(e))
            return False

    def execute_query(self, query):
        cursor = self.connection.cursor()
        cursor.execute(query)
        rows = cursor.fetchall()
        return rows

    def get_column_names(self, table_name):
        cursor = self.connection.cursor()
        cursor.execute(f"SELECT TOP 1 * FROM {table_name}")
        columns = [column[0] for column in cursor.description]
        return columns
class GUIController:
    def __init__(self):
        self.app = tk.Tk()
        self.app.title("Administrador de Base de Datos")
        self.tabla = tk.StringVar()
        self.data_entries = []
        self.opciones = ['Empleados', 'Clientes', 'Servicios', 'Equipos', 'Facturación']
        self.combobox = ttk.Combobox(self.app, values=self.opciones)
        self.combobox.grid(column=4, row=2)
        self.combobox.bind("<<ComboboxSelected>>", self.actualizar_reporte)
        self.database_controller = DatabaseController("localhost", "Telecomunicaciones", self.app)

        self.tabla_reportes = ttk.Treeview(self.root, show="headings", height=20)
        self.tabla_reportes.grid(row=4, column=2, columnspan=10, padx=10, pady=10)
        xscrollbar = ttk.Scrollbar(self.root, orient=HORIZONTAL, command=self.tabla_reportes.xview)
        xscrollbar.grid(row=5, column=2, columnspan=10, sticky=EW, padx=10, pady=10)
        self.tabla_reportes.configure(xscrollcommand=xscrollbar.set)

    def setup(self):
        if self.check_database_connection():
            self.create_table_selector()

    def check_database_connection(self):
        if self.database_controller.connect():
            print("Conexión exitosa a la base de datos")
            return True
        else:
            print("Error al conectar a la base de datos")
            return False

    def actualizar_reporte(self, event):
        # Obtener la tabla seleccionada del combobox
        tabla_seleccionada = self.combobox.get()
        
        # Obtener los datos de la tabla seleccionada
        datos = self.database_controller.execute_query(f"SELECT * FROM {tabla_seleccionada}")
        columnas = self.database_controller.get_column_names(tabla_seleccionada)
        
        # Configurar la tabla de datos
        self.tabla_reportes.configure(columns=columnas)
        for columna in columnas:
            self.tabla_reportes.heading(columna, text=columna)
            self.tabla_reportes.column(columna, width=100)
            self.tabla_reportes.column("#0", width=0)
        self.tabla_reportes.delete(*self.tabla_reportes.get_children())
        for dato in datos:
            if isinstance(dato, (tuple, list)):
                dato_ordenado = dict(zip(columnas, dato))
            elif isinstance(dato, dict):
                dato_ordenado = dato
            else:
                continue
            valores_ordenados = [dato_ordenado[columna] for columna in columnas]
            self.tabla_reportes.insert("", 'end', values=(valores_ordenados))


