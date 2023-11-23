import pyodbc
from tkinter import *
from tkinter import messagebox

def conectar():
    try:
        conexion = pyodbc.connect('DRIVER={SQL Server};SERVER=DESKTOP-HIESJ07;DATABASE=Usarios;Trusted_Connection=yes')
        print('La conexión fue exitosa')
        return conexion
    except Exception as ex:
        messagebox.showerror("Error", "La conexión dio error")

def agregar_usario(nombre, contraseña):
    try:
        conexion = conectar()
        cursor = conexion.cursor()
        cursor.execute(f"exec Insertar_Usuario '{nombre}', '{contraseña}'")
        conexion.commit()
        messagebox.showinfo("Información", "El usuario ha sido registrado correctamente.")
    except ValueError:
        messagebox.showerror("Error", "Los datos no son correctos")
    finally:
        conexion.close()

def eliminar_usuario(nombre):
    try:
        conexion = conectar()
        cursor = conexion.cursor()
        cursor.execute(f"exec Eliminar_Usuario '{nombre}'")
        conexion.commit()
        messagebox.showinfo('Información','El servicio fue eliminado de la base de datos')
    except ValueError:
        messagebox.showerror("Error", "Los datos no son correctos")
    finally:
        conexion.close()