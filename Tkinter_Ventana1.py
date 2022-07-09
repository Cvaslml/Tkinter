# Importo la libreria tkinter, con el alias tk
import tkinter as tk

# ------------------------------
# Ventana principal
# ------------------------------


# Creacion objeto Tk (ventana principal)
ventana_principal = tk.Tk()


# Titulo ventana_principal
ventana_principal.title("Suma enteros")

# Tamaño o dimensiones de la ventana
ventana_principal.geometry("500x500")

# Deshabilitamos el boton maximizar
ventana_principal.resizable(0,0)

# Color de fondo ventana principal
ventana_principal.config(bg="red")

# Icono de la ventana 
# ventana_principal.iconbitmap("suma.ico"/suma.png)

# ------------------------------
# Frame entrada datos
# ------------------------------
frame_entrada = tk.Frame(ventana_principal)
frame_entrada.config(bg="white", width=480, height=240)
frame_entrada.pack(fill=tk.BOTH)
frame_entrada.place(x=10, y=10)

# Etiqueta para el titulo
titulo = tk.Label(frame_entrada,text="Suma de enteros")
titulo.config(bg="green", fg="yellow", font="Calibri, 15")
titulo.place(x=150, y=10)

# Imagen
# logo_uis = tk.PhotoImage(file="uis.png")
# Label_logo = tk.Label(frame_entrada, image = logo_uis)
# Label_logo.place(x=10, y=40)

# ------------------------------
# Frame operaciones
# ------------------------------
frame_operaciones = tk.Frame(ventana_principal)
frame_operaciones.config(bg="white", width=480, height=120)
frame_operaciones.pack(fill=tk.BOTH)
frame_operaciones.place(x=10, y=255)

# ------------------------------
# Frame resultados
# ------------------------------
frame_resultados = tk.Frame(ventana_principal)
frame_resultados.config(bg="pink", width=480, height=110)
frame_resultados.pack(fill=tk.BOTH)
frame_resultados.place(x=10, y=380)

# Desplegar ventana principal, y queda a la espera de los eventos del usuario
ventana_principal.mainloop()