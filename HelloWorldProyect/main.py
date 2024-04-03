import tkinter as tk
from tkinter import ttk

# Se define la ventana principal de la aplicación
root = tk.Tk()

# Se crea el primer elemento dentro de la aplicación
# el primer elemento de Label es la página de la aplicación
# en donde se quiere ubicar el objeto. El argumento text es la
# información que se quiere imprimir y padding asigna espacio a los
# costados y arriba y abajo del texto ingresado. Finalmente, el 
# método pack() hace que el objeto se coloque en la ventana.
ttk.Label(root, text="Hello, World!", padding=(30,10)).pack()

# Se corre la configuración realizada. Todo lo que se configure luego de esta línea no será ejecutado en la aplicación
# hasta que la ventana de la aplicación se cierre.
root.mainloop()
