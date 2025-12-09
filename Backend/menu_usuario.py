# servicios/menu_usuario.py
from libro import Libro


def menu_user(usuario, conexion):
    #Menú principal para usuarios estándar
    while True:
        print("MENÚ USUARIO")
        print("1. Ver mis datos")
        print("2. Editar mis datos")
        print("3. Ver catálogo de libros")
        print("4. Cerrar sesión")
        
        opcion = input("\nSeleccione una opción: ").strip()
        
        if opcion == "1":
            usuario.ver_datos()
        
        elif opcion == "2":
            usuario.editar_datos(conexion)
        
        elif opcion == "3":
            libro = Libro(conexion)
            libro.listar_libros()
        
        elif opcion == "4":
            print("\nSesión cerrada.")
            break
        
        else:
            print("Opción inválida. Intente de nuevo.")