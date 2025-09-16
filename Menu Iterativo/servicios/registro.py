# backend/servicios/registro.py

import re

def validar_contraseña(contraseña):
    if len(contraseña) < 6:
        return "La contraseña debe tener al menos 6 caracteres."
    if not re.search(r'[a-zA-Z]', contraseña):
        return "La contraseña debe tener al menos una letra."
    if not re.search(r'[0-9]', contraseña):
        return "La contraseña debe tener al menos un número."
    return None