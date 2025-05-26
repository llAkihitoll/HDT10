from clima import Clima
from ruta import Ruta

class Grafo:
    def __init__(self):
        self.ciudades = []
        self.indices = {}
        self.matriz = []
        self.rutas = []
        self.clima_actual = Clima.NORMAL

    def leer_archivo(self, path):
        with open(path, 'r') as file:
            lineas = file.readlines()

        conexiones = []
        for linea in lineas:
            datos = linea.strip().split()
            ciudad1, ciudad2 = datos[0], datos[1]
            tiempos = list(map(int, datos[2:]))
            conexiones.append((ciudad1, ciudad2, tiempos))
            for ciudad in [ciudad1, ciudad2]:
                if ciudad not in self.ciudades:
                    self.indices[ciudad] = len(self.ciudades)
                    self.ciudades.append(ciudad)

        n = len(self.ciudades)
        self.matriz = [[[float('inf')] * 4 for _ in range(n)] for _ in range(n)]

        for i in range(n):
            self.matriz[i][i] = [0]*4

        for c1, c2, tiempos in conexiones:
            i, j = self.indices[c1], self.indices[c2]
            self.matriz[i][j] = tiempos

        self.floyd()

    def floyd(self):
        n = len(self.ciudades)
        clima_idx = self.clima_actual.value
        self.rutas = [[Ruta() for _ in range(n)] for _ in range(n)]

        for i in range(n):
            for j in range(n):
                tiempo = self.matriz[i][j][clima_idx]
                if tiempo < float('inf'):
                    self.rutas[i][j] = Ruta(tiempo, [self.ciudades[i], self.ciudades[j]])

        for k in range(n):
            for i in range(n):
                for j in range(n):
                    r1 = self.rutas[i][k]
                    r2 = self.rutas[k][j]
                    if r1.distancia + r2.distancia < self.rutas[i][j].distancia:
                        nuevo_camino = r1.camino[:-1] + r2.camino
                        self.rutas[i][j] = Ruta(r1.distancia + r2.distancia, nuevo_camino)

    def ruta_mas_corta(self, origen, destino):
        i, j = self.indices.get(origen), self.indices.get(destino)
        if i is None or j is None:
            return None
        return self.rutas[i][j]

    def calcular_centro(self):
        n = len(self.ciudades)
        maximos = [max([self.rutas[i][j].distancia for j in range(n)]) for i in range(n)]
        centro_idx = maximos.index(min(maximos))
        return self.ciudades[centro_idx]

    def cambiar_clima(self, clima: Clima):
        self.clima_actual = clima
        self.floyd()

    def añadir_conexion(self, c1, c2, tiempos):
        if c1 not in self.indices:
            self.indices[c1] = len(self.ciudades)
            self.ciudades.append(c1)
        if c2 not in self.indices:
            self.indices[c2] = len(self.ciudades)
            self.ciudades.append(c2)

        self.leer_archivo("logistica.txt")  # se puede mejorar con persistencia dinámica
        i, j = self.indices[c1], self.indices[c2]
        self.matriz[i][j] = tiempos
        self.floyd()

    def modificar_trafico(self, c1, c2):
        i, j = self.indices.get(c1), self.indices.get(c2)
        if i is not None and j is not None:
            self.matriz[i][j] = [float('inf')] * 4
            self.floyd()

    def mostrar_matriz(self):
        print(f"\nMatriz de adyacencia con clima {self.clima_actual.name}:")
        for i, fila in enumerate(self.rutas):
            print(f"{self.ciudades[i]:15} ", end="")
            for ruta in fila:
                if ruta.distancia == float('inf'):
                    print(f"{'∞':>7}", end=" ")
                else:
                    print(f"{ruta.distancia:7.1f}", end=" ")
            print()
