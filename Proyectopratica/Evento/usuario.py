#Aqui estaran las funciones registrar usuario y encontrar usuario por id con decorador

def registrar_usuario(usuarios:list):
    try:

        nombre= input("Ingrese su nombre: ")
        id= str(input("ingrese su id: "))
        edad= int(input("Ingrese su edad : "))
        email= str(input("Ingrese su email: "))
        presupuesto=float(input("Ingrese su presupuesto: "))
        usuario = {
                'nombre':nombre,
                'id':id,
                'edad':edad,
                'email':email,
                'presupuesto':presupuesto
            }
        usuarios.append(usuario)
        print(f"Cliente registrado con exito")
        print("Proceso finalizado")
        
        if presupuesto < 1000:
            print("Usted no tendra dinero suficiente para registrar un eveto")
            
        if edad < 18 :
            print("Tenga en cuenta que no puede puede un evento siendo menor de edad")
    except Exception as e:
        print(f"Error : {e}")




def encontrar_usuario(func):
    def wrapper(usuarios:list,id:str):
        for user in usuarios:
            if user['id'] == id:
                return func(user)
        print("No encontrado")
        return None      
    return wrapper
    


@encontrar_usuario
def buscar_usuario_id(usuario:list):
    print("Usuario encontrado")
    print(usuario)
    return usuario
    

