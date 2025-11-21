import mysql.connector


class Conexion:

    def __init__(self):
        # REEMPLAZA LOS VALORES DE AQUÍ ABAJO CON TUS DATOS REALES
        self.host = "localhost"         # Generalmente es localhost
        self.port = "3306"              # El puerto por defecto es 3306
        self.user = "root"              # Tu usuario de MySQL
        self.password = ""              # Tu contraseña de MySQL (dejar vacío si no tiene)
        self.database = "bookmatch"     # El nombre de tu base de datos

        # Conexión abierta más reciente (se llena al conectar())
        self._last_conn = None

    def conectar(self):
        try:
            conexion = mysql.connector.connect(
                host=self.host,
                port=self.port,
                user=self.user,
                password=self.password,
                database=self.database
            )
            print("¡Conectado exitosamente!")
            self._last_conn = conexion
            return conexion
        except mysql.connector.Error as err:
            print(f"Error al conectar la base de datos: {err}")
            return None

    def close(self):
        """Cierra la última conexión abierta por esta instancia (si existe)."""
        if self._last_conn:
            try:
                self._last_conn.close()
            except Exception:
                pass
            self._last_conn = None


if __name__ == "__main__":
    db = Conexion()
    conn = db.conectar()
    if conn:
        conn.close()