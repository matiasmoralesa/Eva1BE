from Tecnologia import Tecnologia

class Consola(Tecnologia):
    def __init__(self, marca: str, nombre_consola: str, version: str, voltaje: int, precio: float, eficiencia: str):
        super().__init__(marca, voltaje, precio, eficiencia)  # Llama al constructor de la clase base Tecnologia
        self.__marca = marca
        self.__nombre_consola = nombre_consola
        self.__version = version
        self.__voltaje = voltaje
        self.__precio = precio
        self.__eficiencia = eficiencia

    @property
    def _marca(self):
        return self.__marca

    @_marca.setter
    def _marca(self, value):
        self.__marca = value

    @property
    def _nombre_consola(self):
        return self.__nombre_consola

    @_nombre_consola.setter
    def _nombre_consola(self, value):
        self.__nombre_consola = value

    @property
    def _version(self):
        return self.__version

    @_version.setter
    def _version(self, value):
        self.__version = value

    @property
    def _voltaje(self):
        return self.__voltaje

    @_voltaje.setter
    def _voltaje(self, value):
        self.__voltaje = value

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

    def cotizar(self):
        descuento_eficiencia = self.calcular_descuento_version()
        precio_con_descuento = self.__precio * (1 - descuento_eficiencia)
        return f"Características: Marca: {self.__marca}, Nombre de la consola: {self.__nombre_consola}, Versión: {self.__version}, Voltaje: {self.__voltaje}, Eficiencia: {self.__eficiencia}, Precio: ${self.__precio}, Descuento aplicado: {descuento_eficiencia * 100}%, Precio con descuento Eficiencia: ${precio_con_descuento}, Valor total después del descuento: ${precio_con_descuento}"

    def calcular_descuento_version(self):
        descuento_eficiencia = self.calcular_descuento()
        if self.__version.lower() == 'lite':
            descuento_eficiencia += 0.05  # Descuento adicional del 5% para la versión Lite
            return descuento_eficiencia
        
        else:
            return descuento_eficiencia

