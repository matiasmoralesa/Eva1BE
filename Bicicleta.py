from Transporte import Transporte

class Bicicleta(Transporte):
    def __init__(self, aro: float, peso: float, precio: float, marca: str):
        super().__init__(precio)
        self.__aro = aro  
        self.__peso = peso
        self.__precio = precio  
        self.__marca = marca

    @property
    def _aro(self):
        return self.__aro

    @_aro.setter
    def _aro(self, value):
        self.__aro = value

    @property
    def _peso(self):
        return self.__peso

    @_peso.setter
    def _peso(self, value):
        self.__peso = value

    @property
    def _precio(self):
        return self.__precio

    @_precio.setter
    def _precio(self, value):
        self.__precio = value

    @property
    def _marca(self):
        return self.__marca

    @_marca.setter
    def _marca(self, value):
        self.__marca = value

    def calcular_despacho(self):
        costo_despacho_total = Transporte.COSTO_DESPACHO_BASE + self.__peso * 400  # Valor por kilogramo para bicicletas
        return costo_despacho_total
    
    def cotizar(self):
        costo_despacho_total = self.calcular_despacho()
        return f"Características: Aro: {self.__aro}, Peso: {self.__peso} kg, Precio: ${self.__precio}, Marca: {self.__marca}, Costo de despacho: ${costo_despacho_total}"