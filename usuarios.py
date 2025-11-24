import csv

# --- CONFIGURACIÓN ---
USUARIOS_CSV = "usuarios.csv"

# --- FUNCIONES ---
def cargar_usuarios(nombre_archivo):
    """Carga los usuarios desde el archivo CSV y los devuelve como una lista de diccionarios."""
    usuarios = []
    try:
        # 'r' para modo lectura
        with open(nombre_archivo, mode='r', newline='', encoding='utf-8') as archivo:
            lector = csv.DictReader(archivo)
            for fila in lector:
                usuarios.append(fila)
    except FileNotFoundError:
        # Si el archivo no existe, simplemente devuelve una lista vacía
        pass
    return usuarios

def registrar_usuario(nombre_archivo, usuarios):
    """Permite registrar un nuevo usuario y lo añade al CSV."""
    print("\n--- REGISTRO ---")
    nuevo_usuario = input("Nuevo Usuario: ").strip()
    nueva_clave = input("Nueva Contraseña: ").strip()
    
    # Validación de unicidad
    if any(u['usuario'] == nuevo_usuario for u in usuarios):
        print("Error: El usuario ya existe.")
        return

    nuevo_registro = {'usuario': nuevo_usuario, 'contrasena': nueva_clave}
    
    # Escribir en el CSV
    try:
        # 'a' (append) para añadir al final del archivo
        with open(nombre_archivo, mode='a', newline='', encoding='utf-8') as archivo:
            escritor = csv.DictWriter(archivo, fieldnames=['usuario', 'contrasena'])
            
            # Nota: Si el archivo es nuevo, podría ser necesario escribir el encabezado aquí.
            # Para este ejemplo, asumimos que 'usuarios.csv' inicial ya tiene el encabezado.
            escritor.writerow(nuevo_registro)
            print(f"\nUsuario '{nuevo_usuario}' registrado con éxito.")
    except Exception as e:
        print(f"Error al escribir en el archivo: {e}")
        
    # Actualiza la lista en memoria
    usuarios.append(nuevo_registro)


def iniciar_sesion(usuarios):
    """Solicita credenciales y valida contra la lista de usuarios."""
    print("\n--- INICIO DE SESIÓN ---")
    nombre_usuario = input("Usuario: ").strip()
    contraseña = input("Contraseña: ").strip()
    
    for usuario_existente in usuarios:
        if usuario_existente['usuario'] == nombre_usuario and usuario_existente['contrasena'] == contraseña:
            print(f"\nBienvenido(a), {nombre_usuario}!")
            return True, nombre_usuario
    
    print("\nError: Usuario o contraseña incorrectos.")
    return False, None

# --- MENÚ PRINCIPAL ---
def main():
    usuarios = cargar_usuarios(USUARIOS_CSV)
    
    while True:
        print("\n====================")
        print("1. Iniciar Sesión")
        print("2. Registrar Nuevo Usuario")
        print("3. Salir")
        print("====================")
        
        opcion = input("Elige una opción: ").strip()

        if opcion == '1':
            iniciar_sesion(usuarios)
        elif opcion == '2':
            registrar_usuario(USUARIOS_CSV, usuarios) 
        elif opcion == '3':
            print("Saliendo del programa. Mucha suerte en tu examen!")
            break
        else:
            print("Opción no válida.")

if __name__ == "__main__":
    main()
