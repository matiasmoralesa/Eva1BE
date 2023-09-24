from Transporte import Transporte

class Bicicleta(Transporte):
    def __init__(self, aro: float, peso: float, precio: float, marca: str):
        super().__init__(precio) 
        self.__aro = aro  
        self.__peso = peso  
        self.__precio = precio  
        self.__marca = marca  

    def calcular_despacho(self) -> float:
        costo_despacho_total = Transporte.COSTO_DESPACHO_BASE + self.__peso * 400  # Valor por kilogramo para bicicletas
        return costo_despacho_total