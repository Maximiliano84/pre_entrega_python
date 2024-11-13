import random 
from colorama import Fore, Style, init

init(autoreset=True)

salir = False 

while not salir:
    inventario_ids = []          
    inventario_nombres = []       
    inventario_cantidades = []  

    # Agregar productos hasta que se elija "Realizar compra"
    while True:
        print(Fore.CYAN + "\n--- Ingreso de Productos ---" + Style.RESET_ALL)
        nombre = input("Ingrese el nombre del producto: ")

        # Agregar la "Cantidad"
        while True:
            try:
                cantidad = int(input("Ingrese la cantidad de este producto: "))
                if cantidad <= 0:
                    print(Fore.RED + "Error: Debe elegir al menos un producto." + Style.RESET_ALL)
                else:
                    break 
            except ValueError:
                print(Fore.RED + "Error: Inténtelo nuevamente ingresando un número válido." + Style.RESET_ALL)

        # ID aleatorio
        id_producto = random.randint(1000, 9999)
        
        # Añadimos el producto a las listas
        inventario_ids.append(id_producto)
        inventario_nombres.append(nombre)
        inventario_cantidades.append(cantidad)
        print(Fore.GREEN + f"\nProducto '{nombre}' agregado con éxito: (ID: {id_producto})." + Style.RESET_ALL)

        # Mostrar lista
        print(Fore.YELLOW + "\n--- Lista de Productos ---")
        print(f"{'ID':<8}{'Producto':<20}{'Cantidad':<10}")
        print("-" * 40 + Style.RESET_ALL)
        for i in range(len(inventario_ids)):
            print(f"{Fore.CYAN}{inventario_ids[i]:<8}{inventario_nombres[i]:<20}{inventario_cantidades[i]:<10}")

        # Continuar realizar la compra
        continuar = input("\n¿Desea agregar otro producto? (si / no, realizar el pedido): ")
        if continuar.lower() not in ["s", "si"]:
            break

    # Mostrar el inventario completo
    while True:
        print(Fore.YELLOW + "\n--- Total de Productos ---")
        print(f"{'ID':<8}{'Producto':<20}{'Cantidad':<10}")
        print("-" * 40 + Style.RESET_ALL)
        for i in range(len(inventario_ids)):
            print(f"{Fore.CYAN}{inventario_ids[i]:<8}{inventario_nombres[i]:<20}{inventario_cantidades[i]:<10}")

        # Menú de opciones dentro de la lista
        if len(inventario_ids) > 0:
            print(Fore.MAGENTA + "\n--- Opciones de Lista ---" + Style.RESET_ALL)
            print("1. Realizar Pedido")
            print("2. Eliminar Producto")
            print("3. Vaciar Inventario")
            print("4. Agregar Productos")
            print("5. Salir")
            print("-------------------------------------")

            opcion_inventario = input("Seleccione una opción (1, 2, 3, 4 o 5): ")

            # Opción para "comprar"
            if opcion_inventario == "1":
                if len(inventario_ids) > 0: 
                    # Eliminar todo el inventario de ID, nombres y cantidades
                    inventario_ids.clear()
                    inventario_nombres.clear()
                    inventario_cantidades.clear()
                    print(Fore.GREEN + "\n--- PEDIDO REALIZADO CON ÉXITO ---" + Style.RESET_ALL)

                    # Preguntar si desea realizar otro pedido
                    otra_compra = input("\n¿Desea realizar otro pedido? (si / no): ")
                    if otra_compra.lower() in ["s", "si"]:
                        # Si desea hacer otro pedido, se reinicia el sistema
                        print("\nIniciando un nuevo pedido...")
                        break 
                    else:
                        print(Fore.GREEN + "\nMuchas gracias por elegirnos!!!" + Style.RESET_ALL)
                        salir = True 
                        break
                else:
                    print(Fore.RED + "El inventario está vacío. No se puede realizar un pedido." + Style.RESET_ALL)

            # Opción para "eliminar"
            elif opcion_inventario == "2":
                if len(inventario_ids) == 0:
                    print(Fore.RED + "El inventario está vacío. No hay productos para eliminar." + Style.RESET_ALL)
                else:
                    # Mostrar los productos
                    print(Fore.YELLOW + "\nSeleccione el número del producto que desea eliminar:" + Style.RESET_ALL)
                    print(f"{'No.':<5}{'ID':<8}{'Producto':<20}{'Cantidad':<10}")
                    print("-" * 50 + Style.RESET_ALL)
                    for i in range(len(inventario_ids)):
                        print(f"{i+1:<5}{Fore.CYAN}{inventario_ids[i]:<8}{inventario_nombres[i]:<20}{inventario_cantidades[i]:<10}")

                    # Solicitar al usuario seleccionar el producto a eliminar
                    try:
                        producto_a_eliminar = int(input("Ingrese el número del producto a eliminar: "))
                        if 1 <= producto_a_eliminar <= len(inventario_ids):
                            # Eliminar el producto seleccionado usando el índice
                            producto_eliminado_id = inventario_ids.pop(producto_a_eliminar - 1)
                            producto_eliminado_nombre = inventario_nombres.pop(producto_a_eliminar - 1)
                            producto_eliminado_cantidad = inventario_cantidades.pop(producto_a_eliminar - 1)
                            print(Fore.RED + f"\nProducto '{producto_eliminado_nombre}' (ID: {producto_eliminado_id}) eliminado del inventario." + Style.RESET_ALL)
                            
                            # Revisar si el inventario quedó vacío después de la eliminación
                            if len(inventario_ids) == 0:
                                print(Fore.RED + "El inventario está vacío." + Style.RESET_ALL)
                        else:
                            print(Fore.RED + "Error: Número de producto inválido." + Style.RESET_ALL)
                    except ValueError:
                        print(Fore.RED + "Error: Por favor, ingrese un número válido." + Style.RESET_ALL)

            # Opción para "vaciar"
            elif opcion_inventario == "3":
                inventario_ids.clear()
                inventario_nombres.clear()
                inventario_cantidades.clear()
                print(Fore.RED + "\nTodos los productos han sido eliminados del inventario." + Style.RESET_ALL)

            # Opción para "agregar"
            elif opcion_inventario == "4":
                print(Fore.CYAN + "\n--- Ingreso de Productos ---" + Style.RESET_ALL)
                nombre = input("Ingrese el nombre del producto: ")

                while True:
                    try:
                        cantidad = int(input("Ingrese la cantidad de este producto: "))
                        if cantidad <= 0:
                            print(Fore.RED + "Error: Debe elegir al menos una cantidad de 1." + Style.RESET_ALL)
                        else:
                            break 
                    except ValueError:
                        print(Fore.RED + "Error: Inténtelo nuevamente ingresando un número válido." + Style.RESET_ALL)

                # ID aleatorio para el producto 
                id_producto = random.randint(1000, 9999)
                
                # Añadimos el producto a la lista
                inventario_ids.append(id_producto)
                inventario_nombres.append(nombre)
                inventario_cantidades.append(cantidad)
                print(Fore.GREEN + f"\nProducto '{nombre}' agregado con éxito (ID: {id_producto})." + Style.RESET_ALL)

            # Opción para "salir"
            elif opcion_inventario == "5":
                print(Fore.GREEN + "Saliendo del sistema... ¡Hasta luego!" + Style.RESET_ALL)
                salir = True
                break 
                
            # Opción no válida en el menú de inventario
            else:
                print(Fore.RED + "Opción no válida. Por favor, elija una opción del menú." + Style.RESET_ALL)

        else:
            # Mostrar menú si el inventario está vacío
            print(Fore.MAGENTA + "\n--- Opciones de Lista ---" + Style.RESET_ALL)
            print("1. Continuar con el pedido")
            print("2. Salir")
            print("-------------------------------------")

            opcion_inventario = input("Seleccione una opción (1 o 2): ")

            if opcion_inventario == "1":
                print(Fore.CYAN + "\nIniciando un nuevo pedido..." + Style.RESET_ALL)
                break
            elif opcion_inventario == "2":
                print(Fore.GREEN + "Saliendo del sistema... ¡Hasta luego!" + Style.RESET_ALL)
                salir = True
                break 
            
