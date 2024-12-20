import asyncio
import getpass
from Evento.UI import  Register,buscar_usuario_id
from Evento.event import registrar_evento, mostrar_cantidad_eventos_registrados, eliminar_evento, mostrar_eventos_for_tipo 
from Evento.Guardar_info import guardar_informacion, guardar_archivos_en_formato_json
from Evento.filtusuarios import filtrar_usuarios, filtrar_eventos, filtrar_numero_evento_por_tipo
from Evento.Pagos import pagar_evento
from datetime import datetime
from Evento.converstion import convertir_moneda
from Evento.Grafica import generate_bar_chart, generate_pie_chart
#from Evento.notifier import send_reminder


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
        print("10. Eliminar evento")
        print("11. Ver costo de evento en otra moneda")
        print("12. Crear grafica bar de eventos")
        print("13 Crear grafica pie de eventos")
        print("14. Filtrar eventos por tipo")
        print("15. Enviar recordatorio de eventos")
        print("16. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            registrar_usuarios(usuarios)
        elif opcion == '2':
            mostrar_usuarios(usuarios)
        elif opcion == '3':
            buscar_usuarios(usuarios)
        elif opcion == '4':
            registrar_eventos(usuarios, eventos)
        elif opcion == '5':
            mostrar_eventos(eventos)
        elif opcion == '6':
            mostrar_cantidad_eventos(eventos)
        elif opcion == '7':
            guardar_informacion_Evento(usuarios, eventos)
        elif opcion == '8':
            filtrar_usuarios_y_eventos(usuarios, eventos)
        elif opcion == '9':
            pagar_evento_menu(usuarios, eventos)
        elif opcion == '10':
            event_name = input("Ingrese el nombre del evento que desea eliminar: ")
            eliminar_eventos(eventos, event_name)
        elif opcion == "11":
            moneda_destino = str(input("Ingrese la moneda a la que desea convertir el costo del evento ejemplo(USD,EUR,COP): "))
            convertir_monedas(eventos, moneda_destino)
        elif opcion == '12':
            generate_bar_charts(eventos)
        elif opcion == '13':
            generate_pie_charts(eventos)
        elif opcion=="14":
            tipo_evento = input("Ingrese el tipo de evento que desea filtrar: ")
            filtrar_eventos_por_tipo(eventos, tipo_evento)
        
        elif opcion == '15':
            try:
                print("Saliendo del sistema")
                #guardar_archivos_en_formato_json(usuarios, eventos)
                guardar_informacion(usuarios , eventos)
                break
            except Exception as e:
                print(f"Error {e}")
        else:
            print("Opción no válida, por favor intente de nuevo.")

def registrar_usuarios(usuarios):
    try:
        Register.create_user_registration(usuarios)
    except Exception as e:
        print(f"Error al registrar usuarios: {e}")

    
def guardar_informacion_Evento(usuarios, eventos):
    try:
        guardar_informacion(usuarios, eventos)
    except Exception as e:
        print(f"Error al guardar información: {e}")

def mostrar_cantidad_eventos(eventos):
    try:
        mostrar_cantidad_eventos_registrados(eventos)
    except Exception as e:
        print(f"Error {e}")

def mostrar_usuarios(usuarios):
    for usuario in usuarios:
        print(usuario)

def buscar_usuarios(usuarios):
    try:
        id_buscar = getpass.getpass("\nIngrese el ID del usuario que desea buscar: ")
        buscar_usuario_id(usuarios, id_buscar)
    except Exception as e:
        print(f"Error al buscar usuario: {e}")

def registrar_eventos(usuarios, eventos):
    try:
        registrar_evento(usuarios, eventos)
    except Exception as e:
        print(f"Error al registrar eventos: {e}")

def mostrar_eventos(eventos):
    if eventos:
        for evento in eventos:
            print(f"Eventos registrado \n {evento}")
    else:
        print("No hay eventos registrados")

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
        id_usuario = getpass.getpass("Ingrese el ID del usuario que va a pagar el evento: ")
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

def eliminar_eventos(eventos, evento):
    try:
        eliminar_evento(eventos, evento)
    except Exception as e:
        print(f"Error al eliminar evento: {e}")

def convertir_monedas(eventos, moneda_destino):
    try:
        convertir_moneda(eventos, moneda_destino)
    except Exception as e:
        print(f"Error al convertir moneda: {e}")

def generate_bar_charts(eventos):
    numero_eventos_tipo = filtrar_numero_evento_por_tipo(eventos)
    # Extraer las etiquetas y los valores
    tipos_evento = list(numero_eventos_tipo.keys())
    numero_eventos = list(numero_eventos_tipo.values())
    generate_bar_chart(tipos_evento, numero_eventos)

def generate_pie_charts(eventos):
    numero_eventos_tipo = filtrar_numero_evento_por_tipo(eventos)
    # Extraer las etiquetas y los valores
    tipos_evento = list(numero_eventos_tipo.keys())
    numero_eventos = list(numero_eventos_tipo.values())
    generate_pie_chart(tipos_evento, numero_eventos)


def filtrar_eventos_por_tipo(eventos, tipo_evento):
    try:
        mostrar_eventos_for_tipo(eventos, tipo_evento)
    except Exception as e:
        print(f"Error al filtrar eventos por tipo: {e}")

if __name__ == "__main__":
    main()