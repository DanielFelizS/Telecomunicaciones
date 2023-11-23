import pyodbc
from tkinter import messagebox

def conectar():
    try:
        conexion = pyodbc.connect('DRIVER={SQL Server};SERVER=DESKTOP-HIESJ07;DATABASE=Telecomunicaciones;Trusted_Connection=yes')
        print('La conexión fue exitosa')
        return conexion
    except pyodbc.Error as ex:
        messagebox.showerror("Error", "La conexión dio error")

def agregar_empleado(nombre, apellidos, sexo, cargo, sueldo, telefono, direccion, cedula, fecha_nacimiento, correo, fecha_contratacion, nacionalidad):
    try:
        conexion = conectar()
        cursor = conexion.cursor()
        cursor.execute(f"exec Insert_empleados '{nombre}', '{apellidos}', '{sexo}', '{cargo}', '{sueldo}', '{telefono}', '{direccion}', '{cedula}', '{fecha_nacimiento}', '{correo}', '{fecha_contratacion}', '{nacionalidad}'")
        conexion.commit()
        messagebox.showinfo('Información','El empleado fue agregado a la base de datos')
    except ValueError:
        messagebox.showerror("Error", "Los datos no son correctos")
    finally:
        conexion.close()

def eliminar_empleado(Cedul):
    try:
        conexion = conectar()
        cursor = conexion.cursor()
        cursor.execute(f"exec Eliminar_empleado '{Cedul}'")
        conexion.commit()
        messagebox.showinfo('Información','El empleado fue eliminado de la base de datos')
    except ValueError:
        messagebox.showerror("Error", "Los datos no son correctos")
    finally:
        conexion.close()

def actualizar_empleado(nombre, apellidos, sexo, cargo, sueldo, telefono, direccion, cedula, fecha_nacimiento, correo, fecha_contratacion, nacionalidad):
    try:
        conexion = conectar()
        cursor = conexion.cursor()
        cursor.execute(f"exec Actualizar_empleados '{Id}' '{nombre}', '{apellidos}', '{sexo}', '{cargo}', '{sueldo}', '{telefono}', '{direccion}', '{cedula}', '{fecha_nacimiento}', '{correo}', '{fecha_contratacion}', '{nacionalidad}'")
        conexion.commit()
        conexion.commit()
        messagebox.showinfo('Información','El empleado fue actualizado correctamente')
    except ValueError:
        messagebox.showerror("Error", "Los datos no son correctos")
    finally:
        conexion.close()

def ver_empleado(tabla_empleados):
    try:
        conexion = conectar()
        cursor = conexion.cursor()
        cursor.execute(f"SELECT Id, Nombre, Apellido, Sexo, Cargo, Sueldo, Teléfono, Dirección, Cédula, FechaNacimiento, Fecha_contratación, Nacionalidad FROM Empleados")
        resultados = cursor.fetchall()
        if resultados:
            tabla_empleados.delete(*tabla_empleados.get_children())
            for resultado in resultados:
                tabla_empleados.insert("", "end", values=(*resultado,))
        messagebox.showinfo('Información', 'Has consultado los datos correctamente')
    except Exception as ex:
        messagebox.showerror("Error", f"Ocurrió un error al consultar los datos: {ex}")
    finally:
        conexion.close()