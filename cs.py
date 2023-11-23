from tkinter import *
import pyodbc
import pandas as pd
from pandastable import *
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
class clase:
    def __init__(self, root):
        self.root = root 
        self.root.title("Tabla de resultados del JOIN")
        self.elementos()

    def elementos(self):
        # Conectarse a la base de datos
        conn = pyodbc.connect('DRIVER={SQL Server};SERVER=DESKTOP-HIESJ07;DATABASE=Telecomunicaciones;Trusted_Connection=yes')

        # Definir la consulta SQL con el JOIN
        query = """
        select E.Nombre as 'Nombre_empleado', C.Nombre as 'Nombre_cliente', C.Sexo as 'Sexo_cliente', 
        S.Nombre_servicio as 'Servicio', EQ.tipo as 'Tipo_equipo', F.fecha as 'Fecha_facturación' from Empleados as E 
        join Facturación as F on F.Id = F.Id join Servicios as S on S.Id = S.Id join Clientes as C on C.Id =  S.Id 
        join Equipos as EQ on EQ.Id =  S.Id
        """
        # Ejecutar la consulta SQL y obtener los resultados en un DataFrame
        df = pd.read_sql(query, conn)
        # Crear el objeto PandasTable
        # table = Table(self.root, model=TableModel(df))

        # Configurar la tabla y mostrarla
        # table.show()

        # Crear la ventana para el gráfico
        graph_window = Toplevel(self.root)
        graph_window.title("Gráfico con datos extraídos de SQL")

        # Crear un Figure y un Axes para el gráfico de barras
        fig = plt.Figure(figsize=(6, 4), dpi=100)
        ax = fig.add_subplot(111)

        # Crear los datos para el gráfico de barras
        servicios = df['Servicio'].value_counts()
        empleados = df['Nombre_empleado'].value_counts()
        ax.bar(servicios.index, servicios.values, color='b', alpha=0.5, label='Servicios')
        ax.bar(empleados.index, empleados.values, color='r', alpha=0.5, label='Empleados')

        # Agregar una leyenda al gráfico
        ax.legend()

        # Crear un objeto FigureCanvasTkAgg y agregarlo a la ventana secundaria
        canvas = FigureCanvasTkAgg(fig, master=graph_window)
        canvas.draw()
        canvas.get_tk_widget().pack()
        # plt.title("El empleado que más ventas a hecho")

        # Iniciar el bucle principal de Tkinter

        # root.mainloop()