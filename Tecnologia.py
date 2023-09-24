class Tecnologia:
    def __init__(self, marca:str, voltaje:int, eficiencia:str, precio:float):
        self.__marca = marca
        self.__voltaje = voltaje
        self.__eficiencia = eficiencia
        self.__precio = precio

    def calcular_descuento(self):
        if self.__eficiencia in ['A', 'B']:
            return 0.5
        elif self.__eficiencia in ['C', 'D']:
            return 0.3
        elif self.__eficiencia in ['E', 'F']:
            return 0.1
        else:
            return 0

    def cotizar(self):
        descuento_eficiencia = self.calcular_descuento()
        precio_con_descuento = self.__precio * (1 - descuento_eficiencia)
        return f"Características: Marca: {self.__marca}, Voltaje: {self.__voltaje}, Eficiencia: {self.__eficiencia}, Precio: ${self.__precio}, Descuento aplicado: {descuento_eficiencia * 100}%, Precio con descuento: ${precio_con_descuento}"
