# clases/rol.py

class Rol:
    def __init__(self, id, nombre):
        self.id = id
        self.nombre = nombre
    
    @staticmethod
    def obtener_nombre(id_rol): #retorna el nombre del rol segun su id
        
        roles = {
            1: "Administrador",
            2: "Usuario Estándar"
        }
        return roles.get(id_rol, "Desconocido")