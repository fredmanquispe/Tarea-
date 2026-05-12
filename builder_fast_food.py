class ComboFastFood:
    def __init__(self):
        self.hamburguesa = None
        self.bebida = None
        self.papas = None

    def __str__(self):
        return f"Detalle del pedido: {self.hamburguesa}, {self.bebida}, {self.papas}."

class Builder:
    def __init__(self):
        self.combo = ComboFastFood()

    def add_hamburguesa(self, tipo):
        self.combo.hamburguesa = f"Hamburguesa: {tipo}"
        return self

    def add_bebida(self, tipo):
        self.combo.bebida = f"Bebida: {tipo}"
        return self

    def add_papas(self, tamano):
        self.combo.papas = f"Papas Fritas: {tamano}"
        return self

    def build(self):
        return self.combo

# Implementación del combo de fast food
if __name__ == "__main__":
    mi_combo = (Builder()
                .add_hamburguesa("Doble Carne con Queso")
                .add_bebida("Gaseosa Mediana")
                .add_papas("Grandes")
                .build())
    
    print("--- Combo Fast Food ---")
    print(mi_combo)
