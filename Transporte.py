class Transporte:
    COSTO_DESPACHO_BASE = 4000  

    def __init__(self,  peso: float):
        self.__peso = peso

    def get_marca(self):
        return self.__marca

    def set_marca(self, value):
        self.__marca = value

    def get_voltaje(self):
        return self.__voltaje

    def set_voltaje(self, value):
        self.__voltaje = value

    def get_precio(self):
        return self.__precio

    def set_precio(self, value):
        self.__precio = value

    def get_eficiencia(self):
        return self.__eficiencia

    def set_eficiencia(self, value):
        self.__eficiencia = value

    def get_peso(self):
        return self.__peso

    def set_peso(self, value):
        self.__peso = value


    def calcular_despacho(self) -> float:
        costo_despacho_total = Transporte.COSTO_DESPACHO_BASE + self.__peso * self.__valor_por_kg
        return costo_despacho_total
