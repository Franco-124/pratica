import random
import time
from node_queue import Queue

lista_canciones = ["cancion1", "cancion2", "cancion3", "cancion4", "cancion5", "cancion6", "cancion7", "cancion8", "cancion9"]

# Create a global Queue instance
queue = Queue()

def canciones(list: list):
    return random.choice(list)

def add_canciones():
    result_cancion = canciones(lista_canciones)
    queue.enqueue(result_cancion)
    print("Cancion agregada a la lista de reproduccion")

def reproduce_song():
    if queue.count > 0:
        print("Reproduciendo cancion: ", queue.dequeue())
        time.sleep(5)
        print("Cancion eliminada de la lista de reproduccion")
    else:
        print("No hay canciones en la lista de reproduccion")

def main():
    add_canciones()
    add_canciones()
    add_canciones()
    reproduce_song()
    reproduce_song()
    reproduce_song()

main()