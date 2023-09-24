class Tecnologia:
    def __init__(self, marca:str, voltaje:int, eficiencia:str, precio:float):
        self.__marca = marca
        self.__voltaje = voltaje
        self.__eficiencia = eficiencia
        self.__precio = precio

    @property
    def _marca(self):
        return self.__marca

    @_marca.setter
    def _marca(self, value):
        self.__marca = value

    @property
    def _voltaje(self):
        return self.__voltaje

    @_voltaje.setter
    def _voltaje(self, value):
        self.__voltaje = value

    @property
    def _eficiencia(self):
        return self.__eficiencia

    @_eficiencia.setter
    def _eficiencia(self, value):
        self.__eficiencia = value

    @property
    def _precio(self):
        return self.__precio

    @_precio.setter
    def _precio(self, value):
        self.__precio = value


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


