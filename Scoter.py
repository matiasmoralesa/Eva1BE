from Tecnologia import Tecnologia
from Transporte import Transporte

class Scoter(Transporte, Tecnologia):
    def __init__(self, marca: str, voltaje: int, precio: float, eficiencia: str, aro: float, velocidad: int, peso: float):
        Transporte.__init__(self, marca, voltaje, precio, eficiencia, peso)  
        Tecnologia.__init__(self, marca, voltaje, precio, eficiencia) 
        self.aro = aro
        self.velocidad = velocidad
        self.peso = peso

    def calcular_despacho(self) -> float:
        valor_por_kg = 300  
        costo_despacho_total = Transporte.COSTO_DESPACHO_BASE + self.peso * valor_por_kg
        return costo_despacho_total

    def cotizar(self):
        descuento_eficiencia = self.calcular_descuento()
        costo_despacho = self.calcular_despacho()
        precio_con_descuento = self.precio * (1 - descuento_eficiencia)
        precio_final = precio_con_descuento + costo_despacho
        return f"Características: Marca: {self.marca}, Voltaje: {self.voltaje}, Eficiencia: {self.eficiencia}, Precio: ${self.precio}, Aro: {self.aro}, Velocidad: {self.velocidad} km/h, Peso: {self.peso} kg, Descuento aplicado: {descuento_eficiencia * 100}%, Costo de despacho: ${costo_despacho}, Precio total: ${precio_final}"