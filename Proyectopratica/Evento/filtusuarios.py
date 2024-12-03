#vamos a filtar y mostrar usuarios por edad y eventos por hora de evento

def filtrar_usuarios(usuarios,edad):
    edad=int(edad)
    filtro=[usuario for usuario in usuarios if usuario['edad']==edad]
    print(f"Usuarios registrados con edad igual a {edad}")
    for user in filtro:
        if not user:
            print(f"No hay eventos registrados con edad igual a {edad}")
            return 
        print(user)
        print("-------------------")
        return


def filtrar_eventos(eventos,hora):
    hora_str = hora.strftime("%H:%M")
    filtro=[evento for evento in eventos if evento['hora']==hora]
    print(f"Eventos registrados a las {hora_str}")
    for event in filtro:
        if not event:
            print(f"No hay eventos registrados a las {hora_str}")
            return
        print(event)




