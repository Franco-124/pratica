import asyncio
import getpass
import tkinter as tk
from tkinter import messagebox
from Evento.UIuser import Register, buscar_usuario_id
from Evento.UIevent import Register_event, mostrar_cantidad_eventos_registrados, eliminar_evento, mostrar_eventos_for_tipo
from Evento.Guardar_info import guardar_informacion, guardar_archivos_en_formato_json
from Evento.filtusuarios import filtrar_usuarios, filtrar_eventos, filtrar_numero_evento_por_tipo
from Evento.Pagos import pagar_evento
from datetime import datetime
from Evento.converstion import convertir_moneda
from Evento.Grafica import generate_bar_chart, generate_pie_chart
# from Evento.notifier import send_reminder

User_name = []
password = []

class Login:
    def __init__(self):
        self.User_name = []
        self.password = []

    def singin_interface(self):
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

        label_user_name = tk.Label(root, text="User name", **label_style)
        label_user_name.grid(row=5, column=0, padx=20, pady=5, sticky="nsew")

        entry_nombre = tk.Entry(root, **entry_style)
        entry_nombre.grid(row=5, column=1, padx=20, pady=5, sticky="nsew")

        label_password = tk.Label(root, text="Password", **label_style)
        label_password.grid(row=6, column=0, padx=10, pady=5, sticky="nsew")

        entry_password = tk.Entry(root, show ="*",**entry_style)
        entry_password.grid(row=6, column=1, columnspan=2, padx=10, pady=5, sticky="nsew")

        button_singin = tk.Button(root, text="sing in", command=lambda: self.user_sign(root, entry_nombre, entry_password))
        button_singin.grid(row=7, column=0, columnspan=3, padx=10, pady=5, sticky="nsew")

        button_login = tk.Button(root, text="Login", command=lambda: self.user_login(root))
        button_login.grid(row=8, column=0, columnspan=3, padx=10, pady=5, sticky="nsew")

        root.mainloop()

    def user_sign(self, root, entry_nombre, entry_password):
        user = entry_nombre.get()
        password = entry_password.get()

        self.User_name.append(user)
        self.password.append(password)

        messagebox.showinfo("Sing in", "User registered successfully")
        

    def user_login(self, sing_root):
        sing_root.destroy()
        root = tk.Tk()
        root.title("Login")
        root.geometry("400x400")
        label_style = {"bg": "lightblue", "fg": "black", "font": ("Arial", 12)}
        entry_style = {"bg": "white", "fg": "black", "font": ("Arial", 12)}
        root.config(bg="lightblue")  # Color de fondo

        label_user_name = tk.Label(root, text="User name", **label_style)
        label_user_name.grid(row=5, column=0, padx=20, pady=5, sticky="nsew")

        entry_nombre = tk.Entry(root, **entry_style)
        entry_nombre.grid(row=5, column=1, padx=20, pady=5, sticky="nsew")

        label_password = tk.Label(root, text="Password", **label_style)
        label_password.grid(row=6, column=0, padx=10, pady=5, sticky="nsew")

        entry_password = tk.Entry(root, show ="*",**entry_style)
        entry_password.grid(row=6, column=1, columnspan=2, padx=10, pady=5, sticky="nsew")

        #Help me to validate the user and the password, if password is correct show the main menu
        button_login = tk.Button(root, text="Login", command=lambda: self.validate_user(root, entry_nombre, entry_password))
        button_login.grid(row=8, column=0, columnspan=3, padx=10, pady=5, sticky="nsew")
    
    def validate_user(self, root, entry_nombre, entry_password):
        user = entry_nombre.get()
        password = entry_password.get()

        if user in self.User_name and password in self.password:
            messagebox.showinfo("Login", "User logged in successfully")
            root.destroy()
            self.main()
            
        else:
            messagebox.showerror("Login", "Incorrect user or password")

    def main(self):
        root = tk.Tk()
        root.title("Menú de opciones")
        root.geometry("400x600")
        label_style = {"bg": "lightblue", "fg": "black", "font": ("Arial", 12)}
        button_style = {"bg": "white", "fg": "black", "font": ("Arial", 12)}

        usuarios = []
        eventos = []

        options = [
            ("Registrar usuario", lambda: self.registrar_usuarios(usuarios)),
            ("Mostrar usuarios registrados", lambda: self.mostrar_usuarios(usuarios)),
            ("Buscar usuario por ID", lambda: self.buscar_usuarios(usuarios)),
            ("Registrar evento", lambda: self.registrar_eventos(usuarios, eventos)),
            ("Mostrar eventos registrados", lambda: self.mostrar_eventos(eventos)),
            ("Mostrar cantidad de eventos registrados", lambda: self.mostrar_cantidad_eventos(eventos)),
            ("Guardar información", lambda: self.guardar_informacion_Evento(usuarios, eventos)),
            ("Filtrar usuarios y eventos", lambda: self.filtrar_usuarios_y_eventos(usuarios, eventos)),
            ("Pagar evento", lambda: self.pagar_evento_menu(usuarios, eventos)),
            ("Eliminar evento", lambda: self.eliminar_eventos(eventos)),
            ("Ver costo de evento en otra moneda", lambda: self.convertir_monedas(eventos)),
            ("Crear gráfica bar de eventos", lambda: self.generate_bar_charts(eventos)),
            ("Crear gráfica pie de eventos", lambda: self.generate_pie_charts(eventos)),
            ("Filtrar eventos por tipo", lambda: self.filtrar_eventos_por_tipo(eventos)),
            ("Salir", lambda: self.salir(root, usuarios, eventos))
        ]

        for i, (text, command) in enumerate(options):
            button = tk.Button(root, text=text, command=command, **button_style)
            button.pack(fill='x', padx=20, pady=5)

        root.mainloop()

    def registrar_usuarios(self, usuarios):
        try:
            Register.create_user_registration(usuarios)
        except Exception as e:
            messagebox.showerror("Error", f"Error al registrar usuarios: {e}")

    def guardar_informacion_Evento(self, usuarios, eventos):
        try:
            guardar_informacion(usuarios, eventos)
        except Exception as e:
            messagebox.showerror("Error", f"Error al guardar información: {e}")

    def mostrar_cantidad_eventos(self, eventos):
        try:
            mostrar_cantidad_eventos_registrados(eventos)
        except Exception as e:
            messagebox.showerror("Error", f"Error {e}")

    def mostrar_usuarios(self, usuarios):
        if usuarios:
            for usuario in usuarios:
                print(usuario)
        else:
            messagebox.showinfo("Información", "No hay usuarios registrados")

    def buscar_usuarios(self, usuarios):
        try:
            id_buscar = getpass.getpass("\nIngrese el ID del usuario que desea buscar: ")
            buscar_usuario_id(usuarios, id_buscar)
        except Exception as e:
            messagebox.showerror("Error", f"Error al buscar usuario: {e}")

    def registrar_eventos(self, usuarios, eventos):
        try:
            Register_event.create_event_registration(usuarios, eventos)
        except Exception as e:
            messagebox.showerror("Error", f"Error al registrar eventos: {e}")

    def mostrar_eventos(self, eventos):
        if eventos:
            for evento in eventos:
                print(f"Eventos registrado \n {evento}")
        else:
            messagebox.showinfo("Información", "No hay eventos registrados")

    def filtrar_usuarios_y_eventos(self, usuarios, eventos):
        try:
            edad = input("Ingrese edad para buscar usuarios con esta edad: ")
            hora = datetime.strptime(input("Ingrese la hora (HH:MM): "), "%H:%M").time()
            filtrar_usuarios(usuarios, edad)
            print("---------")
            filtrar_eventos(eventos, hora)
        except Exception as e:
            messagebox.showerror("Error", f"Error al filtrar usuarios y eventos: {e}")

    def pagar_evento_menu(self, usuarios, eventos):
        try:
            id_usuario = getpass.getpass("Ingrese el ID del usuario que va a pagar el evento: ")
            usuario = buscar_usuario_id(usuarios, id_usuario)
            if not usuario:
                messagebox.showerror("Error", "Usuario no encontrado.")
                return

            nombre_evento = input("Ingrese el nombre del evento a pagar: ")
            evento = next((e for e in eventos if e['nombre'] == nombre_evento and e['id'] == id_usuario), None)
            if not evento:
                messagebox.showerror("Error", "Evento no encontrado.")
                return

            asyncio.run(pagar_evento(usuario, evento))
        except Exception as e:
            messagebox.showerror("Error", f"Error al pagar evento: {e}")

    def eliminar_eventos(self, eventos):
        try:
            event_name = input("Ingrese el nombre del evento que desea eliminar: ")
            eliminar_evento(eventos, event_name)
        except Exception as e:
            messagebox.showerror("Error", f"Error al eliminar evento: {e}")

    def convertir_monedas(self, eventos):
        try:
            moneda_destino = str(input("Ingrese la moneda a la que desea convertir el costo del evento ejemplo(USD,EUR,COP): "))
            convertir_moneda(eventos, moneda_destino)
        except Exception as e:
            messagebox.showerror("Error", f"Error al convertir moneda: {e}")

    def generate_bar_charts(self, eventos):
        numero_eventos_tipo = filtrar_numero_evento_por_tipo(eventos)
        tipos_evento = list(numero_eventos_tipo.keys())
        numero_eventos = list(numero_eventos_tipo.values())
        generate_bar_chart(tipos_evento, numero_eventos)

    def generate_pie_charts(self, eventos):
        numero_eventos_tipo = filtrar_numero_evento_por_tipo(eventos)
        tipos_evento = list(numero_eventos_tipo.keys())
        numero_eventos = list(numero_eventos_tipo.values())
        generate_pie_chart(tipos_evento, numero_eventos)

    def filtrar_eventos_por_tipo(self, eventos):
        try:
            tipo_evento = input("Ingrese el tipo de evento que desea filtrar: ")
            mostrar_eventos_for_tipo(eventos, tipo_evento)
        except Exception as e:
            messagebox.showerror("Error", f"Error al filtrar eventos por tipo: {e}")

    def salir(self, root, usuarios, eventos):
        try:
            guardar_informacion(usuarios, eventos)
            root.destroy()
        except Exception as e:
            messagebox.showerror("Error", f"Error al salir: {e}")

if __name__ == "__main__":
    login = Login()
    login.singin_interface()