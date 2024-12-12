import requests

def give_info(eventos, nombre_evento, ubicacion_evento):
    APY_KEY = f"https://timeapi.io/api/Time/current/zone?timeZone={ubicacion_evento}"

    try:
        response = requests.get(APY_KEY)
        data = response.json()
        

        if response.status_code == 200: 
            return f" Evento {nombre_evento} programado el dia {data['dayOfWeek']} a las {data['time']} en {ubicacion_evento}"

    except Exception as e:
        print(f"Error al consultar la disponibilidad de eventos: {e}")
        return


