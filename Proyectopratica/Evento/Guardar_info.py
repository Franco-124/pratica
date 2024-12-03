#guardar información de eventos y usuarios en archivos

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