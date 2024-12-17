import tkinter as tk
from tkinter import messagebox

usuarios = []

class Register:
    def create_user_registration(usuarios: list):
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

        label_user = tk.Label(root, text="User name", **label_style)
        label_user.grid(row=5, column=0, padx=20, pady=5, sticky="nsew")

        entry_user = tk.Entry(root, **entry_style)
        entry_user.grid(row=5, column=1, padx=20, pady=5, sticky="nsew")

        label_id = tk.Label(root, text="ID:", **label_style)
        label_id.grid(row=6, column=0, padx=10, pady=5, sticky="nsew")

        entry_id = tk.Entry(root, show="*", **entry_style)
        entry_id.grid(row=6, column=1, columnspan=2, padx=10, pady=5, sticky="nsew")

        label_Email = tk.Label(root, text="Email", **label_style)
        label_Email.grid(row=7, column=0, padx=20, pady=5, sticky="nsew")

        entry_Email = tk.Entry(root, **entry_style)
        entry_Email.grid(row=7, column=1, padx=20, pady=5, sticky="nsew")

        label_Edad = tk.Label(root, text="Edad", **label_style)
        label_Edad.grid(row=8, column=0, padx=20, pady=5, sticky="nsew")

        entry_Edad = tk.Entry(root, **entry_style)
        entry_Edad.grid(row=8, column=1, padx=20, pady=5, sticky="nsew")

        label_Presupuesto = tk.Label(root, text="Presupuesto", **label_style)
        label_Presupuesto.grid(row=9, column=0, padx=20, pady=5, sticky="nsew")

        entry_Presupuesto = tk.Entry(root, **entry_style)
        entry_Presupuesto.grid(row=9, column=1, padx=20, pady=5, sticky="nsew")

        button_register = tk.Button(root, text="Register", command=lambda: Register.registrar_usuario(usuarios, root, entry_user, entry_id, entry_Email, entry_Edad, entry_Presupuesto), **label_style)
        button_register.grid(row=11, column=0, columnspan=3, padx=10, pady=5, sticky="nsew")

        root.mainloop()

    def registrar_usuario(usuarios: list, root, entry_user, entry_id, entry_Email, entry_Edad, entry_Presupuesto):
        try:
            nombre = entry_user.get()
            id = entry_id.get()
            edad = int(entry_Edad.get())
            email = entry_Email.get()
            presupuesto = float(entry_Presupuesto.get())

            usuario = {
                'nombre': nombre,
                'id': id,
                'edad': edad,
                'email': email,
                'presupuesto': presupuesto
            }

            usuarios.append(usuario)
            print("Cliente registrado con éxito")
            print("Proceso finalizado")

            if presupuesto < 1000:
                print("Usted no tendrá dinero suficiente para registrar un evento")

            if edad < 18:
                print("Tenga en cuenta que no puede registrar un evento siendo menor de edad")

            # Mostrar mensaje de confirmación
            messagebox.showinfo("Registro exitoso", "Usuario registrado con éxito")

            # Cerrar la ventana
            root.destroy()

        except Exception as e:
            print(f"Error: {e}")

def encontrar_usuario(func):
    def wrapper(usuarios: list, id: str):
        for user in usuarios:
            if user['id'] == id:
                return func(user)
        print("No encontrado")
        return None
    return wrapper

@encontrar_usuario
def buscar_usuario_id(usuario: list):
    print("Usuario encontrado")
    print(usuario)
    return usuario