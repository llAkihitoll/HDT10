from grafo import Grafo
from clima import Clima

def mostrar_menu():
    print("""
1. Mostrar ruta más corta entre dos ciudades
2. Mostrar el centro del grafo
3. Cambiar el clima
4. Interrumpir tráfico entre dos ciudades
5. Añadir conexión nueva
6. Mostrar matriz de adyacencia
7. Salir
""")

def main():
    grafo = Grafo()
    grafo.leer_archivo("logistica.txt")

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            o = input("Ciudad origen: ")
            d = input("Ciudad destino: ")
            ruta = grafo.ruta_mas_corta(o, d)
            print(f"Ruta: {ruta}" if ruta else "Ruta no encontrada.")

        elif opcion == '2':
            print("Centro del grafo:", grafo.calcular_centro())

        elif opcion == '3':
            print("Opciones: NORMAL, LLUVIA, NIEVE, TORMENTA")
            c = input("Clima actual: ").upper()
            if c in Clima.__members__:
                grafo.cambiar_clima(Clima[c])
                print("Clima actualizado.")
            else:
                print("Clima inválido.")

        elif opcion == '4':
            a = input("Ciudad1: ")
            b = input("Ciudad2: ")
            grafo.modificar_trafico(a, b)

        elif opcion == '5':
            a = input("Ciudad1: ")
            b = input("Ciudad2: ")
            t = list(map(int, input("Tiempos (normal lluvia nieve tormenta): ").split()))
            grafo.añadir_conexion(a, b, t)

        elif opcion == '6':
            grafo.mostrar_matriz()

        elif opcion == '7':
            print("Programa finalizado.")
            break

        else:
            print("Opción inválida.")

if __name__ == "__main__":
    main()
