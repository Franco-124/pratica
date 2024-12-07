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
    def wrapper (eventos:list, tipo)->dict:
        eventos_filtrados = list(filter(lambda item: item['tipo']==tipo, eventos))
        if eventos_filtrados is not None:
            print(f"Eventos encontrados de tipo {tipo}")
            return func(eventos_filtrados)
        else:
            print(f"Eventos de tipo {tipo} no encontrado")
    return wrapper


@filtrar_eventos_tipo
def mostrar_eventos_for_tipo(eventos:list)->dict:
    print("Eventos registrados")
    print(eventos)
    return eventos

