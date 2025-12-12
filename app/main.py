from data_manager import insertar_datos, consultar_datos, cont_id, extract_name

def main():
    
    print("\n--- INSERCIÓN DE DATOS ---")
    
    val_name = ""
    while val_name != False:
        nombre =input("Ingrese el nomre de usuario y presione Enter para insertars su puntaje...")
        nombre = input("Ingrese el nombre de usuario: ")
        val_name = extract_name(nombre)
        if val_name != False:
            print(f"El nombre ya existe. Intente con otro.", {val_name})
    
    print(insertar_datos(cont_id(), nombre, 850))
    
    print("\n--- CONSULTA DE DATOS ---")
    consultar_datos()
    
    print("\n--- OCULTAR DATO (Ej. ID 1) ---")
    
    print("\n--- FIN DEL PROGRAMA ---")

if __name__ == "__main__":
    main()