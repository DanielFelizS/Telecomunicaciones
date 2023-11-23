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

def agregar_equipo(TipoEquipo, Fecha):
    try:
        conexion = conectar()
        cursor = conexion.cursor()
        cursor.execute(f"exec Insertar_Equipos '{TipoEquipo}', '{Fecha}'")
        conexion.commit()
        messagebox.showinfo('Información','El equipo fue agregado a la base de datos')
    except ValueError:
        messagebox.showerror("Error", "Los datos no son correctos")
    finally:
        conexion.close()

def eliminar_equipo(Fecha):
    try:
        conexion = conectar()
        cursor = conexion.cursor()
        cursor.execute(f"exec Eliminar_Equipo '{Fecha}'")
        conexion.commit()
        messagebox.showinfo('Información','El equipo fue eliminado de la base de datos')
    except ValueError:
        messagebox.showerror("Error", "Los datos no son correctos")
    finally:
        conexion.close()

def actualizar_equipo(TipoEquipo, Fecha):
    try:
        conexion = conectar()
        cursor = conexion.cursor()
        cursor.execute(f"exec Actualizar_Equipo '{TipoEquipo}', '{Fecha}'")
        conexion.commit()
        conexion.commit()
        messagebox.showinfo('Información','El equipo fue actualizado correctamente')
    except ValueError:
        messagebox.showerror("Error", "Los datos no son correctos")
    finally:
        conexion.close()

def buscar_equipo(Fecha, tabla_equipo):
    try:
        conexion = conectar()
        cursor = conexion.cursor()
        cursor.execute(f"SELECT Id, tipo, fecha_fabricación FROM Equipos WHERE fecha_fabricación LIKE '%{Fecha}%' ORDER BY Id DESC")
        resultados = cursor.fetchall()
        if resultados:
            tabla_equipo.delete(*tabla_equipo.get_children())
            for resultado in resultados:
                tabla_equipo.insert("", "end", values=(*resultado,))
        else:
            messagebox.showinfo('Información','No se encontraron equipos con la fecha especificada')
    except ValueError:
        messagebox.showerror("Error", "Los datos no son correctos")
    finally:
        conexion.close()

def ver_equipo(tabla_equipo):
    try:
        conexion = conectar()
        cursor = conexion.cursor()
        cursor.execute(f"SELECT Id, tipo, fecha_fabricación FROM Equipos")
        resultados = cursor.fetchall()
        if resultados:
            tabla_equipo.delete(*tabla_equipo.get_children())
            for resultado in resultados:
                tabla_equipo.insert("", "end", values=(*resultado,))
        conexion.close()
        messagebox.showinfo('Información', 'Has consultado los datos correctamente')
    except Exception as ex:
        messagebox.showerror("Error", f"Ocurrió un error al consultar los datos: {ex}")
    finally:
        conexion.close()