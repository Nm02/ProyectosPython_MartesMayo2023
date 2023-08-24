class Veterinario:
    def __init__(self, nombre, telefono, veterinaria, id_veterinario=0):
        self.__id_veterinario=id_veterinario
        self.__nombre=nombre
        self.__telefono=telefono
        self.__veterinaria=veterinaria

    def get_id_veterinario(self):
        return self.__id_veterinario

    def get_nombre(self):
        return self.__nombre

    def set_nombre(self, value):
        self._nombre=value

    def get_telefono(self):
        return self.__telefono

    def set_telefono(self, value):
        self.__telefono=value

    def get_veterinaria(self):
        return self.__veterinaria

    def set_veterinaria(self, value):
        self.__veterinaria=value
