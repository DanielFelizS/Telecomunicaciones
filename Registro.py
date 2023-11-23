from tkinter import *
from tkinter import messagebox
import pyodbc
import usuario
from Telecomunicaciones import interfaz

# Crea una conexión a la base de datos
conn = pyodbc.connect('DRIVER={SQL Server};SERVER=DESKTOP-HIESJ07; Database=Usuarios; Trusted_Connection=yes;')

# Crea una tabla de usuarios (si no existe)
conn.execute('''IF NOT EXISTS (SELECT * FROM sysobjects WHERE name='usuarios' and xtype='U')
                CREATE TABLE usuarios
                (ID INT PRIMARY KEY IDENTITY,
                USERNAME VARCHAR(50) NOT NULL UNIQUE,
                PASSWORD VARCHAR(50) NOT NULL);''')

# Guarda los cambios en la base de datos
conn.commit()

# Función de registros
def registro():
    # Obtiene el nombre de usuario y la contraseña
    username = entry_username.get()
    password = entry_password.get()

    # Verifica que el nombre de usuario no esté en uso
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM usuarios WHERE USERNAME = ?", (username,))
    row = cursor.fetchone()
    if row is not None:
        messagebox.showerror("Error", "El nombre de usuario ya está en uso.")
        return

    # Agrega el usuario a la base de datos
    cursor.execute("INSERT INTO usuarios (USERNAME, PASSWORD) VALUES (?, ?)", (username, password))
    conn.commit()

    # Muestra un mensaje de éxito
    messagebox.showinfo("Registro", "Registro exitoso.")

    # Crea la nueva ventana
    nueva_ventana = Toplevel(ventana)
    Telecomunicaciones = interfaz(nueva_ventana)
    nueva_ventana.mainloop()

# Función de login
def login():
    # Obtiene el nombre de usuario y la contraseña
    username = entry_username.get()
    password = entry_password.get()
    # Verifica que el nombre de usuario y la contraseña sean correctos
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM usuarios WHERE USERNAME = ? AND PASSWORD = ?", (username, password))
    row = cursor.fetchone()
    if row is None:
        messagebox.showerror("Error", "Nombre de usuario o contraseña incorrectos.")
        return
    # Muestra un mensaje de éxito
    messagebox.showinfo("Login", "Login exitoso.")
    # Crea la nueva ventana
    nueva_ventana = Toplevel(ventana)
    Telecomunicaciones = interfaz(nueva_ventana)
    nueva_ventana.mainloop()

ventana = Tk()
ventana.title("Login y Registro")
ventana.geometry("{0}x{1}+0+0".format(ventana.winfo_screenwidth(), ventana.winfo_screenheight()))
# Crea los campos de entrada
label_username = Label(ventana, text="Nombre de usuario")
label_username.pack()
entry_username = Entry(ventana, width = 35)
entry_username.pack()

label_password = Label(ventana, text="Contraseña")
label_password.pack()
entry_password = Entry(ventana, show="*", width = 35)
entry_password.pack()

# Crea los botones de registro y login
boton_registro = Button(ventana, text="Registro", command=registro, padx = 6, pady = 6)
boton_registro.pack()

boton_login = Button(ventana, text="Login", command=login, padx = 6, pady = 6)
boton_login.pack()

# Ejecuta el bucle principal de la aplicación
ventana.mainloop()