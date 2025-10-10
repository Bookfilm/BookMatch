class crud_menu:
    def __init__(self):
        self.generos = {1: "Ensayos literarios", 2: "Ficción Moderna y contemporánea", 3: "Ciencia-Ficción"}
        self.libros = [
            {"ID": 1, "Titulo": "Archipiélago", "Autor": "Mariana Enriquez", "Año": 2025,
             "Idioma": "Español", "Paginas": 300, "Genero": 1},
            {"ID": 2, "Titulo": "Cómo desaparecer completamente", "Autor": "Mariana Enriquez",
             "Año": 2025, "Idioma": "Español", "Paginas": 200, "Genero": 2},
            {"ID": 3, "Titulo": "El buen mal", "Autor": "Samanta Schweblin",
             "Año": 2025, "Idioma": "Inglés", "Paginas": 192, "Genero": 3}
        ]
        self.id_siguiente = 4
        
    def crear(self, titulo, autor, año, idioma, paginas, genero):
        self.libros.append({
            "ID": self.id_siguiente,
            "Titulo": titulo,
            "Autor": autor,
            "Año": int(año),
            "Idioma": idioma,
            "Paginas": int(paginas),
            "Genero": int(genero)
        })
        self.id_siguiente += 1

    def listar(self):
        for libro in self.libros:
            print(f"{libro['ID']}) {libro['Titulo']} | {libro['Autor']} | {libro['Año']} | "
                  f"{libro['Idioma']} | {libro['Paginas']} págs. | Género: {self.generos[libro['Genero']]}")

    def baja(self, identificador):
        self.libros[:] = [libro for libro in self.libros if libro["ID"] != identificador]

    def modificar(self, identificador, **campos):
        for libro in self.libros:
            if libro["ID"] == identificador:
                for clave, valor in campos.items():
                    if valor is None or valor == "":
                        continue
                    if clave in ("Año", "Paginas", "Genero"):
                        while True:
                            try:
                                numero = int(valor)
                                if clave == "Genero" and numero not in self.generos:
                                    valor = input(f"Género debe ser 1, 2 o 3: ")
                                    continue
                                libro[clave] = numero
                                break
                            except ValueError:
                                valor = input(f"Valor inválido para {clave}. Ingresá solo números: ")
                    else:
                        libro[clave] = valor
                break

    def menu(self):
        while True:
            self.listar()
            print("\n1 Crear | 2 Editar | 3 Borrar | 4 Salir")
            opcion = input(">>> ")
            if opcion == "1":
                print("Crear libro:")
                titulo   = input("Título: ")
                autor    = input("Autor : ")
                año      = input("Año   : ")
                idioma   = input("Idioma: ")
                paginas  = input("Páginas: ")
                print("Géneros: 1 Terror | 2 Romance | 3 Ciencia-Ficción")
                genero   = input("Id gen: ")
                self.crear(titulo, autor, año, idioma, paginas, genero)
                print("Libro agregado.")
            elif opcion == "2":
                print("Editar libro:")
                identificador = int(input("ID a editar: "))
                print("Deja vacío si no querés cambiarlo.")
                titulo   = input("Nuevo título: ")
                autor    = input("Nuevo autor : ")
                año      = input("Nuevo año   : ")
                idioma   = input("Nuevo idioma: ")
                paginas  = input("Nuevas páginas: ")
                genero   = input("Nuevo id gen: ")
                self.modificar(
                    identificador,
                    Titulo=titulo or None,
                    Autor=autor or None,
                    Año=año or None,
                    Idioma=idioma or None,
                    Paginas=paginas or None,
                    Genero=genero or None
                )
                print("Actualizado.")
            elif opcion == "3":
                identificador = int(input("ID a borrar: "))
                self.baja(identificador)
                print("Borrado.")
            elif opcion == "4":
                print("¡Chau!")
                break
            else:
                print("Opción no válida.")