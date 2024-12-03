"""
Vamos a gestionar los pagos de los eventos, usando el presupuesto del usuario 
y el costo total de cada evento

vamos tambien a generar una factura y guardarla en un archivo

parametros: usuarios:list , eventos: list

retornara el dinero descontado y el pago del evento

"""

import asyncio
from datetime import datetime


async def pagar_evento(usuario, evento):
    print(f"Está a punto de hacer el pago del evento {evento['nombre']}")
    if usuario['presupuesto'] >= evento['total_evento']:
        usuario['presupuesto'] -= evento['total_evento']
        await generar_factura(usuario, evento)
        print(f"Evento pagado con éxito a nombre de {usuario['nombre']}, presupuesto restante {usuario['presupuesto']}")
    else:
        print(f"No hay presupuesto suficiente para pagar el evento {evento['nombre']}")

async def generar_factura(usuario, evento):
    try:
        fecha_actual = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        factura = (
            f"------Factura evento----\n"
            f"----------------------------\n"
            f"Responsable: {usuario['nombre']}\n"
            f"Nombre evento: {evento['nombre']}\n"
            f"Fecha: {fecha_actual}\n"
            f"Monto: {evento['total_evento']}\n"
            f"Presupuesto restante: {usuario['presupuesto']}\n"
        )
        archivo = f"{evento['nombre']}_{usuario['nombre']}.txt"
        with open(archivo, 'w') as file:
            file.write(factura)
        print(f"Factura de evento: {evento['nombre']} a nombre de {usuario['nombre']} impresa exitosamente")
    except Exception as e:
        print("Error",e)


