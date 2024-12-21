import tkinter as tk
from tkinter import messagebox
from .buscar_hora import give_info
from datetime import datetime
from Evento.UIuser import buscar_usuario_id

usuarios = []

class Register_event:
    def create_event_registration(usuarios, eventos: list):
        """
        vamos a crear una interfaz grafica para el registro de usuarios

        no se necesita de parametros

        no retorna nada
        """
        root = tk.Tk()
        root.title("Login")
        root.geometry("400x400")
        label_style = {"bg": "lightblue", "fg": "black", "font": ("Arial", 12)}
        entry_style = {"bg": "white", "fg": "black", "font": ("Arial", 12)}
        root.config(bg="lightblue")  # Color de fondo

        # Create a grid with 3 columns
        root.columnconfigure(0, weight=1)
        root.columnconfigure(1, weight=1)
        root.columnconfigure(2, weight=1)

        # Creacion de labels y entrys

        label_welcome = tk.Label(root, text="Welcome", **label_style)
        label_welcome.grid(row=4, column=0, columnspan=3, padx=10, pady=5, sticky="nsew")

        label_nombre = tk.Label(root, text="Event name", **label_style)
        label_nombre.grid(row=5, column=0, padx=20, pady=5, sticky="nsew")

        entry_nombre = tk.Entry(root, **entry_style)
        entry_nombre.grid(row=5, column=1, padx=20, pady=5, sticky="nsew")

        label_hora = tk.Label(root, text="Hora:", **label_style)
        label_hora.grid(row=6, column=0, padx=10, pady=5, sticky="nsew")

        entry_hora = tk.Entry(root, **entry_style)
        entry_hora.grid(row=6, column=1, columnspan=2, padx=10, pady=5, sticky="nsew")

        label_duracion = tk.Label(root, text="Duración", **label_style)
        label_duracion.grid(row=7, column=0, padx=20, pady=5, sticky="nsew")

        entry_duracion = tk.Entry(root, **entry_style)
        entry_duracion.grid(row=7, column=1, padx=20, pady=5, sticky="nsew")

        label_ubicacion = tk.Label(root, text="Ubicacion", **label_style)
        label_ubicacion.grid(row=8, column=0, padx=20, pady=5, sticky="nsew")

        entry_ubicacion = tk.Entry(root, **entry_style)
        entry_ubicacion.grid(row=8, column=1, padx=20, pady=5, sticky="nsew")

        label_tipo = tk.Label(root, text="Tipo", **label_style)
        label_tipo.grid(row=9, column=0, padx=20, pady=5, sticky="nsew")

        entry_tipo = tk.Entry(root, **entry_style)
        entry_tipo.grid(row=9, column=1, padx=20, pady=5, sticky="nsew")

        label_fecha = tk.Label(root, text="Fecha", **label_style)
        label_fecha.grid(row=10, column=0, padx=20, pady=5, sticky="nsew")

        entry_fecha = tk.Entry(root, **entry_style)
        entry_fecha.grid(row=10, column=1, padx=20, pady=5, sticky="nsew")

        button_register = tk.Button(root, text="Register", command=lambda: registrar_evento(usuarios, root, eventos, entry_nombre, entry_hora, entry_duracion, entry_ubicacion, entry_tipo, entry_fecha), **label_style)
        button_register.grid(row=11, column=0, columnspan=3, padx=10, pady=5, sticky="nsew")

        root.mainloop()

def registrar_evento(usuarios: list, root, eventos: list, nombre: str, hora: str, duracion: str, ubicacion: str, tipo: str, fecha: str):
    try:
        nombre = nombre.get()
        hora = hora.get()
        duracion = duracion.get()
        ubicacion = ubicacion.get()   
        tipo = tipo.get()
        fecha = fecha.get()

        # Formatear la fecha
        try:
            fecha_obj = datetime.strptime(fecha, "%d/%m/%Y")
            fecha_formateada = fecha_obj.strftime("%Y-%m-%d")
        except ValueError:
            messagebox.showerror("Error", "Formato de fecha inválido. Use el formato DD/MM/YYYY.")
            return

        total_Evento = 0
        if tipo.lower() == "social":
            total_Evento = 2000
        elif tipo.lower() == "privado":
            total_Evento = 3000
        elif tipo.lower() == "personalizado":
            total_Evento = 4000
        else:
            total_Evento = 1000
        
        for event in eventos:
            if event['ubicacion'] == ubicacion and event['hora'] == hora:
                messagebox.showerror("Error", f"Ya hay un evento programado para el {fecha_formateada} en {ubicacion} a las {hora}")
                return

        root.destroy()
        
        # Crear nueva ventana para ingresar usuario y ID
        user_root = tk.Tk()
        user_root.geometry("400x400")
        user_root.title("User Information")
        label_style = {"bg": "lightblue", "fg": "black", "font": ("Arial", 12)}
        entry_style = {"bg": "white", "fg": "black", "font": ("Arial", 12)}

        label_nombre_usuario = tk.Label(user_root, text="Enter user name", **label_style)
        label_nombre_usuario.grid(row=1, column=0, padx=20, pady=5, sticky="nsew")

        entry_nombre_usuario = tk.Entry(user_root, **entry_style)
        entry_nombre_usuario.grid(row=1, column=1, padx=20, pady=5, sticky="nsew")

        label_id = tk.Label(user_root, text="User ID", **label_style)
        label_id.grid(row=2, column=0, padx=20, pady=5, sticky="nsew")

        entry_id = tk.Entry(user_root, show="*" , **entry_style)
        entry_id.grid(row=2, column=1, padx=20, pady=5, sticky="nsew")

        button_register_user = tk.Button(user_root, text="Register", command=lambda: check_and_register(user_root, entry_id, entry_nombre_usuario, usuarios, eventos, nombre, hora, duracion, ubicacion, tipo, total_Evento, fecha_formateada), **label_style)
        button_register_user.grid(row=3, column=0, columnspan=2, padx=10, pady=5, sticky="nsew")

        user_root.mainloop()

    except ValueError as e:
        messagebox.showerror("Error", f"Entrada inválida: {e}")
    except Exception as e:
        messagebox.showerror("Error", f"Error al registrar evento: {e}")

def check_and_register(root, entry_id, entry_nombre, usuarios, eventos, nombre, hora, duracion, ubicacion, tipo, total_Evento, fecha):
    """
    Metodo que verifica el id y el nombre usuario

    recibe parametros de usuarios,eventos, y los entrys de id y nombre

    El metodo no retorna nada
    """
    id = entry_id.get()
    nombre_usuario = entry_nombre.get()

    usuario = buscar_usuario_id(usuarios, id)
    if not usuario:
        messagebox.showerror("Error", "Usuario no encontrado, ingrese un ID válido")
        return

    if usuario['edad'] < 18:
        messagebox.showerror("Error", "No puede registrar un evento siendo menor de edad")
        return
    
    if usuario['presupuesto'] < 1000:
        messagebox.showerror("Error", "No puede registrar un evento, presupuesto insuficiente")
        return 

    evento = {
        'nombre_usuario': usuario['nombre'],
        'id': id,
        'nombre': nombre,
        'hora': hora,
        'duracion': duracion,
        'ubicacion': ubicacion,
        'tipo': tipo,
        'total_evento': total_Evento,
        'fecha': fecha
    }
    eventos.append(evento)
    messagebox.showinfo("Éxito", "Evento registrado con éxito")
    print(give_info(eventos, nombre, ubicacion))

    root.destroy()

def mostrar_cantidad_eventos_registrados(eventos: list):
    cont = len(eventos)
    print(f"Hay {cont} eventos registrados")

def eliminar_evento(eventos, evento_name):
    print("Está a punto de eliminar un evento")
    opcion = input("¿Desea borrar el evento (si/no)? ").lower()

    if opcion == "si":
        encontrado = False
        for evento in eventos:
            if evento['nombre'] == evento_name:
                eventos.remove(evento)
                print(f"Evento '{evento_name}' eliminado con éxito")
                encontrado = True
                break
        
        if not encontrado:
            print("Evento no encontrado")
    else:
        print("Operación cancelada") 

    if eventos:
        print("Eventos registrados:")
        for evento in eventos:
            print(evento)
    else:
        print("No hay eventos registrados")

def filtrar_eventos_tipo(func):
    def wrapper(eventos: list, tipo) -> dict:
        eventos_filtrados = list(filter(lambda item: item['tipo'] == tipo, eventos))
        if eventos_filtrados:
            print(f"Eventos encontrados de tipo {tipo}")
            return func(eventos_filtrados)
        else:
            print(f"Eventos de tipo {tipo} no encontrados")
    return wrapper

@filtrar_eventos_tipo
def mostrar_eventos_for_tipo(eventos: list) -> dict:
    print("Eventos registrados")
    print(eventos)
    return eventos