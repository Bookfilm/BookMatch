# servicios/menu_administrador.py
from usuario import Usuario
from libro import Libro


def menu_admin(usuario, conexion):
    #Menú principal para administradores
     while True:
        print("\nMenú administrador")
        print("1. Ver mis datos personales")
        print("2. Editar mis datos personales")
        print("3. Ver todos los usuarios")
        print("4. Cambiar rol de un usuario")
        print("5. Eliminar usuario")
        print("6. Ver catálogo de libros")
        print("7. Agregar nuevo libro")
        print("8. Eliminar libro")
        print("9. Cerrar sesión")
        
        opcion = input("\nSeleccione una opción: ").strip()
        
        if opcion == "1":
            usuario.ver_datos()
    
        elif opcion == "2":
            usuario.editar_datos(conexion)

        elif opcion == "3":
            Usuario.listar_usuarios(conexion)
        elif opcion == "4":
            try:
                user_id = int(input("\nIngrese ID del usuario: ").strip())
                print("\nRoles disponibles:")
                print("1 = Administrador")
                print("2 = Usuario Estándar")
                nuevo_rol = int(input("Nuevo rol: ").strip())
                if nuevo_rol in [1, 2]:
                    Usuario.cambiar_rol(conexion, user_id, nuevo_rol)
                else:
                    print("Rol inválido. Debe ser 1 o 2.")
            except ValueError:
                print("Debe ingresar números válidos.")
        
        elif opcion == "5":
            try:
                user_id = int(input("\nIngrese ID del usuario a eliminar: ").strip())
                confirm = input(f"¿Está seguro de eliminar usuario ID {user_id}? (s/n): ").strip().lower()
                if confirm == "s":
                    Usuario.eliminar_usuario(conexion, user_id)
                else:
                    print("Operación cancelada.")
            except ValueError:
                print("Debe ingresar un ID válido.")
        
        elif opcion == "6":
            libro = Libro(conexion)
            libro.listar_libros()
        elif opcion == "7":
            print("\nAGREGAR NUEVO LIBRO")
            titulo = input("Título: ").strip()
            autor = input("Autor: ").strip()
            isbn = input("ISBN (13 dígitos): ").strip()
            
            if all([titulo, autor, isbn]):
                libro = Libro(conexion)
                libro.agregar_libro(titulo, autor, isbn)
            else:
                print("Todos los campos son obligatorios.")
        
        elif opcion == "8":
            try:
                libro_id = int(input("\nIngrese ID del libro a eliminar: ").strip())
                confirm = input(f"¿Está seguro de eliminar el libro ID {libro_id}? (s/n): ").strip().lower()
                if confirm == "s":
                    libro = Libro(conexion)
                    libro.eliminar_libro(libro_id)
                else:
                    print("Operación cancelada.")
            except ValueError:
                print("Debe ingresar un ID válido.")
        
        elif opcion == "9":
            print("\nSesión cerrada.")
            break
        
        else:
            print("Opción inválida. Intente de nuevo.")