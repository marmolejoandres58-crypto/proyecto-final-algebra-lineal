import pymysql

DB_CONFIG = {
    'host': 'localhost',
    'database': 'pichadorcito',
    'user': 'root',
    'password': '',
    'port': 3306 
}

def obtener_conexion():
    conexion = None
    try:
        conexion = pymysql.connect(**DB_CONFIG)
        if(conexion.open):
            print("Exito en concexion con la base de datos.")
        return conexion
    except Exception as e:
        print("--- ERROR DE CONEXIÓN CRÍTICO (pymysql) ---")
        print(" Asegúrate de que MySQL/MariaDB esté ENCENDIDO.")
        print(f" Detalle del Error: {e}")
        print("-------------------------------------------------")
        return None