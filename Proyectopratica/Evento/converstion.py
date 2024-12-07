import requests

def convertir_moneda(eventos, moneda_destino):
    if not eventos:
        print("No hay eventos registrados")
        return

    url = "https://api.exchangerate-api.com/v4/latest/EUR"
    
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an HTTPError for bad responses
        data = response.json()
        
        if not isinstance(data, dict):
            print("Error: La respuesta de la API no es un diccionario")
            return
        
        if 'rates' not in data:
            print("Error: La respuesta de la API no contiene la clave 'rates'")
            return
        
        if moneda_destino not in data['rates']:
            print("No existe ese tipo de moneda en la tasa de cambio")
            return
        
        tasa_conversion = data['rates'][moneda_destino]
        
        for evento in eventos:
            costo_convertido = evento['total_evento'] * tasa_conversion
            print(f"Costo del evento {evento['nombre']} en {moneda_destino}: {costo_convertido}")
    
    except requests.exceptions.RequestException as e:
        print(f"Error al realizar la solicitud: {e}")
    except ValueError as e:
        print(f"Error al procesar la respuesta JSON: {e}")
    except KeyError as e:
        print(f"Error al acceder a los datos de la tasa de conversión: {e}")
    except Exception as e:
        print(f"Error inesperado: {e}")