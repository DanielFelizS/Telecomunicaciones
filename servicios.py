import pyodbc
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

def conectar():
    try:
        conexion = pyodbc.connect('DRIVER={SQL Server};SERVER=DESKTOP-HIESJ07;DATABASE=Telecomunicaciones;Trusted_Connection=yes')
        print('La conexión fue exitosa')
        return conexion
    except pyodbc.Error as ex:
        messagebox.showerror("Error", "La conexión dio error")

def agregar_servicio(Cliente, Empleado, Equipos, Nombre_servicio, Descripcion, Precio, Tipo_plan):
    try:
        conexion = conectar()
        cursor = conexion.cursor()
        cursor.execute(f"exec Insertar_Servicios '{Cliente}', '{Empleado}', '{Equipos}', '{Nombre_servicio}', '{Descripcion}', '{Precio}', '{Tipo_plan}'")
        conexion.commit()
        messagebox.showinfo('Información','El servicio fue agregado a la base de datos')
    except ValueError:
        messagebox.showerror("Error", "Los datos no son correctos")
    finally:
        conexion.close()

def eliminar_servicio(Cliente):
    try:
        conexion = conectar()
        cursor = conexion.cursor()
        cursor.execute(f"exec Eliminar_servicio '{Cliente}'")
        conexion.commit()
        messagebox.showinfo('Información','El servicio fue eliminado de la base de datos')
    except ValueError:
        messagebox.showerror("Error", "Los datos no son correctos")
    finally:
        conexion.close()

def actualizar_servicio(Cliente, Empleado, Equipos, Nombre_servicio, Descripcion, Precio, Tipo_plan):
    try:
        conexion = conectar()
        cursor = conexion.cursor()
        cursor.execute(f"exec Actualizar_servicio '{Cliente}', '{Empleado}', '{Equipos}', '{Nombre_servicio}', '{Descripcion}', '{float(Precio)}', '{Tipo_plan}'")
        conexion.commit()
        conexion.commit()
        messagebox.showinfo('Información','El servicio fue actualizado correctamente')
    except ValueError:
        messagebox.showerror("Error", "Los datos no son correctos")
    finally:
        conexion.close()

def buscar_servicio(Nombre, tabla_servicios):
    try:
        conexion = conectar()
        cursor = conexion.cursor()
        cursor.execute(f"SELECT Id, Nombre_cliente, Nombre_empleado, Nombre_equipo, Nombre_servicio, Descripcion, Precio, Tipo_plan FROM Servicios WHERE Nombre_cliente LIKE '%{Nombre}%' ORDER BY Id DESC")
        resultados = cursor.fetchall()
        if resultados:
            tabla_servicios.delete(*tabla_servicios.get_children())
            for resultado in resultados:
                tabla_servicios.insert("", "end", values=(*resultado,))
        else:
            messagebox.showinfo('Información','No se encontraron servicios con el nombre de el cliente específico')
    except ValueError:
        messagebox.showerror("Error", "Los datos no son correctos")
    finally:
        conexion.close()

def ver_servicio(tabla_servicios):
    try:
        conexion = conectar()
        cursor = conexion.cursor()
        cursor.execute("SELECT Id, Nombre_cliente, Nombre_empleado, Nombre_equipo, Nombre_servicio, Descripcion, Precio, Tipo_plan FROM Servicios")
        resultados = cursor.fetchall()
        if resultados:
            tabla_servicios.delete(*tabla_servicios.get_children())
            for resultado in resultados:
                tabla_servicios.insert("", "end", values=(*resultado,))
        conexion.close()
        messagebox.showinfo('Información', 'Has consultado los datos correctamente')
    except Exception as ex:
        messagebox.showerror("Error", f"Ocurrió un error al consultar los datos: {ex}")
    finally:
        conexion.close()