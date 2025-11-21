from conexion import Conexion
from login import Login
from libro import Libro
from menu_administrador import menu_admin
from menu_usuario import menu_user
from registro import registrarse
from rol import Rol
from conexion import Conexion
from login import Login
from libro import Libro
from menu_administrador import menu_admin
from menu_usuario import menu_user
from registro import registrarse
from rol import Rol


def iniciar_sesion(login_service):
    # Solicita credenciales y autentica al usuario (reintenta en caso de error)
    print("\n--- INICIAR SESIÓN ---")
    intentos = 0
    max_intentos = 3
    try:
        while intentos < max_intentos:
            email = input("Email: ").strip()
            contraseña = input("Contraseña: ").strip()
            usuario = login_service.autenticar(email, contraseña)
            if usuario:
                return usuario
            intentos += 1
            remaining = max_intentos - intentos
            if remaining > 0:
                print(f"\nEmail o contraseña incorrectos. Te quedan {remaining} intento(s). Intenta de nuevo.")
            else:
                print("\nHas alcanzado el límite de intentos de inicio de sesión.")
                return None
    except KeyboardInterrupt:
        print("\nInicio de sesión cancelado. Volviendo al menú...")
        return None


def mostrar_menu_principal():
    # Muestra el menú principal del sistema
    print("\nBOOKMATCH")
    print("1. Iniciar sesión")
    print("2. Registrarse")
    print("3. Ver Libros")
    print("4. Salir")
    return input("\nSeleccione una opción: ").strip()


def registrar_usuario(conexion):
    # Delegar al módulo de registro (el módulo se encarga de pedir los datos)
    print("\nRegistro de Nuevo Usuario")
    registrarse(conexion)


def main():
    conexion = Conexion()
    conn = conexion.conectar()
    if not conn:
        print("No se pudo establecer conexión con la base de datos. El programa se cerrará.")
        return

    login_service = Login(conexion)
    libro_service = Libro(conexion)

    try:
        while True:
            opcion = mostrar_menu_principal()

            if opcion == "1":
                usuario = iniciar_sesion(login_service)
                if usuario:
                    print(f"\n¡Bienvenido, {usuario.nombre}!")
                    if getattr(usuario, 'id_rol', None) == 1:
                        menu_admin(usuario, conexion)
                    else:
                        menu_user(usuario, conexion)
                else:
                    print("\nEmail o contraseña incorrectos.")
            elif opcion == "2":
                registrar_usuario(conexion)
            elif opcion == "3":
                libro_service.listar_libros()
            elif opcion == "4":
                print("\n¡Hasta luego!")
                try:
                    conexion.close()
                except Exception:
                    pass
                break
            else:
                print("\nOpción no válida. Por favor, intenta de nuevo.")
    except KeyboardInterrupt:
        print("\nInterrupción recibida. Cerrando aplicación...")
        try:
            conexion.close()
        except Exception:
            pass


if __name__ == "__main__":
    main()