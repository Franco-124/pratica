#Aca vamos a registrar eventos por cliente usando el decorador de usuario

from datetime import datetime
from Evento.usuario import buscar_usuario_id

def registrar_evento(usuarios: list, eventos: list):
    try:
        nombre = input("Ingrese nombre del evento: ")
        hora = (lambda: datetime.strptime(input("Ingrese la hora (HH:MM): "), "%H:%M").time() if True else None)()
        duracion = str(input("Duracion del evento: ejemplo (2 horas): "))
        ubicacion = str(input("Ingrese ubicacion del evento: "))
        tipo = str(input("Ingrese un tipo de evento (social, privado, personalizado): "))
        total_Evento = 0
        if tipo.lower() == "social":
            total_Evento = 2000
        elif tipo.lower() == "privado":
            total_Evento = 3000
        elif tipo.lower() == "personalizado":
            total_Evento = 4000
        else:
            total_Evento = 1000

        nombre_usuario = input("Ingrese el usuario de la persona responsable del evento: ")
        id = str(input("Ingrese el id de la persona responsable: "))
        
        usuario = None
        while not usuario:
            usuario = buscar_usuario_id(usuarios, id)
            if not usuario:
                print(f"Usuario con id {id} no encontrado, intente de nuevo")
                id = str(input("Ingrese el id de la persona responsable: "))

        if usuario['edad'] < 18:
            print("No puede registrar un evento siendo menor de edad")
            return
        
        if usuario['presupuesto']<1000:
            print("No puede registrar un evento ,--Presupuesto insuficiente--")
            return 

        evento = {
            'nombre_usuario': usuario['nombre'],
            'id': id,
            'nombre': nombre,
            'hora': hora,
            'duracion': duracion,
            'ubicacion': ubicacion,
            'tipo': tipo,
            'total_evento': total_Evento
        }
        eventos.append(evento)
        print(f"Evento registrado a nombre de {usuario['nombre']} con exito")
        return eventos

    except ValueError as e:
        print(f"Entrada inválida: Error {e}")
    except Exception as e:
        print(f"Error al registrar evento: {e}")


def mostrar_cantidad_eventos_registrados(eventos: list):
    cont=0
    for event in eventos:
        cont+=1
    print(f"Hay {cont} eventos registrados ")
    
