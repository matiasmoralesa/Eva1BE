from Tecnologia import Tecnologia

class Tv(Tecnologia):
    def __init__(self, marca: str, voltaje: int, precio: float, eficiencia: str, tamanio: float):
        super().__init__(marca, voltaje, precio, eficiencia)
        self.__precio = precio
        self.__eficiencia = eficiencia
        self.__tamanio = tamanio
        self.__marca = marca
        self.__voltaje = voltaje

    @property
    def _precio(self):
        return self.__precio

    @_precio.setter
    def _precio(self, value):
        self.__precio = value

    @property
    def _eficiencia(self):
        return self.__eficiencia

    @_eficiencia.setter
    def _eficiencia(self, value):
        self.__eficiencia = value

    @property
    def _tamanio(self):
        return self.__tamanio

    @_tamanio.setter
    def _tamanio(self, value):
        self.__tamanio = value

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


    def cotizar(self):
        descuento_eficiencia = self.calcular_descuento()
        precio_con_descuento = self.__precio * (1 - descuento_eficiencia)
        return f"Características: Marca: {self.__marca}, Voltaje: {self.__voltaje}, Eficiencia: {self.__eficiencia}, Precio: ${self.__precio}, Tamanio: {self.__tamanio}, Descuento aplicado: {descuento_eficiencia * 100}%, Precio con descuento: ${precio_con_descuento}, Valor total después del descuento: ${precio_con_descuento}"
