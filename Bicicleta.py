from Transporte import Transporte

class Bicicleta(Transporte):
    def __init__(self, marca, voltaje, eficiencia, precio, peso, tipo):
        super().__init__(marca, voltaje, eficiencia, precio, peso)
        self.tipo = tipo

    def cotizar(self):
        descuento_eficiencia = self.calcular_descuento()
        costo_despacho = self.calcular_costo_despacho(400)  # Valor por kg para bicicletas
        precio_con_descuento = self.precio * (1 - descuento_eficiencia)
        precio_final = precio_con_descuento + costo_despacho
        return f"Características: Marca: {self.marca}, Voltaje: {self.voltaje}, Eficiencia: {self.eficiencia}, Precio: ${self.precio}, Peso: {self.peso} kg, Tipo: {self.tipo}, Descuento aplicado: {descuento_eficiencia * 100}%, Costo de despacho: ${costo_despacho}, Precio total: ${precio_final}"
