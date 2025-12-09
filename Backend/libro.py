# clases/libro.py
import mysql.connector


class Libro:
    def __init__(self, conexion, libro_id=None, titulo=None, autor=None, isbn=None):
        self.conexion = conexion
        self.libro_id = libro_id
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn
    
    def listar_libros(self):
        conn = self.conexion.conectar()
        if not conn:
            print("No se pudo conectar a la base de datos.")
            return
        
        try:
            cursor = conn.cursor()
            # Unimos con la tabla genero para mostrar el género del libro (si existe)
            cursor.execute(
                """
                SELECT l.libro_id, l.titulo, l.autor, l.isbn, g.nombre as genero
                FROM libro l
                LEFT JOIN genero g ON l.id_genero = g.genero_id
                ORDER BY l.titulo
                """
            )
            libros = cursor.fetchall()
            
            print("\n CATÁLOGO DE LIBROS")

            
            if len(libros) > 0:
                for libro in libros:
                    # fila: (libro_id, titulo, autor, isbn, genero)
                    print(f"\nID: {libro[0]}")
                    print(f"Título: {libro[1]}")
                    print(f"Autor: {libro[2]}")
                    print(f"ISBN: {libro[3]}")
                    print(f"Género: {libro[4] if libro[4] else 'Sin género definido'}")
            else:
                print("No hay libros disponibles en el catálogo.")
            
        except Exception as err:
            print(f"  Error al listar libros: {err}")
        finally:
            cursor.close()
            conn.close()
    
    def agregar_libro(self, titulo, autor, isbn):
        """Agrega un nuevo libro al catálogo (solo Admin)"""
        conn = self.conexion.conectar()
        if not conn:
            return False
        
        try:
            cursor = conn.cursor()
            sql = "INSERT INTO libro (titulo, autor, isbn) VALUES (%s, %s, %s)"
            cursor.execute(sql, (titulo, autor, isbn))
            conn.commit()
            print(f"\nLibro '{titulo}' agregado correctamente.")
            return True
        except mysql.connector.IntegrityError:
            print(f"  Error: El ISBN '{isbn}' ya existe.")
            return False
        except Exception as err:
            print(f"Error al agregar libro: {err}")
            return False
        finally:
            cursor.close()
            conn.close()
    
    def eliminar_libro(self, libro_id):
        """Elimina un libro del catálogo (solo Admin)"""
        conn = self.conexion.conectar()
        if not conn:
            return False
        
        try:
            cursor = conn.cursor()
            sql = "DELETE FROM libro WHERE libro_id = %s"
            cursor.execute(sql, (libro_id,))
            conn.commit()
            
            if cursor.rowcount > 0:
                print(f"\nLibro ID {libro_id} eliminado correctamente.")
                return True
            else:
                print(f"No se encontró libro con ID {libro_id}.")
                return False
        except Exception as err:
            print(f"Error al eliminar libro: {err}")
            return False
        finally:
            cursor.close()
            conn.close()