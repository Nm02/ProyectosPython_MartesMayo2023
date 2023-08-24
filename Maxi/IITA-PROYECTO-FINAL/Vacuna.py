import Tipo_Vacuna as t_vacuna
import Veterinario as veterinario

class Vacuna:
    def __init__(self, tipo_vacuna:t_vacuna, marca, dosis, fecha_de_colocacion,veterinario:veterinario, id_vacuna=0):
        self.__id_vacuna=id_vacuna
        self.__tipo_vacuna=tipo_vacuna
        self.__marca=marca
        self.__dosis=dosis
        self.__fecha_de_colocacion=fecha_de_colocacion
        self.__veterinario=veterinario

    def get_id_vacuna(self):
        return self.__id_vacuna

    def get_tipo_vacuna(self):
        return self.__tipo_vacuna

    def set_tipo_vacuna(self, value):
        self.__tipo_vacuna=value

    def get_marca(self):
        return self.__marca

    def set_marca(self, value):
        self.__marca=value

    def get_dosis(self):
        return self.__dosis

    def set_dosis(self, value):
        self.__dosis=value

    def get_fecha_de_colocacion(self):
        return self.__fecha_de_colocacion

    def set_fecha_de_colocacion(self, value):
        self.__fecha_de_colocacion=value

    def get_veterinario(self):
        return self.__veterinario

    def set_veterinario(self, value):
        self.__veterinario=value