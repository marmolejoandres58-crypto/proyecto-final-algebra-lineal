from conexion import obtener_conexion 
from datetime import datetime
import pymysql

def cont_id():
    conexion = obtener_conexion()
    
    if not conexion:
        print("Fallo al obtener conexión para CONTAR ID.")
        return 0

    try:
        with conexion.cursor() as cursor:
            cursor.execute("SELECT COUNT(*) FROM puntajes_usuarios")
            (total_registros,) = cursor.fetchone()
            return total_registros + 1
            
    except Exception as e:
        print(f"Error al contar IDs: {e}")
        return 0
        
    finally:
        if conexion:
            conexion.close()

def extract_name(filename):
    retornable = False
    conexion = obtener_conexion()
    if not conexion:
        print("Fallo al obtener conexión para CONTAR ID.")
        return 0

    try:
        with conexion.cursor() as cursor:
            sql = "SELECT nombre FROM puntajes_usuarios WHERE nombre = %s"
            cursor.execute(sql, (filename,))
            result = cursor.fetchone()
            if result:
                retornable = result
    except Exception as e:
        print(f"Error al extraer nombre: {e}")

    return retornable

def insertar_datos(id, nombre, puntaje):
    """Inserta un nuevo registro de puntaje, manejando su propia conexión."""
    conexion = obtener_conexion()
    
    if not conexion:
        return "Fallo al obtener conexión para INSERTAR."

    try:
        with conexion.cursor() as cursor:
            fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            sql = "INSERT INTO puntajes_usuarios (id_puntajes, nombre, puntaje, fecha, estado) VALUES (%s, %s, %s, %s, %s)"
            valores = (id, nombre, puntaje, fecha, 1)
            cursor.execute(sql, valores)
            conexion.commit()
            return f"Registro insertado: {nombre} - {puntaje} puntos"
            
    except Exception as e:
        conexion.rollback() 
        return f"Error al insertar (Verifica tabla/estructura): {e}"
        
    finally:
        if conexion:
            conexion.close()
            
            
def consultar_datos():
    """Consulta y muestra los puntajes visibles, manejando su propia conexión."""
    conexion = obtener_conexion()
    
    if not conexion:
        print("Fallo al obtener conexión para CONSULTAR.")
        return []
    
    datos = []
    try:
        with conexion.cursor() as cursor:
            cursor.execute("SELECT id_puntajes, nombre, puntaje, fecha, estado FROM puntajes_usuarios WHERE estado = 1 ORDER BY puntaje DESC LIMIT 10")
            datos = cursor.fetchall()
            
    except Exception as e:
        print(f"Error al consultar: {e}")
        
    finally:
        if conexion:
            conexion.close()

    print("\nPuntajes visibles (Ranking):")
    print("-" * 70)
    if datos:
        for fila in datos:
            fecha_formateada = fila[3].strftime("%Y-%m-%d %H:%M:%S")
            print(f"Nombre: {fila[1]:<15} | Puntaje: {fila[2]:<6} | Fecha: {fecha_formateada}")
    else:
        print("No se encontraron puntajes visibles.")
        
    return datos


def ocultar_puntaje(id_puntaje):
    conexion = obtener_conexion()
    
    if not conexion:
        return "Fallo al obtener conexión para OCULTAR."

    try:
        with conexion.cursor() as cursor:
            sql = "UPDATE puntajes_usuarios SET estado = 0 WHERE id_puntajes = %s"
            cursor.execute(sql, (id_puntaje,))
            
            if cursor.rowcount > 0:
                conexion.commit()
                return f"Puntaje {id_puntaje} ocultado"
            else:
                conexion.rollback()
                return f"Aviso: No se encontró el Puntaje {id_puntaje} para ocultar."
                
    except Exception as e:
        conexion.rollback()
        return f"Error al ocultar: {e}"
        
    finally:
        if conexion:
            conexion.close()