# registro.py
from conexion import Conexion
import re


def validar_email(email): 
    patron = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(patron, email) is not None

def validar_contraseña(contraseña):
   
    if len(contraseña) < 8:
        return False, "La contraseña debe tener al menos 8 caracteres"
    
    if not any(c.isupper() for c in contraseña):
        return False, "Debe contener al menos una letra mayúscula"
    
    if not any(c.islower() for c in contraseña):
        return False, "Debe contener al menos una letra minúscula"
    
    if not any(c.isdigit() for c in contraseña):
        return False, "Debe contener al menos un número"
    
    return True, "Contraseña válida"


def registrarse(conexion): #registra nuevo usuario
    

    print("REGISTRO DE NUEVO USUARIO")    
    intentos = 0
    max_intentos = 3
    
    while intentos < max_intentos:
        # Solicitar datos
        try:
            nombre = input("\nNombre: ").strip()
            apellido = input("Apellido: ").strip()
            email = input("Email: ").strip()
            contraseña = input("Contraseña (mín. 8 caracteres, letras y números): ").strip()
        except KeyboardInterrupt:
            print("\nRegistro cancelado. Volviendo al menú...")
            return
        
        # Validar campos vacíos
        if not all([nombre, apellido, email, contraseña]):
            print("Error: No se permiten campos vacíos.")
            intentos += 1
            continue
        
        # Validar email
        if not validar_email(email):
            print("Error: Formato de email inválido.")
            intentos += 1
            continue
        
        # Validar contraseña
        es_valida, mensaje = validar_contraseña(contraseña)
        if not es_valida:
            print(f"Error: {mensaje}")
            intentos += 1
            continue
        
        # Confirmar contraseña
        confirmar = input("Confirmar contraseña: ").strip()
        if contraseña != confirmar:
            print("Error: Las contraseñas no coinciden.")
            intentos += 1
            continue

        # Elegir rol
        print("\nSeleccioná el rol para este usuario:")
        print("1. Administrador")
        print("2. Usuario Estándar")
        id_rol = None
        while id_rol is None:
            try:
                opcion_rol = input("Ingrese 1 o 2 (por defecto 2): ").strip()
            except KeyboardInterrupt:
                print("\nRegistro cancelado. Volviendo al menú...")
                return
            if opcion_rol == "":
                id_rol = 2
            elif opcion_rol in ("1", "2"):
                id_rol = int(opcion_rol)
            else:
                print("Opción de rol inválida. Ingrese 1 o 2.")
        
        # Intentar registrar en la base de datos
        conn = conexion.conectar()
        if conn is None:
            print("No se pudo conectar a la base de datos.")
            return
        
        try:
            cursor = conn.cursor()
            
            # Verificar si el email ya existe
            cursor.execute("SELECT email FROM usuario WHERE email = %s", (email,))
            if cursor.fetchone():
                print(f"Error: El email '{email}' ya está registrado.")
                intentos += 1
                cursor.close()
                conn.close()
                continue
            
            # Insertar nuevo usuario con el rol elegido
            sql = """
                INSERT INTO usuario (nombre, apellido, email, contraseña, id_rol) 
                VALUES (%s, %s, %s, %s, %s)
            """
            valores = (nombre, apellido, email, contraseña, id_rol)
            cursor.execute(sql, valores)
            conn.commit()
            
            print("\n¡Registro exitoso!")
            print(f"Bienvenido/a, {nombre} {apellido}")
            print("Ya puedes iniciar sesión con tu email y contraseña.")
            
            cursor.close()
            conn.close()
            return
            
        except Exception as err:
            print(f"Error al registrar usuario: {err}")
            intentos += 1
        finally:
            if conn and conn.is_connected():
                conn.close()
    
    print(f"\nHas alcanzado el límite de {max_intentos} intentos.")
    print("Por favor, intenta nuevamente más tarde.")


if __name__ == "__main__":
    db = Conexion()
    registrarse(db)