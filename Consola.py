from Tecnologia import Tecnologia

class Consola(Tecnologia):
    def __init__(self, nombre_consola: str, version: str, voltaje: int, precio: float, eficiencia: str):
        Tecnologia().__init__("Consola", voltaje, precio, eficiencia)  # La marca será "Consola" para todas las consolas
        self.__nombre_consola = nombre_consola
        self.__version = version

    def calcular_descuento(self) -> float:
        descuento_eficiencia = Tecnologia().calcular_descuento()
        if self.__version.lower() == 'lite':
            descuento_eficiencia += 0.05  # Descuento adicional del 5% para la versión Lite
        return descuento_eficiencia

    def cotizar(self):
        descuento_eficiencia = self.calcular_descuento()
        precio_con_descuento = self.__precio * (1 - descuento_eficiencia)
        return f"Características: Marca: {self.__marca}, Nombre de la Consola: {self.__nombre_consola}, Versión: {self.__version}, Voltaje: {self.__voltaje}, Eficiencia: {self.__eficiencia}, Precio: ${self.__precio}, Descuento aplicado: {descuento_eficiencia * 100}%, Precio con descuento: ${precio_con_descuento}, Valor total después del descuento: ${precio_con_descuento}"
