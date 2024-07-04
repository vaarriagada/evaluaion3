import csv
import os

# Lista para almacenar los pedidos
pedidos = []

# Función para limpiar la pantalla
def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')

# Función para mostrar el menú y obtener la opción del usuario
def menu():
    limpiar_pantalla()
    print("Menú CleanWasser")
    print("1. Registrar pedido")
    print("2. Listar todos los pedidos")
    print("3. Imprimir hoja de ruta")
    print("4. Buscar pedido por ID")
    print("5. Salir del programa")
    while True:
        try:
            opcion = int(input("Ingrese una opción: "))
            if opcion in range(1, 6):
                return opcion
            else:
                print("Opción inválida. Intente de nuevo.")
        except ValueError:
            print("Ingrese solo números.")

# Función para registrar un pedido
def registrar_pedido():
    limpiar_pantalla()
    print("Registro de pedido")
    nombre = input("Ingrese nombre del cliente: ")
    apellido = input("Ingrese apellido del cliente: ")
    direccion = input("Ingrese dirección: ")
    comuna = input("Ingrese comuna: ")

    # Detalle del pedido
    detalle = {}
    while True:
        print("\nDetalle de pedido:")
        print("1. Dispensador de 6 litros")
        print("2. Dispensador de 10 litros")
        print("3. Dispensador de 20 litros")
        print("4. Finalizar pedido")
        try:
            opc = int(input("Ingrese opción de dispensador: "))
            if opc == 4:
                if sum(detalle.values()) > 0:
                    break
                else:
                    print("Debe seleccionar al menos un dispensador.")
            elif opc in range(1, 4):
                cantidad = int(input(f"Ingrese cantidad de dispensadores de {opc * 5} litros: "))
                if cantidad > 0:
                    detalle[opc] = cantidad
                else:
                    print("La cantidad debe ser mayor a cero.")
            else:
                print("Opción inválida.")
        except ValueError:
            print("Ingrese solo números.")

    # Generar ID de pedido (simulado con número aleatorio)
    id_pedido = len(pedidos) + 1

    # Guardar pedido en la lista
    pedidos.append({
        "ID pedido": id_pedido,
        "Cliente": f"{nombre} {apellido}",
        "Dirección": direccion,
        "Sector": comuna,
        "Disp.6lts": detalle.get(1, 0),
        "Disp.10lts": detalle.get(2, 0),
        "Disp.20lts": detalle.get(3, 0)
    })

    print("\nPedido registrado exitosamente.")

# Función para listar todos los pedidos
def listar_pedidos():
    limpiar_pantalla()
    if len(pedidos) == 0:
        print("No hay pedidos registrados.")
    else:
        print("Listado de pedidos:")
        print("{:<10} {:<20} {:<20} {:<15} {:<10} {:<10} {:<10}".format(
            "ID pedido", "Cliente", "Dirección", "Sector", "Disp.6lts", "Disp.10lts", "Disp.20lts"
        ))
        for pedido in pedidos:
            print("{:<10} {:<20} {:<20} {:<15} {:<10} {:<10} {:<10}".format(
                pedido["ID pedido"], pedido["Cliente"], pedido["Dirección"], pedido["Sector"],
                pedido["Disp.6lts"], pedido["Disp.10lts"], pedido["Disp.20lts"]
            ))

# Función para imprimir hoja de ruta
def imprimir_hoja_de_ruta():
    limpiar_pantalla()
    sectores = ["Concepción", "Chiguayante", "Talcahuano", "Hualpén", "San Pedro"]
    print("Sectores disponibles para imprimir hoja de ruta:")
    for idx, sector in enumerate(sectores, start=1):
        print(f"{idx}. {sector}")

    while True:
        try:
            opc = int(input("Seleccione un sector para generar la hoja de ruta: "))
            if opc in range(1, len(sectores) + 1):
                sector_seleccionado = sectores[opc - 1]
                filename = f"hoja_de_ruta_{sector_seleccionado.lower()}.csv"
                with open(filename, mode='w', newline='') as file:
                    writer = csv.writer(file)
                    writer.writerow(["ID pedido", "Cliente", "Dirección", "Sector", "Disp.6lts", "Disp.10lts", "Disp.20lts"])
                    for pedido in pedidos:
                        if pedido["Sector"] == sector_seleccionado:
                            writer.writerow([
                                pedido["ID pedido"], pedido["Cliente"], pedido["Dirección"],
                                pedido["Sector"], pedido["Disp.6lts"], pedido["Disp.10lts"], pedido["Disp.20lts"]
                            ])
                print(f"Hoja de ruta para {sector_seleccionado} generada en {filename}")
                break
            else:
                print("Opción inválida. Intente de nuevo.")
        except ValueError:
            print("Ingrese solo números.")

# Función para buscar un pedido por ID
def buscar_pedido_por_id():
    limpiar_pantalla()
    if len(pedidos) == 0:
        print("No hay pedidos registrados.")
    else:
        try:
            id_buscar = int(input("Ingrese el ID del pedido a buscar: "))
            encontrado = False
            for pedido in pedidos:
                if pedido["ID pedido"] == id_buscar:
                    encontrado = True
                    print("\nDetalle del pedido encontrado:")
                    print("{:<10} {:<20} {:<20} {:<15} {:<10} {:<10} {:<10}".format(
                        "ID pedido", "Cliente", "Dirección", "Sector", "Disp.6lts", "Disp.10lts", "Disp.20lts"
                    ))
                    print("{:<10} {:<20} {:<20} {:<15} {:<10} {:<10} {:<10}".format(
                        pedido["ID pedido"], pedido["Cliente"], pedido["Dirección"], pedido["Sector"],
                        pedido["Disp.6lts"], pedido["Disp.10lts"], pedido["Disp.20lts"]
                    ))
                    break
            if not encontrado:
                print("Pedido no encontrado.")
        except ValueError:
            print("Ingrese solo números.")

# Función principal para ejecutar el programa
def main():
    while True:
        opcion = menu()

        if opcion == 1:
            registrar_pedido()
        elif opcion == 2:
            listar_pedidos()
        elif opcion == 3:
            imprimir_hoja_de_ruta()
        elif opcion == 4:
            buscar_pedido_por_id()
        elif opcion == 5:
            print("Saliendo del programa...")
            break

if __name__ == "__main__":
    main()
