import requests

def consultar_disponibilidad_eventos_por_fecha(eventos, nombre_evento, ubicacion_evento):
    APY_KEY = f"https://timeapi.io/api/Time/current/zone?timeZone=America/Bogota"

    try:
        response = requests.get(APY_KEY)
        data = response.json()
    except Exception as e:
        print(f"Error al consultar la disponibilidad de eventos: {e}")
        return


