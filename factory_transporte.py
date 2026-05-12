from abc import ABC, abstractmethod

# Interfaz base de transporte
class Transporte(ABC):
    @abstractmethod
    def entregar(self):
        pass

# Producto concreto 1
class Camion(Transporte):
    def entregar(self):
        return "Entrega por carretera (Camion) realizada con éxito."

# Producto concreto 2
class Barco(Transporte):
    def entregar(self):
        return "Entrega por mar (Barco) realizada con éxito."

# Clase Factory
class Factory:
    @staticmethod
    def get_transporte(tipo):
        if tipo.lower() == "camion":
            return Camion()
        elif tipo.lower() == "barco":
            return Barco()
        return None

# Prueba del patrón
if __name__ == "__main__":
    transporte = Factory.get_transporte("barco")
    if transporte:
        print(f"Resultado Factory: {transporte.entregar()}")
