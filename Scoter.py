from Tecnologia import Tecnologia
from Transporte import Transporte

class Scoter(Transporte, Tecnologia):
    def __init__(self, marca: str, voltaje: int, precio: float, eficiencia: str, aro: float, velocidad: int, peso: float):
        Transporte.__init__(self, marca, voltaje, precio, eficiencia, peso)  
        Tecnologia.__init__(self, marca, voltaje, precio, eficiencia) 
        self.__aro = aro
        self.__velocidad = velocidad
        self.__peso = peso
        self.__marca = marca
        self.__voltaje = voltaje
        self.__precio = precio
        self.__eficiencia = eficiencia

    @property
    def _aro(self):
        return self.__aro

    @_aro.setter
    def _aro(self, value):
        self.__aro = value

    @property
    def _velocidad(self):
        return self.__velocidad

    @_velocidad.setter
    def _velocidad(self, value):
        self.__velocidad = value

    @property
    def _peso(self):
        return self.__peso

    @_peso.setter
    def _peso(self, value):
        self.__peso = value

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

    def calcular_despacho(self):
        valor_por_kg = 300  
        costo_despacho_total = Transporte.COSTO_DESPACHO_BASE + self.__peso * valor_por_kg
        return costo_despacho_total

    def cotizar(self):
        descuento_eficiencia = self.calcular_descuento()
        costo_despacho = self.calcular_despacho()
        precio_con_descuento = self.precio * (1 - descuento_eficiencia)
        precio_final = precio_con_descuento + costo_despacho
        return f"Características: Marca: {self.__marca}, Voltaje: {self.__voltaje}, Eficiencia: {self.__eficiencia}, Precio: ${self.__precio}, Aro: {self.__aro}, Velocidad: {self.__velocidad} km/h, Peso: {self.__peso} kg, Descuento aplicado: {descuento_eficiencia * 100}%, Costo de despacho: ${costo_despacho}, Precio total: ${precio_final}"
    
    