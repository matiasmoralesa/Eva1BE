class Transporte:
    COSTO_DESPACHO_BASE = 4000  # Nuevo atributo

    def __init__(self, marca: str, voltaje: int, precio: float, eficiencia: str, peso: float):
        self.marca = marca
        self.voltaje = voltaje
        self.precio = precio
        self.eficiencia = eficiencia
        self.peso = peso

    def calcular_descuento(self) -> float:
        if self.eficiencia in ['A', 'B']:
            return 0.5
        elif self.eficiencia in ['C', 'D']:
            return 0.3
        elif self.eficiencia in ['E', 'F']:
            return 0.1
        else:
            return 0

    def calcular_despacho(self) -> float:
        costo_despacho_total = Transporte.COSTO_DESPACHO_BASE + self.peso * self.valor_por_kg
        return costo_despacho_total

    def cotizar(self, valor_por_kg: float):
        self.valor_por_kg = valor_por_kg
        descuento_eficiencia = self.calcular_descuento()
        costo_despacho = self.calcular_despacho()
        precio_con_descuento = self.precio * (1 - descuento_eficiencia)
        precio_final = precio_con_descuento + costo_despacho
        return f"Características: Marca: {self.marca}, Voltaje: {self.voltaje}, Eficiencia: {self.eficiencia}, Precio: ${self.precio}, Peso: {self.peso} kg, Descuento aplicado: {descuento_eficiencia * 100}%, Costo de despacho: ${costo_despacho}, Precio total: ${precio_final}"

