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

def agregar_cliente(Nombre, Apellidos, Sexo, Fecha_Na, Dire, Sector, Municipio, Provincia, Cedula, Correo, Tele):
    try:
        conexion = conectar()
        cursor = conexion.cursor()
        cursor.execute(f"exec Insertar_clientes '{Nombre}', '{Apellidos}', '{Sexo}', '{Fecha_Na}', '{Dire}', '{Sector}', '{Municipio}', '{Provincia}', '{Cedula}', '{Correo}', '{Tele}'")
        conexion.commit()
        messagebox.showinfo('Información','El cliente fue agregado a la base de datos')
    except ValueError:
        messagebox.showerror("Error", "Los datos no son correctos")
    finally:
        conexion.close()

def eliminar_cliente(Cedul):
    try:
        conexion = conectar()
        cursor = conexion.cursor()
        cursor.execute(f"exec Eliminar_cliente '{Cedul}'")
        conexion.commit()
        messagebox.showinfo('Información','El cliente fue eliminado de la base de datos')
    except ValueError:
        messagebox.showerror("Error", "Los datos no son correctos")
    finally:
        conexion.close()

def actualizar_cliente(Nombre, Apellidos, Sexo, Fecha_Na, Dire, Sector, Municipio, Provincia, Cedula, Correo, Tele):
    try:
        conexion = conectar()
        cursor = conexion.cursor()
        cursor.execute(f"exec Actualizar_cliente '{Nombre}', '{Apellidos}', '{Sexo}', '{Fecha_Na}', '{Dire}', '{Sector}', '{Municipio}', '{Provincia}', '{Cedula}', '{Correo}', '{Tele}'")
        conexion.commit()
        conexion.commit()
        messagebox.showinfo('Información','El cliente fue actualizado correctamente')
    except ValueError:
        messagebox.showerror("Error", "Los datos no son correctos")
    finally:
        conexion.close()

def buscar_cliente(Cedula, tabla_cliente):
    try:
        conexion = conectar()
        cursor = conexion.cursor()
        cursor.execute(f"SELECT Id, Nombre, Apellido, Sexo, Fecha_nacimiento, Direccion, Sector, Municipio, Provincia, Cédula, Correo, Teléfono FROM Clientes WHERE Cédula LIKE '%{Cedula}%' ORDER BY Id DESC")
        resultados = cursor.fetchall()
        if resultados:
            tabla_cliente.delete(*tabla_cliente.get_children())
            for resultado in resultados:
                tabla_cliente.insert("", "end", values=(*resultado,))
        else:
            messagebox.showinfo('Información','No se encontraron clientes con la cédula especificada')
    except ValueError:
        messagebox.showerror("Error", "Los datos no son correctos")

def ver_cliente(tabla_cliente):
    try:
        conexion = conectar()
        cursor = conexion.cursor()
        cursor.execute("SELECT Id, Nombre, Apellido, Sexo, Fecha_nacimiento, Direccion, Sector, Municipio, Provincia, Cédula, Correo, Teléfono FROM Clientes")
        resultados = cursor.fetchall()
        if resultados:
            for resultado in resultados:
                tabla_cliente.insert("", "end", values=resultado)
        conexion.close()
        messagebox.showinfo('Información', 'Has consultado los datos correctamente')

    except Exception as ex:
        messagebox.showerror("Error", f"Ocurrió un error al consultar los datos: {ex}")