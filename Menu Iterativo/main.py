# backend/main.py

from modelos.usuario import Usuario
from servicios.registro import validar_contraseña
from vista.menu import MenuPrincipal

def main():
    menu = MenuPrincipal()
    menu.mostrar()

if __name__ == "__main__":
    main()