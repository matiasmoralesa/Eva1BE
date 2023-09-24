from Tecnologia import Tecnologia

class Tv(Tecnologia):
    def __init__(self, marca: str, voltaje: int, precio: float, eficiencia: str, tamanio: float):
        super().__init__(marca, voltaje, precio, eficiencia)
        self.__tamanio = tamanio

    def cotizar(self):
        descuento_eficiencia = self.calcular_descuento()
        precio_con_descuento = self.__precio * (1 - descuento_eficiencia)
        return f"Características: Marca: {self.__marca}, Voltaje: {self.__voltaje}, Eficiencia: {self.__eficiencia}, Precio: ${self.precio}, Tamanio: {self.__tamanio}, Descuento aplicado: {descuento_eficiencia * 100}%, Precio con descuento: ${precio_con_descuento}, Valor total después del descuento: ${precio_con_descuento}"
