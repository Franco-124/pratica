#guardar información de eventos y usuarios en archivos
from datetime import datetime
import json



def guardar_informacion(usuarios: list, eventos: list):
    try:
        with open('info_evento.txt', mode='w') as file:
            file.write("----Usuarios registrados-----\n")
            for user in usuarios:
                file.write(f"\n nombre: {user['nombre']} \n id: {user['id']}\n edad: {user['edad']} \n email: {user['email']}")
            file.write("\n----Eventos Registrados----\n")
            for event in eventos:
                file.write(f"\n nombre: {event['nombre']}\n hora: {event['hora']}, \n duracion :{event['duracion']}, \n ubicacion {event['ubicacion']} \n tipo: {event['tipo']} \n Costo evento : {event['total_evento']} ")  
            print("Informacion de eventos guardada exitosamente")
    except Exception as e:
        print(f"Error {e}")


def guardar_archivos_en_formato_json(usuarios: list, eventos: list):
    eventos_serializables = []
    for evento in eventos:
        evento_serializable = evento.copy()
        if isinstance(evento_serializable['hora'], datetime.time):
            evento_serializable['hora'] = evento_serializable['hora'].strftime("%H:%M")
        eventos_serializables.append(evento_serializable)
    info = usuarios + eventos_serializables
    try:
        with open("evento_info_json.json" , mode ="a")as file:
            json.dump(info, file, indent=4)
            print("Archivo json guardado exitosamente")
    
    except Exception as e:
        print(f"Error al intentar guardar el json {e}")
            
        