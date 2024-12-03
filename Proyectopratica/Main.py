import asyncio
try:
    from Evento.usuario import registrar_usuario, buscar_usuario_id
    from Evento.event import registrar_evento, mostrar_cantidad_eventos_registrados
    from Evento.Guardar_info import guardar_informacion
    from Evento.filtusuarios import filtrar_usuarios, filtrar_eventos
    from Evento.Pagos import pagar_evento
    from datetime import datetime

except Exception as e:
    print(f"Error {e}")

def main():
    usuarios = []
    eventos = []

    while True:
        print("\nMenú de opciones:")
        print("1. Registrar usuario")
        print("2. Mostrar usuarios registrados")
        print("3. Buscar usuario por ID")
        print("4. Registrar evento")
        print("5. Mostrar eventos registrados")
        print("6. Mostrar cantidad de eventos registrados")
        print("7. Guardar información")
        print("8. Filtrar usuarios y eventos")
        print("9. Pagar evento")
        print("10. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            registrar_usuarios(usuarios)
        elif opcion == '2':
            mostrar_usuarios(usuarios)
        elif opcion == '3':
            buscar_usuario_por_id(usuarios)
        elif opcion == '4':
            registrar_eventos(usuarios, eventos)
        elif opcion == '5':
            mostrar_eventos(eventos)
        elif opcion == '6':
            mostrar_cantidad_eventos(eventos)
        elif opcion == '7':
            guardar_informacion(usuarios, eventos)
        elif opcion == '8':
            filtrar_usuarios_y_eventos(usuarios, eventos)
        elif opcion == '9':
            pagar_evento_menu(usuarios, eventos)
        elif opcion == '10':
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida, por favor intente de nuevo.")

def registrar_usuarios(usuarios):
    try:
        registrar_usuario(usuarios)
        
    except Exception as e:
        print(f"Error al registrar usuarios: {e}")

def mostrar_cantidad_eventos(eventos):
    try:
        mostrar_cantidad_eventos_registrados(eventos)
    except Exception as e:
        print(f"Error {e}")

def mostrar_usuarios(usuarios):
    for usuario in usuarios:
        print(usuario)

def buscar_usuario_por_id(usuarios):
    try:
        id_buscar = input("\nIngrese el ID del usuario que desea buscar: ")
        buscar_usuario_id(usuarios, id_buscar)
    except Exception as e:
        print(f"Error al buscar usuario: {e}")

def registrar_eventos(usuarios, eventos):
    try:
        registrar_evento(usuarios, eventos)
    except Exception as e:
        print(f"Error al registrar eventos: {e}")

def mostrar_eventos(eventos):
    for evento in eventos:
        print(evento)

def filtrar_usuarios_y_eventos(usuarios, eventos):
    try:
        edad = input("Ingrese edad para buscar usuarios con esta edad: ")
        hora = datetime.strptime(input("Ingrese la hora (HH:MM): "), "%H:%M").time()
        filtrar_usuarios(usuarios, edad)
        print("---------")
        filtrar_eventos(eventos, hora)
    except Exception as e:
        print(f"Error al filtrar usuarios y eventos: {e}")

def pagar_evento_menu(usuarios, eventos):
    try:
        id_usuario = input("Ingrese el ID del usuario que va a pagar el evento: ")
        usuario = buscar_usuario_id(usuarios, id_usuario)
        if not usuario:
            print("Usuario no encontrado.")
            return

        nombre_evento = input("Ingrese el nombre del evento a pagar: ")
        evento = next((e for e in eventos if e['nombre'] == nombre_evento and e['id'] == id_usuario), None)
        if not evento:
            print("Evento no encontrado.")
            return

        asyncio.run(pagar_evento(usuario, evento))
    except Exception as e:
        print(f"Error al pagar evento: {e}")

if __name__ == "__main__":
    main()