# backend/vista/menu.py

from usuario import Usuario, Rol
from registro import validar_contraseña

class MenuPrincipal:
    def __init__(self):
        self.menu_administrador = MenuAdministrador()
        self.menu_usuario = MenuUsuario()

    def mostrar(self):
        while True:
            print("\n=== MENÚ PRINCIPAL ===")
            print("1. Registrar usuario")
            print("2. Iniciar sesión")
            print("3. Salir")
            opcion = input("Elige: ")

            if opcion == "1":
                self.registrar_usuario()
            elif opcion == "2":
                nombre, rol = self.iniciar_sesion()
                if nombre is None:
                    continue
                if rol == Rol.ADMIN:
                    self.menu_administrador.mostrar()
                else:
                    self.menu_usuario.mostrar(nombre)
            elif opcion == "3":
                print("¡Hasta luego!")
                break
            else:
                print("Opción no válida.")

    def registrar_usuario(self):
        while True:
            nombre = input("Nombre de usuario: ")
            if Usuario.existe(nombre):
                print("Ese nombre ya existe.")
                continue
            break

        while True:
            contraseña = input("Contraseña (6 caracteres, letras y números): ")
            error = validar_contraseña(contraseña)
            if error:
                print(error)
                continue

            repetir = input("Repite la contraseña: ")
            if contraseña != repetir:
                print("No coinciden las contraseñas.")
                continue
            break

        while True:
            rol = input("Rol (1 = admin, 2 = usuario): ")
            if rol not in ["1", "2"]:
                print("Rol inválido.")
                continue
            if rol == "1":
                clave = input("Contraseña de admin (123): ")
                if clave != "123":
                    print("Contraseña incorrecta.")
                    continue
            break

        Usuario.agregar(nombre, contraseña, int(rol))
        print("")
        print("Usuario registrado con éxito.")

    def iniciar_sesion(self):
        while True:
            print("\n--- INICIAR SESIÓN ---")
            nombre = input("Usuario (o escribí 'salir' para volver al MENÚ PRINCIPAL): ").strip()
            if nombre.lower() == "salir":
                return None, None
            contraseña = input("Contraseña: ").strip()
            usuario = Usuario.iniciar_sesion(nombre, contraseña)
            if usuario:
                return usuario.nombre, usuario.rol
            print("Usuario o contraseña incorrectos.")

class MenuAdministrador:
    def mostrar(self):
        while True:
            print("\nMenú Administrador")
            print("1. Ver usuarios")
            print("2. Cambiar rol")
            print("3. Eliminar usuario")
            print("4. Salir")
            opcion = input("Elige una opción: ")

            if opcion == "1":
                self.ver_usuarios()
            elif opcion == "2":
                self.cambiar_rol()
            elif opcion == "3":
                self.eliminar_usuario()
            elif opcion == "4":
                break
            else:
                print("Opción no válida.")

    def ver_usuarios(self):
        print("\nUsuarios:")
        for nombre, datos in Usuario.usuarios.items():
            rol = "admin" if datos['rol'] == Rol.ADMIN else "usuario"
            print(f" - {nombre} ({rol})")

    def cambiar_rol(self):
        nombre = input("Nombre del usuario: ")
        nuevo_rol = input("Nuevo rol (1 = admin, 2 = usuario): ")
        if nuevo_rol in ["1", "2"]:
            Usuario.cambiar_rol(nombre, int(nuevo_rol))
            print("Rol cambiado.")
        else:
            print("Rol inválido.")

    def eliminar_usuario(self):
        nombre = input("Usuario a eliminar: ")
        if Usuario.eliminar(nombre):
            print("Usuario eliminado.")
        else:
            print("No existe ese usuario.")

class MenuUsuario:
    def mostrar(self, nombre):
        while True:
            print("\nMenú Usuario")
            print("1. Ver mis datos")
            print("2. Salir")
            opcion = input("Elige una opción: ")

            if opcion == "1":
                self.ver_mis_datos(nombre)
            elif opcion == "2":
                break
            else:
                print("Opción no válida.")

    def ver_mis_datos(self, nombre):
        datos = Usuario.usuarios[nombre]
        rol = "admin" if datos['rol'] == Rol.ADMIN else "usuario"
        print(f"Nombre: {nombre}")
        print(f"Rol: {rol}")
        input("\nPresioná ENTER para volver al menú...")