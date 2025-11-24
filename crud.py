
import os   # Importamos 'os' para interactuar con el sistema operativo (verificar si existen archivos)
import csv  # Importamos 'csv' para manejar archivos de texto separados por comas

# ==============================================================================
# BLOQUE DE INICIALIZACIÓN DE ARCHIVOS
# Este bloque se ejecuta apenas arranca el programa. Su objetivo es asegurar
# que los archivos necesarios existan antes de intentar leerlos.
# ==============================================================================

# 1. Verificamos si NO existe el archivo de login
if not os.path.exists('login.csv'):    
    # Si no existe, lo creamos en modo escritura ('w').
    # newline='' es vital en Windows para evitar filas en blanco extra.
    with open('login.csv', 'w', newline='') as archivo:
        writer = csv.writer(archivo)
        # Escribimos los encabezados (nombres de columnas)
        writer.writerow(['correo', 'contrasena'])
        # Escribimos un usuario administrador por defecto
        writer.writerow(['juacarmona721@gmail.com','1234'])

# 2. Verificamos si NO existe el archivo de usuarios (donde guardaremos la data)
if not os.path.exists('users.csv'):
    with open('users.csv', 'w', newline='') as usuarios:
        writer = csv.writer(usuarios)
        # Escribimos los encabezados para la base de datos de usuarios
        writer.writerow(['nombres', 'apellidos', 'correos'])
        # Escribimos un usuario de ejemplo
        writer.writerow(['juan esteban', 'carmona graciano', 'juancarmona721@gmail.com'])

# ==============================================================================
# FUNCIÓN: LOGIN
# Maneja la autenticación del usuario.
# Retorna: True si la contraseña es correcta.
# ==============================================================================
def login():
    """
    Pide credenciales al usuario y las compara con el archivo login.csv.
    Permite un máximo de 3 intentos fallidos.
    """
    count = 0  # Contador de intentos fallidos
    
    while True: # Ciclo infinito: no saldremos de aquí hasta entrar o fallar 3 veces
        print("===INICIO DE SESION===")
        mail_input = input("Ingrese correo electronico: ")
        password_input = input("Ingrese contraseña: ")
        
        login = False  # Bandera (flag) para saber si encontramos al usuario
        
        # Abrimos el archivo en modo LECTURA ('r')
        with open('login.csv', 'r') as archivo:
            reader = csv.reader(archivo)
            next(reader)  # ¡IMPORTANTE! Saltamos la primera fila (los encabezados) para no compararlos
            
            # Recorremos fila por fila buscando coincidencias
            for fila in reader:
                # fila[0] es el correo, fila[1] es la contraseña en el archivo
                if mail_input == fila[0] and password_input == fila[1]:
                    login = True
                    print("Bienvenido!!! datos ingresados correctamente")
                    return True  # Retornamos éxito y salimos de la función inmediatamente
        
        # Si terminamos de leer todo el archivo y la bandera 'login' sigue en False:
        if login == False:
            print("ERROR: correo o contraseña incorrectos")
            count += 1  # Aumentamos el contador de errores
            print(f"llevas {count} intentos de 3")
            
            # Si llegamos al límite de intentos
            if count >= 3:
                print("limite de intentos alcanzado. intente de nuevo mas tarde")
                break  # Rompemos el ciclo while y el programa terminará

# ==============================================================================
# FUNCIÓN: MENU PRINCIPAL
# Contiene toda la lógica del CRUD (Crear, Leer, Actualizar, Borrar)
# ==============================================================================
def main_menu():
    """
    Muestra las opciones disponibles y ejecuta la lógica según la elección del usuario.
    """
    while True: # Ciclo infinito para que el menú vuelva a aparecer después de cada acción
        print("\n--- MENU CRUD ---")
        print("1. Crear usuario")
        print("2. Listar usuarios")
        print("3. Actualizar usuario")
        print("4. Eliminar usuario")
        print("5. Buscar usuario")
        print("6. Salir")
        
        # Convertimos la entrada a entero para comparar con los números
        choice = int(input("Ingrese una opcion: "))
        
        # --- OPCIÓN 1: CREAR (CREATE) ---
        if choice == 1:
            print("CREACION DE USUARIO")
            # Abrimos en modo 'a' (APPEND/AGREGAR) para escribir al final sin borrar lo anterior
            with open ('users.csv', 'a', newline='') as usuarios:
                writer = csv.writer(usuarios)
                
                # Pedimos los datos
                user_name = input("\ningrese el nombre del usuario: ")
                user_last_name = input("\ningrese apellidos del usario: ")
                user_mail = input("\ningrese correo del usuario: ")
                
                # Escribimos la nueva fila directamente
                writer.writerow([user_name , user_last_name , user_mail])
                print(f"\nEXITO! usuario {user_name} creado correctamente")
                
        # --- OPCIÓN 2: LISTAR (READ ALL) ---
        elif choice == 2:
            # Abrimos en modo lectura ('r')
            with open('users.csv', 'r') as usuarios:
                reader = csv.reader(usuarios)
                # Recorremos e imprimimos cada fila (lista de datos)
                for user in reader:
                    print(f"USUARIO: {user}")
                    
        # --- OPCIÓN 3: ACTUALIZAR (UPDATE) ---
        elif choice == 3:
            search_email = input("ingrese el email del usuario: ")
            
            # PASO 1: LEER TODO A LA MEMORIA
            with open('users.csv', 'r') as usuarios:
                # Convertimos todo el archivo a una LISTA de listas llamada 'data'
                # Esto es necesario porque para editar, necesitamos reescribir todo el archivo luego
                data = list(csv.reader(usuarios))
                
                found = False # Bandera para saber si lo encontramos
                
                # 'enumerate' nos da el índice (i) y el contenido (fila) al mismo tiempo
                for i, fila in enumerate(data):
                    # Validamos len(fila) > 2 para evitar errores con filas vacías
                    # Comparamos fila[2] (el correo) con lo que buscamos
                    if len(fila) > 2 and fila[2] == search_email:
                        print("===USUARIO ENCONTRADO===")
                        print(f"datos actuales {fila}")
                        
                        print("--NUEVA INFO DEL USUARIO--")
                        # Lógica para mantener el dato anterior si el usuario presiona Enter vacío
                        new_name = input("Ingrese el nuevo nombre (ENTER SI NO MODIFICA): ")
                        if new_name == "":
                            new_name = fila[0] # Mantiene el nombre original
                            
                        new_last_name = input("Ingrese nuevo apellido (ENTER SI NO MODIFICA): ")
                        if new_last_name == "":
                            new_last_name = fila[1] # Mantiene el apellido original
                            
                        new_mail = input("Ingrese nuevo correo (ENTER SI NO MODIFICA): ")
                        if new_mail == "":
                            new_mail = fila[2] # Mantiene el correo original
                            
                        # Modificamos la lista en la memoria RAM (en la posición 'i')
                        data[i] = [new_name, new_last_name, new_mail]
                        found = True
                        break # Dejamos de buscar porque ya lo encontramos
                
                # PASO 2: SOBRESCRIBIR EL ARCHIVO
                if found:
                    # Abrimos en modo 'w' (WRITE) que borra todo y escribe desde cero
                    with open('users.csv', 'w', newline='') as usuarios:
                        writer = csv.writer(usuarios)
                        writer.writerows(data) # Escribimos la lista 'data' ya modificada
                    print("\nUSUARIO ACTUALIZADO")
                else:
                    print("ERROR: usuario no encontrado")          
    
        # --- OPCIÓN 4: ELIMINAR (DELETE) ---
        elif choice == 4:
            search_email = input("Ingrese el correo del usuario: ")
            
            # PASO 1: LEER TODO A MEMORIA
            with open('users.csv', 'r') as usuarios:
                data = list(csv.reader(usuarios)) # Cargamos todo en la lista 'data'
                found = False
                
                for i, fila in enumerate(data):
                    if len(fila) > 2 and fila[2] == search_email:
                        found = True
                        data.pop(i) # Eliminamos la fila específica de la lista en memoria
                        break # Salimos del ciclo
                        
                # PASO 2: SOBRESCRIBIR SI HUBO CAMBIOS
                if found:
                    with open('users.csv', 'w', newline='') as usuarios:
                        writer = csv.writer(usuarios)
                        writer.writerows(data) # Guardamos la lista 'data' (que ya tiene un usuario menos)
                        print("usuario ENCONTRADO y ELIMINADO")
                else:        
                    print(f"Usuario {search_email} no existe. Intente de nuevo ")
                    
        # --- OPCIÓN 5: BUSCAR (SEARCH - READ ONE) ---
        elif choice == 5:
            search_email = input("Ingrese el correo del usuario: ")
            
            with open('users.csv','r') as usuarios: 
                # Usamos DictReader para acceder por nombre de columna (ej: fila['correos'])
                # Esto hace el código más legible que usar índices numéricos
                reader = csv.DictReader(usuarios)
                for fila in reader:
                    if fila['correos'] == search_email:
                        print("USUARIO ENCONTRADO")
                        print(f"\nEl usuario es {fila['nombres']} {fila['apellidos']}")
        
        # --- OPCIÓN 6: SALIR ---
        elif choice == 6:
            print("==HASTA LUEGO==")
            break # Rompe el ciclo while True y termina la función main_menu

# ==============================================================================
# PUNTO DE ENTRADA (ENTRY POINT)
# Aquí comienza la ejecución real del programa
# ==============================================================================
if login() == True:  # Ejecuta login(). Si retorna True...
    main_menu()      # ...entonces permite entrar al menú principal.