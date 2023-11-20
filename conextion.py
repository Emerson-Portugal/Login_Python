import psycopg2

def conexion():
    try:
        credenciales = {
            "dbname": "login",
            "user": "postgres",
            "password": "admin7895",
            "host": "localhost",
            "port": 5432
        }
        conn = psycopg2.connect(**credenciales)
        print("Conexión exitosa")
        return conn  # Devuelve la conexión creada
    except psycopg2.Error as e:
        print("Ocurrió un error al conectar a PostgreSQL: ", e)


def obtener_usuario_por_credenciales(username, password):
    conn = conexion()
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM usuario WHERE nombre = %s AND pass = %s", (username, password))
        user = cursor.fetchone()
        return user
    finally:
        conn.close()

def main():
    # Example of using obtener_usuario_por_credenciales
    user = obtener_usuario_por_credenciales('Emer', '123')
    print(user)

if __name__ == "__main__":
    main()