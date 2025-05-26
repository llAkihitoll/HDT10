class Ruta:
    def __init__(self, distancia=float('inf'), camino=None):
        self.distancia = distancia
        self.camino = camino if camino else []

    def __str__(self):
        return f"{self.distancia}h por {' → '.join(self.camino)}"
