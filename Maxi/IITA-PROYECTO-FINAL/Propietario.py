class Propietario:
    def __init__(self, nombre, apellido, mail, telefono, domicilio, id_propietario=0):
        self._id_propietario=id_propietario
        self._nombre=nombre
        self._apellido=apellido
        self._mail=mail
        self._telefono=telefono
        self._domicilio=domicilio

    def get_id_propietario(self):
        return self._id_propietario

    def set_nombre(self, nombre):
        self._nombre = nombre

    def get_nombre(self):
        return self._nombre

    def set_apellido(self, apellido):
        self._apellido = apellido

    def get_apellido(self):
        return self._apellido

    def set_mail(self, mail):
        self._mail = mail

    def get_mail(self):
        return self._mail

    def set_telefono(self, telefono):
        self._telefono = telefono

    def get_telefono(self):
        return self._telefono

    def set_domicilio(self, domicilio):
        self._domicilio = domicilio

    def get_domicilio(self):
        return self._domicilio
