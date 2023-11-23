import pyodbc
from tkinter import messagebox
from tkinter import ttk

def conectar():
    try:
        conexion = pyodbc.connect('DRIVER={SQL Server};SERVER=DESKTOP-HIESJ07;DATABASE=Telecomunicaciones;Trusted_Connection=yes')
        print('La conexión fue exitosa')
        return conexion
    except pyodbc.Error as ex:
        messagebox.showerror("Error", "La conexión dio error")

def agregar_factura(Cliente, Empleado, Servicio, Equipo, Fecha, Descripcion):
    try:
        conexion = conectar()
        cursor = conexion.cursor()
        cursor.execute(f"exec Insert_Factura '{Cliente}', '{Empleado}', '{Servicio}', '{Equipo}', {Fecha}, '{Descripcion}'")
        conexion.commit()
        messagebox.showinfo('Información','La factura fue agregada a la base de datos')
    except ValueError:
        messagebox.showerror("Error", "Los datos no son correctos")
    finally:
        conexion.close()

def eliminar_factura(cliente):
    try:
        conexion = conectar()
        cursor = conexion.cursor()
        cursor.execute(f"exec Eliminar_Factura '{cliente}'")
        conexion.commit()
        messagebox.showinfo('Información','La factura fue eliminada de la base de datos')
    except ValueError:
        messagebox.showerror("Error", "Los datos no son correctos")
    finally:
        conexion.close()

def actualizar_factura(Cliente, Empleado, Servicio, Equipo, Fecha, Descripcion):
    try:
        conexion = conectar()
        cursor = conexion.cursor()
        cursor.execute(f"exec Actualizar_Factura '{Cliente}', '{Empleado}', '{Servicio}', '{Equipo}', {Fecha}, '{Descripcion}'")
        conexion.commit()
        conexion.commit()
        messagebox.showinfo('Información','La factura fue actualizada correctamente')
    except ValueError:
        messagebox.showerror("Error", "Los datos no son correctos")
    finally:
        conexion.close()

def buscar_factura(Cliente, tabla_factura):
    try:
        conexion = conectar()
        cursor = conexion.cursor()
        cursor.execute(f"SELECT Id, Nombre_cliente, Nombre_empleado, Nombre_servicio, Nombre_equipo, fecha, descripcion FROM Facturación WHERE Nombre_cliente LIKE '%{Cliente}%' ORDER BY Id DESC")
        resultados = cursor.fetchall()
        if resultados:
            tabla_factura.delete(*tabla_factura.get_children())
            for resultado in resultados:
                tabla_factura.insert("", "end", values=(*resultado,))
        else:
            messagebox.showinfo('Información','No se encontraron facturas con el cliente especificado')
    except ValueError:
        messagebox.showerror("Error", "Los datos no son correctos")
    finally:
        conexion.close()

def ver_facturas(tabla_factura):
    try:
        conexion = conectar()
        cursor = conexion.cursor()
        cursor.execute(f"SELECT Id, Nombre_cliente, Nombre_empleado, Nombre_servicio, Nombre_equipo, fecha, descripcion FROM Facturación")
        resultados = cursor.fetchall()
        if resultados:
            tabla_factura.delete(*tabla_factura.get_children())
            for resultado in resultados:
                tabla_factura.insert("", "end", values=(*resultado,))
        messagebox.showinfo('Información', 'Has consultado los datos correctamente')
    except Exception as ex:
        messagebox.showerror("Error", f"Ocurrió un error al consultar los datos: {ex}")
    finally:
        conexion.close()
