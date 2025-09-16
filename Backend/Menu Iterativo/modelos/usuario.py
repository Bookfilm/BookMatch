# backend/modelos/usuario.py

from .rol import Rol  # Importa la clase Rol desde el mismo paquete

class Usuario:
    usuarios = {
        'admin': {'contraseña': 'admin123', 'rol': Rol.ADMIN},
        'user1': {'contraseña': 'user123', 'rol': Rol.USUARIO}
    }

    def __init__(self, nombre, contraseña, rol):
        self.nombre = nombre
        self.contraseña = contraseña
        self.rol = rol

    @classmethod
    def existe(cls, nombre):
        return nombre in cls.usuarios

    @classmethod
    def agregar(cls, nombre, contraseña, rol):
        cls.usuarios[nombre] = {'contraseña': contraseña, 'rol': rol}

    @classmethod
    def iniciar_sesion(cls, nombre, contraseña):
        datos = cls.usuarios.get(nombre)
        if datos and datos['contraseña'] == contraseña:
            return cls(nombre, contraseña, datos['rol'])
        return None

    @classmethod
    def eliminar(cls, nombre):
        if nombre in cls.usuarios:
            del cls.usuarios[nombre]
            return True
        return False

    @classmethod
    def cambiar_rol(cls, nombre, nuevo_rol):
        if nombre in cls.usuarios:
            cls.usuarios[nombre]['rol'] = nuevo_rol
            return True
        return False