# clases/usuario.py
from conexion import Conexion
from registro import validar_email, validar_contraseña


class Usuario:
    def __init__(self, id, nombre, apellido, email, contraseña, id_rol):
        self.id = id
        self.nombre = nombre
        self.apellido = apellido
        self.email = email
        self.contraseña = contraseña
        self.id_rol = id_rol
    
    
    def ver_datos(self):
        print("\nMIS DATOS")
        print(f"ID: {self.id}")
        print(f"Nombre completo: {self.nombre} {self.apellido}")
        print(f"Email: {self.email}")
        
        rol_nombre = "Administrador" if self.id_rol == 1 else "Usuario Estándar"
        print(f"Rol: {rol_nombre}")

    
    def editar_datos(self, conexion):

        print("EDITAR MIS DATOS")
        print("Dejar vacío para mantener el valor actual\n")
        try:
            nuevo_nombre = input(f"Nombre [{self.nombre}]: ").strip() or self.nombre
            nuevo_apellido = input(f"Apellido [{self.apellido}]: ").strip() or self.apellido
            nuevo_email = input(f"Email [{self.email}]: ").strip() or self.email
            nueva_contraseña = input("Nueva contraseña (dejar vacío para no cambiar): ").strip()
        except KeyboardInterrupt:
            print("\nEdición cancelada. Volviendo al menú...")
            return
        
        # Si no cambia la contraseña, mantener la actual
        if not nueva_contraseña:
            nueva_contraseña = self.contraseña

        # Validar formato de email
        if not validar_email(nuevo_email):
            print("Error: Formato de email inválido. No se actualizaron los datos.")
            return

        # Si se proporcionó una nueva contraseña, validar su fortaleza
        if nueva_contraseña != self.contraseña:
            es_valida, mensaje = validar_contraseña(nueva_contraseña)
            if not es_valida:
                print(f"Error: {mensaje}. No se actualizaron los datos.")
                return
        
        conn = conexion.conectar()
        if not conn:
            print("No se pudo conectar a la base de datos.")
            return
        
        try:
            cursor = conn.cursor()
            sql = """
                UPDATE usuario 
                SET nombre = %s, apellido = %s, email = %s, contraseña = %s
                WHERE usuario_id = %s
            """
            valores = (nuevo_nombre, nuevo_apellido, nuevo_email, nueva_contraseña, self.id)
            cursor.execute(sql, valores)
            conn.commit()
            
            # Actualizar 
            self.nombre = nuevo_nombre
            self.apellido = nuevo_apellido
            self.email = nuevo_email
            self.contraseña = nueva_contraseña
            
            print("\nDatos actualizados correctamente.")
            
        except Exception as err:
            print(f"Error al actualizar datos: {err}")
        finally:
            cursor.close()
            conn.close()
    
    # Métodos solo para Administrador 
    
    @staticmethod
    def listar_usuarios(conexion):
        
        print("USUARIOS REGISTRADOS")
        
        
        conn = conexion.conectar()
        if not conn:
            print("No se pudo conectar a la base de datos.")
            return
        
        try:
            cursor = conn.cursor()
            cursor.execute("""  
                SELECT u.usuario_id, u.nombre, u.apellido, u.email, r.rol
                FROM usuario u
                JOIN rol r ON u.id_rol = r.rol_id
                ORDER BY u.usuario_id
            """)
            usuarios = cursor.fetchall()
            
            if len(usuarios) > 0:
                print(f"{'ID':<5} | {'Nombre':<20} | {'Apellido':<20} | {'Email':<30} | {'Rol':<15}")
                for u in usuarios:
                    print(f"{u[0]:<5} | {u[1]:<20} | {u[2]:<20} | {u[3]:<30} | {u[4]:<15}")
            else:
                print("No hay usuarios registrados.")

            
        except Exception as err:
            print(f"Error al obtener usuarios: {err}")
        finally:
            cursor.close()
            conn.close()
    
    @staticmethod
    def cambiar_rol(conexion, user_id, nuevo_rol):
        conn = conexion.conectar()
        if not conn:
            print("No se pudo conectar a la base de datos.")
            return
        try:
            cursor = conn.cursor()
            sql = "UPDATE usuario SET id_rol = %s WHERE usuario_id = %s"
            cursor.execute(sql, (nuevo_rol, user_id))
            conn.commit()
            print(f"\nRol actualizado correctamente para usuario ID {user_id}.")
        except Exception as err:
            print(f"Error al actualizar rol: {err}")
        finally:
            cursor.close()
            conn.close()
    
    @staticmethod
    def eliminar_usuario(conexion, user_id):
        conn = conexion.conectar()
        if not conn:
            print("No se pudo conectar a la base de datos.")
            return
        try:
            cursor = conn.cursor()
            # Eliminar usuario
            sql = "DELETE FROM usuario WHERE usuario_id = %s"
            cursor.execute(sql, (user_id,))
            conn.commit()
            print(f"\nUsuario ID {user_id} eliminado correctamente.")
        except Exception as err:
            print(f"Error al eliminar usuario: {err}")
        finally:
            cursor.close()
            conn.close()