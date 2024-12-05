#Aqui estaran las funciones registrar usuario y encontrar usuario por id con decorador
import getpass
def registrar_usuario(usuarios:list):
    try:

        nombre = input("Ingrese su nombre: ")
        id = getpass.getpass("Ingrese su id: ")
        edad = int(input("Ingrese su edad: "))
        email = str(input("Ingrese su email: "))
        presupuesto = float(input("Ingrese su presupuesto: "))
        
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
            
    except Exception as e:
        print(f"Error: {e}")



def encontrar_usuario(func):
    def wrapper(usuarios:list,id:str, nombre: str):
        for user in usuarios:
            if user['id'] == id and user['nombre'] == nombre:
                return func(user)
        print("Usuario  no encontrado")
        return None      
    return wrapper


@encontrar_usuario
def buscar_usuario(usuario:list):
    if usuario:
        print(f"Usuario con id  {usuario['id']} y nombre {usuario['nombre']} encontrado")
        print(usuario)
        return usuario

        

