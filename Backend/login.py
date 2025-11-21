# servicios/login.py
from usuario import Usuario
import mysql.connector


class Login:
    def __init__(self, conexion):
        self.conexion = conexion
    
    def autenticar(self, email, contraseña):
        """Autentica un usuario por email y contraseña"""
        try:
            conn = self.conexion.conectar()
            if not conn:
                print("No se pudo conectar a la base de datos.")
                return None
            
            cursor = conn.cursor()
            query = """
                SELECT usuario_id, nombre, apellido, email, contraseña, id_rol
                FROM usuario 
                WHERE email = %s
            """
            cursor.execute(query, (email,))
            resultado = cursor.fetchone()
            
            cursor.close()
            conn.close()
            
            if not resultado:
                print("Usuario no encontrado.")
                return None
            
            usuario_id, nombre, apellido, email_db, password_db, id_rol = resultado
            
            # Verificar contraseña
            if contraseña != password_db:
                print("Contraseña incorrecta.")
                return None
            
            # Crear Usuario
            usuario = Usuario(
                id=usuario_id,
                nombre=nombre,
                apellido=apellido,
                email=email_db,
                contraseña=password_db,
                id_rol=id_rol
            )
            
            print(f"\nBienvenido/a, {usuario.nombre} {usuario.apellido}!")
            return usuario
            
        except mysql.connector.Error as err:
            print(f"Error al autenticar: {err}")
            return None