import Eespecie as especie
import Propietario as propietario
import Vacuna as vacuna
import Tipo_Vacuna as t_vacuna
import Veterinario as veterinario

from datetime import datetime, timedelta
from email.mime.text import MIMEText
from smtplib import SMTP

class Mascota:
    def __init__(self, nombre, fecha_de_nacimiento, especie, raza, color, sexo, esterilizado, peso, observaciones, propietario:propietario, id_mascota=0):
        self.__id_mascota=id_mascota
        self.__nombre=nombre
        self.__fecha_de_nacimiento=datetime.strptime(fecha_de_nacimiento,'%Y-%m-%d')
        self.__especie=especie
        self.__raza=raza
        self.__color=color
        self.__sexo=sexo
        self.__esterilizado=esterilizado
        self.__peso=peso
        self.__observaciones=observaciones
        self.__propietario=propietario
        self.__lista_de_vacunas_especie=[]
        self.__lista_de_vacunas_desparacitaria=[]
        self.__lista_de_vacunas_antirrabica=[]
        self.__lista_de_proximas_vacunas={}

    # GETTERS AND SETTERS
    def get_id_mascota(self):
        return self.__id_mascota

    def get_nombre(self):
        return self.__nombre

    def set_nombre(self, value):
        self.__nombre=value

    def get_fecha_de_nacimiento(self):
        return self.__fecha_de_nacimiento

    def set_fecha_de_nacimiento(self, value):
        self.__fecha_de_nacimiento=value

    def get_edad(self):
        fecha_actual = datetime.now()
        edad_anios=fecha_actual.year-self.get_fecha_de_nacimiento().year-((fecha_actual.month,fecha_actual.day)<(self.get_fecha_de_nacimiento().month,self.get_fecha_de_nacimiento().day))
        return edad_anios

    def get_especie(self):
        if(self.__especie):
            return "Canino"
        else:
            return "Felino"

    def set_especie(self, value):
        self.__especie=value

    def get_raza(self):
        return self.__raza

    def set_raza(self, value):
        self.__raza=value

    def get_color(self):
        return self.__color

    def set_color(self, value):
        self.__color=value

    def get_sexo(self):
        if(self.__sexo):
            return "Macho"
        else:
            return "Hembra"

    def set_sexo(self, value):
        self.__sexo=value

    def get_esterilizado(self):
        if(self.__esterilizado):
            return "Si"
        else:
            return "No"

    def set_esterilizado(self, value):
        self.__esterilizado=value

    def get_peso(self):
        return self.__peso

    def set_peso(self, value):
        self.__peso=value

    def get_observaciones(self):
        return self.__observaciones

    def set_observaciones(self, value):
        self.__observaciones=value

    def get_propietario(self):
        return self.__propietario

    def set_propietario(self, value):
        self.__propietario=value

    def get_lista_de_vacunas_especie(self):
        return self.__lista_de_vacunas_especie

    def set_lista_de_vacunas_especie(self, value):
        self.__lista_de_vacunas_especie=value

    def agregar_lista_de_vacunas_especie(self, vacuna):
        self.get_lista_de_vacunas_especie().append(vacuna)

    def get_lista_de_vacunas_desparacitaria(self):
        return self.__lista_de_vacunas_desparacitaria

    def set_lista_de_vacunas_desparacitaria(self, value):
        self.__lista_de_vacunas_desparacitaria=value

    def agregar_lista_de_vacunas_desparacitaria(self,vacuna):
        self.get_lista_de_vacunas_desparacitaria().append(vacuna)

    def get_lista_de_vacunas_antirrabica(self):
        return self.__lista_de_vacunas_antirrabica

    def set_lista_de_vacunas_antirrabica(self, value):
        self.__lista_de_vacunas_antirrabica=value

    def agregar_lista_de_vacunas_antirrabica(self, vacuna):
        self.get_lista_de_vacunas_antirrabica().append(vacuna)

    def get_lista_de_proximas_vacunas(self):
        return self.__lista_de_proximas_vacunas

    def set_lista_de_proximas_vacunas(self, value):
        self.__lista_de_proximas_vacunas=value

    # EDAD EN DIAS
    def get_edad_dias(self):
        fecha_actual = datetime.now()
        aux=fecha_actual-self.get_fecha_de_nacimiento()
        return aux.days

    # AGREGAR PROXIMAS VACUNAS
    def agregar_lista_proximas_vacunas(self, vacuna, descripcion):
        self.get_lista_de_proximas_vacunas()[vacuna]=descripcion

    # ELIMINAR VACUNA DE LA LISTA DE PROXIMA VACUNA
    def eliminar_vacuna_de_lista_proximas_vacuna(self, valor_a_eliminar):
        claves_a_eliminar = []
        for clave, valor in self.get_lista_de_proximas_vacunas().items():
            if valor == valor_a_eliminar:
                claves_a_eliminar.append(clave)

        for clave in claves_a_eliminar:
            del self.get_lista_de_proximas_vacunas()[clave]

    # QUE ESPECIE ES
    def es_especie(self):
        if(self.__especie==especie.Especie.CANINO):
            return True
        else:
            return False

    # VACUNAS DE LA MASCOTA
    def vacunas(self):
        if(self.es_especie()):
            self.vacunas_canino()
        else:
            self.vacunas_felino()

    # CONTAR CUANTAS VACUNAS HAY EN LA LISTA DE VACUNAS DE ESPECIE
    def count_lista_de_vacunas_especie(self):
        return len(self.get_lista_de_vacunas_especie())

    # CONTAR CUANTA VACUNA HAY EN LA LISTA DE VACUNAS DESPARASITARIAS
    def count_lista_de_vacunas_desparasitaria(self):
        return len(self.get_lista_de_vacunas_desparacitaria())

    # CONTAR CUANTA VACUNA HAY EN LA LISTA DE VACUNAS ANTIRRABICAS
    def count_lista_de_vacunas_antirrabicas(self):
        return len(self.get_lista_de_vacunas_antirrabica())

    # VERIFICAR QUINTUTLE LE TOCA A UN CANINO
    def quintuple_canino(self):
        if(self.get_edad_dias()<45 and self.count_lista_de_vacunas_especie()==0):
            fechaDeNacimiento=self.get_fecha_de_nacimiento()
            nuevosDias=timedelta(days=45)
            fechaProximaVacuna=fechaDeNacimiento+nuevosDias
            anotacion="1ra dosis de la vacuna Quintuple Canina a partir "+str(fechaProximaVacuna.date())+"."
            self.agregar_lista_proximas_vacunas(t_vacuna.Tipo.QUINTUPLE_CANINA,anotacion)
        if(self.get_edad_dias()>=45 and self.count_lista_de_vacunas_especie()==0):
            self.agregar_lista_proximas_vacunas(t_vacuna.Tipo.QUINTUPLE_CANINA,"1ra dosis de la Vacuna Quintuple Canina.")
        if(self.get_edad_dias()>=45 and self.count_lista_de_vacunas_especie()==1):
            fechaAnteriorVacuna=self.get_lista_de_vacunas_especie()[self.count_lista_de_vacunas_especie()-1].get_fecha_de_colocacion()
            nuevosDias=timedelta(days=15)
            fechaProximaVacuna=fechaAnteriorVacuna+nuevosDias
            anotacion="2da dosis de la Vacuna Quintuple Canina a partir "+str(fechaProximaVacuna.date())+"."
            self.agregar_lista_proximas_vacunas(t_vacuna.Tipo.QUINTUPLE_CANINA,anotacion)
        if(self.get_edad_dias()>=60 and self.count_lista_de_vacunas_especie()==2):
            fechaAnteriorVacuna=self.get_lista_de_vacunas_especie()[self.count_lista_de_vacunas_especie()-1].get_fecha_de_colocacion()
            nuevosDias=timedelta(days=30)
            fechaProximaVacuna=fechaAnteriorVacuna+nuevosDias
            anotacion="3ra dosis de la Vacuna Quintuple Canina a partir "+str(fechaProximaVacuna.date())+"."
            self.agregar_lista_proximas_vacunas(t_vacuna.Tipo.QUINTUPLE_CANINA,anotacion)
        if(self.get_edad_dias()>=90 and self.count_lista_de_vacunas_especie()==3):
            fechaAnteriorVacuna=self.get_lista_de_vacunas_especie()[self.count_lista_de_vacunas_especie()-1].get_fecha_de_colocacion()
            nuevosDias=timedelta(days=30)
            fechaProximaVacuna=fechaAnteriorVacuna+nuevosDias
            anotacion="4ta dosis de la Vacuna Quintuple Canina a partir "+str(fechaProximaVacuna.date())+"."
            self.agregar_lista_proximas_vacunas(t_vacuna.Tipo.QUINTUPLE_CANINA,anotacion)
        if(self.get_edad_dias()>=120 and self.count_lista_de_vacunas_especie()>=4):
            fechaAnteriorVacuna=self.get_lista_de_vacunas_especie()[self.count_lista_de_vacunas_especie()-1].get_fecha_de_colocacion()
            nuevosDias=timedelta(days=360)
            fechaProximaVacuna=fechaAnteriorVacuna+nuevosDias
            anotacion="Refuerzo anual de la Vacuna Quintuple Canina a partir "+str(fechaProximaVacuna.date())+"."
            self.agregar_lista_proximas_vacunas(t_vacuna.Tipo.QUINTUPLE_CANINA,anotacion)

    # VERIFICAR DESPARASITARIA LE TOCA A UN CANINO
    def desparasitaria_canino(self):
        if(self.get_edad_dias()<45 and self.count_lista_de_vacunas_desparasitaria()==0):
            fechaDeNacimiento=self.get_fecha_de_nacimiento()
            nuevosDias=timedelta(days=45)
            fechaProximaVacuna=fechaDeNacimiento+nuevosDias
            anotacion="1ra dosis de la vacuna Desparasitaria Canina a partir "+str(fechaProximaVacuna.date())+"."
            self.agregar_lista_proximas_vacunas(t_vacuna.Tipo.DESPARACITARIA,anotacion)
        if(self.get_edad_dias()>=45 and self.count_lista_de_vacunas_desparasitaria()==0):
            self.agregar_lista_proximas_vacunas(t_vacuna.Tipo.DESPARACITARIA,"1ra dosis de la vacuna Desparasitaria Canina.")
        if(self.get_edad_dias()>=45 and self.count_lista_de_vacunas_desparasitaria()==1):
            fechaAnteriorVacuna=self.get_lista_de_vacunas_desparacitaria()[self.count_lista_de_vacunas_desparasitaria()-1].get_fecha_de_colocacion()
            nuevosDias=timedelta(days=15)
            fechaProximaVacuna=fechaAnteriorVacuna+nuevosDias
            anotacion="2da dosis de la vacuna Desparasitaria Canina a partir "+str(fechaProximaVacuna.date())+"."
            self.agregar_lista_proximas_vacunas(t_vacuna.Tipo.DESPARACITARIA,anotacion)
        if(self.get_edad_dias()>=60 and self.count_lista_de_vacunas_desparasitaria()==2):
            fechaAnteriorVacuna=self.get_lista_de_vacunas_desparacitaria()[self.count_lista_de_vacunas_desparasitaria()-1].get_fecha_de_colocacion()
            nuevosDias=timedelta(days=30)
            fechaProximaVacuna=fechaAnteriorVacuna+nuevosDias
            anotacion="3ra dosis de la vacuna Desparasitaria Canina a partir "+str(fechaProximaVacuna.date())+"."
            self.agregar_lista_proximas_vacunas(t_vacuna.Tipo.DESPARACITARIA,anotacion)
        if(self.get_edad_dias()>=90 and self.count_lista_de_vacunas_desparasitaria()>=3):
            fechaAnteriorVacuna=self.get_lista_de_vacunas_desparacitaria()[self.count_lista_de_vacunas_desparasitaria()-1].get_fecha_de_colocacion()
            nuevosDias=timedelta(days=360)
            fechaProximaVacuna=fechaAnteriorVacuna+nuevosDias
            anotacion="Refuerzo anual de la Vacuna Desparacitaria Canina a partir "+str(fechaProximaVacuna.date())+"."
            self.agregar_lista_proximas_vacunas(t_vacuna.Tipo.DESPARACITARIA,anotacion)

    # VERIFICAR ANTIRRABICA LE TOCA A UN CANINO
    def antirrabica_canino(self):
        if(self.get_edad_dias()<120 and self.count_lista_de_vacunas_antirrabicas()==0):
            fechaDeNacimiento=self.get_fecha_de_nacimiento()
            nuevosDias=timedelta(days=120)
            fechaProximaVacuna=fechaDeNacimiento+nuevosDias
            anotacion="1ra dosis de la vacuna Antirrábica Canina a partir "+str(fechaProximaVacuna.date())+"."
            self.agregar_lista_proximas_vacunas(t_vacuna.Tipo.ANTIRRABICA,anotacion)
        if(self.get_edad_dias()>=120 and self.count_lista_de_vacunas_antirrabicas()==0):
            self.agregar_lista_proximas_vacunas(t_vacuna.Tipo.ANTIRRABICA,"1ra dosis de la vacuna Antirrábica Canina.")
        if(self.get_edad_dias()>=120 and self.count_lista_de_vacunas_antirrabicas()>=1):
            fechaAnteriorVacuna=self.get_lista_de_vacunas_antirrabica()[self.count_lista_de_vacunas_antirrabicas()-1].get_fecha_de_colocacion()
            nuevosDias=timedelta(days=360)
            fechaProximaVacuna=fechaAnteriorVacuna+nuevosDias
            anotacion="Refuerzo anual de la Vacuna Desparacitaria Canina a partir "+str(fechaProximaVacuna.date())+"."
            self.agregar_lista_proximas_vacunas(t_vacuna.Tipo.ANTIRRABICA,anotacion)

    # VACUNAS DE CANINOS
    def vacunas_canino(self):
        self.quintuple_canino()
        self.desparasitaria_canino()
        self.antirrabica_canino()

    # VERIFICAR TRIPLE LE TOCA A UN FELINA
    def triple_felina(self):
        if(self.get_edad_dias()<60 and self.count_lista_de_vacunas_especie()==0):
            fechaDeNacimiento=self.get_fecha_de_nacimiento()
            nuevosDias=timedelta(days=60)
            fechaProximaVacuna=fechaDeNacimiento+nuevosDias
            anotacion="1ra dosis de la Vacuna Triple Felina a partir "+str(fechaProximaVacuna.date())+"."
            self.agregar_lista_proximas_vacunas(t_vacuna.Tipo.TRIPLE_FELINA,anotacion)
        if(self.get_edad_dias()>=60 and self.count_lista_de_vacunas_especie()==0):
            self.agregar_lista_proximas_vacunas(t_vacuna.Tipo.TRIPLE_FELINA,"1ra dosis de la vacuna Triple Felina.")
        if(self.get_edad_dias()>=60 and self.count_lista_de_vacunas_especie()==1):
            fechaAnteriorVacuna=self.get_lista_de_vacunas_especie()[self.count_lista_de_vacunas_especie()-1].get_fecha_de_colocacion()
            nuevosDias=timedelta(days=90)
            fechaProximaVacuna=fechaAnteriorVacuna+nuevosDias
            anotacion="2da dosis de la Vacuna Triple Felina a partir "+str(fechaProximaVacuna.date())+"."
            self.agregar_lista_proximas_vacunas(t_vacuna.Tipo.TRIPLE_FELINA,anotacion)
        if(self.get_edad_dias()>=90 and self.count_lista_de_vacunas_especie()>=2):
            fechaAnteriorVacuna=self.get_lista_de_vacunas_especie()[self.count_lista_de_vacunas_especie()-1].get_fecha_de_colocacion()
            nuevosDias=timedelta(days=360)
            fechaProximaVacuna=fechaAnteriorVacuna+nuevosDias
            anotacion="Refuerzo anual de la Vacuna Triple Felina a partir "+str(fechaProximaVacuna.date())+"."
            self.agregar_lista_proximas_vacunas(t_vacuna.Tipo.TRIPLE_FELINA,anotacion)

    # VERIFICAR DESPARASITARIA LE TOCA A UN FELINO
    def desparasitaria_felina(self):
        if(self.get_edad_dias()<60 and self.count_lista_de_vacunas_desparasitaria()==0):
            fechaDeNacimiento=self.get_fecha_de_nacimiento()
            nuevosDias=timedelta(days=60)
            fechaProximaVacuna=fechaDeNacimiento+nuevosDias
            anotacion="1ra dosis de la Vacuna Desparasitaria a partir "+str(fechaProximaVacuna.date())+"."
            self.agregar_lista_proximas_vacunas(t_vacuna.Tipo.DESPARACITARIA,anotacion)
        if(self.get_edad_dias()>=60 and self.count_lista_de_vacunas_desparasitaria()==0):
            self.agregar_lista_proximas_vacunas(t_vacuna.Tipo.DESPARACITARIA,"1ra dosis de la Vacuna Desparasitaria.")
        if(self.get_edad_dias()>=60 and self.count_lista_de_vacunas_desparasitaria()==1):
            fechaAnteriorVacuna=self.get_lista_de_vacunas_desparacitaria()[self.count_lista_de_vacunas_desparasitaria()-1].get_fecha_de_colocacion()
            nuevosDias=timedelta(days=90)
            fechaProximaVacuna=fechaAnteriorVacuna+nuevosDias
            anotacion="2da dosis de la Vacuna Desparasitaria a partir "+str(fechaProximaVacuna.date())+"."
            self.agregar_lista_proximas_vacunas(t_vacuna.Tipo.DESPARACITARIA,anotacion)
        if(self.get_edad_dias()>=90 and self.count_lista_de_vacunas_desparasitaria()>=2):
            fechaAnteriorVacuna=self.get_lista_de_vacunas_desparacitaria()[self.count_lista_de_vacunas_desparasitaria()-1].get_fecha_de_colocacion()
            nuevosDias=timedelta(days=360)
            fechaProximaVacuna=fechaAnteriorVacuna+nuevosDias
            anotacion="Refuerzo anual de la Vacuna Desparasitaria a partir "+str(fechaProximaVacuna.date())+"."
            self.agregar_lista_proximas_vacunas(t_vacuna.Tipo.DESPARACITARIA,anotacion)

    # VERIFICAR ANTIRRABICA LE TOCA A UN CANINO
    def antirrabica_felina(self):
        if(self.get_edad_dias()<120 and self.count_lista_de_vacunas_antirrabicas()==0):
            fechaDeNacimiento=self.get_fecha_de_nacimiento()
            nuevosDias=timedelta(days=120)
            fechaProximaVacuna=fechaDeNacimiento+nuevosDias
            anotacion="1ra dosis de la vacuna Antirrábica Felina a partir "+str(fechaProximaVacuna.date())+"."
            self.agregar_lista_proximas_vacunas(t_vacuna.Tipo.ANTIRRABICA,anotacion)
        if(self.get_edad_dias()>=120 and self.count_lista_de_vacunas_antirrabicas()==0):
            self.agregar_lista_proximas_vacunas(t_vacuna.Tipo.ANTIRRABICA,"1ra dosis de la vacuna Antirrábica Felina.")
        if(self.get_edad_dias()>=120 and self.count_lista_de_vacunas_antirrabicas()>=1):
            fechaAnteriorVacuna=self.get_lista_de_vacunas_antirrabica()[self.count_lista_de_vacunas_antirrabicas()-1].get_fecha_de_colocacion()
            nuevosDias=timedelta(days=360)
            fechaProximaVacuna=fechaAnteriorVacuna+nuevosDias
            anotacion="Refuerzo anual de la Vacuna Desparacitaria Felina a partir "+str(fechaProximaVacuna.date())+"."
            self.agregar_lista_proximas_vacunas(t_vacuna.Tipo.ANTIRRABICA,anotacion)

    # VACUNAS DE FELINOS
    def vacunas_felino(self):
        self.triple_felina()
        self.desparasitaria_felina()
        self.antirrabica_felina()

    # MOSTRAR PROXIMAS VACUNAS
    def mostrar_proximas_vacunas(self):
        print("*************METODO mostrar_proximas_vacunas*************")
        print(f"Proximas vacunas de {self.get_nombre()}:")
        i = 1
        for clave, valor in self.get_lista_de_proximas_vacunas().items():
            print(str(i) + ". " + valor)
            i += 1

    # AGREGAR VACUNA CORRESPONDIENTE
    def agregar_vacuna_correspondiente(self,tipo_vacuna,vacuna):
        if(tipo_vacuna==t_vacuna.Tipo.QUINTUPLE_CANINA or tipo_vacuna==t_vacuna.Tipo.TRIPLE_FELINA):
            self.agregar_lista_de_vacunas_especie(vacuna)
        if(tipo_vacuna==t_vacuna.Tipo.DESPARACITARIA):
            self.agregar_lista_de_vacunas_desparacitaria(vacuna)
        if(tipo_vacuna==t_vacuna.Tipo.ANTIRRABICA):
            self.agregar_lista_de_vacunas_antirrabica(vacuna)

    # ELEGIR VACUNA
    def elegir_vacuna(self,valorvacuna):
        i = 1
        copia_claves = list(self.get_lista_de_proximas_vacunas().keys())
        for clave in copia_claves:
            valor = self.get_lista_de_proximas_vacunas()[clave]
            if i == valorvacuna:
                dosis=0
                if(clave==t_vacuna.Tipo.QUINTUPLE_CANINA or clave==t_vacuna.Tipo.TRIPLE_FELINA):
                    dosis=self.count_lista_de_vacunas_especie()+1
                if(clave==t_vacuna.Tipo.DESPARACITARIA):
                    dosis=self.count_lista_de_vacunas_desparasitaria()+1
                if(clave==t_vacuna.Tipo.ANTIRRABICA):
                    dosis=self.count_lista_de_vacunas_antirrabicas()+1
                print("*****************DATOS DE LA VACUNA*****************")
                marca=input("Ingrese la marca de la vacuna: \n")
                nombreVeterinario=input("Ingrese en nombre del Veterinario:\n")
                telefonoVeterinario=input("Ingrese el telefono del veterinario: \n")
                fechaStr=input("Ingrese la fecha en formato YYYY-MM-DD: \n")
                fechaDeColocación=datetime.strptime(fechaStr,'%Y-%m-%d')
                veterinariaVeterinario=input("Ingrese el nombre de la veterinaria:\n")
                nuevoVeterinario=veterinario.Veterinario(nombre=nombreVeterinario,telefono=telefonoVeterinario,veterinaria=veterinariaVeterinario)
                nuevaVacuna=vacuna.Vacuna(tipo_vacuna=clave,marca=marca,dosis=dosis,fecha_de_colocacion=fechaDeColocación,veterinario=nuevoVeterinario)
                self.agregar_vacuna_correspondiente(tipo_vacuna=clave,vacuna=nuevaVacuna)
                self.eliminar_vacuna_de_lista_proximas_vacuna(valor_a_eliminar=valor)
                self.vacunas()
                break

    # COLOCAR VACUNA
    def colocar_vacuna(self):
        print("*************METODO colocar_vacuna*************")
        print(f"Seleccione que vacuna va a colocar a {self.get_nombre()}:")
        i = 1
        for clave, valor in self.get_lista_de_proximas_vacunas().items():
            print(str(i) + ". " + valor)
            i += 1
        valorVacuna=int(input("Ingrese que vacuna va a colocar: \n"))
        if(valorVacuna<=len(self.get_lista_de_proximas_vacunas())):
            self.elegir_vacuna(valorVacuna)
        else:
            self.colocar_vacuna()
        desicion=int(input("Desea ingresar una nueva Vacuna?\n1. Si.\n2. No.\n"))
        if(desicion==1):
            self.colocar_vacuna()

    # DATOS DE LA MASCOTA
    def datos_mascota(self):
        datos=f"*******************DATOS DE {self.get_nombre()}*******************\n" \
            f"Nombre: {self.get_nombre()}\n" \
            f"Fecha de Nacimiento: {self.get_fecha_de_nacimiento()}\n" \
            f"Edad: {self.get_edad()}\n" \
            f"Especie: {self.get_especie()}\n" \
            f"Raza: {self.get_raza()}\n" \
            f"Color: {self.get_color()}\n" \
            f"Esterilizado: {self.get_esterilizado()}\n" \
            f"Peso: {self.get_peso()}\n" \
            f"Observaciones: {self.get_observaciones()}\n" \
            f"Propietario: {self.get_propietario().get_nombre()} {self.get_propietario().get_apellido()}\n" \
            f"Mail: {self.get_propietario().get_mail()}\n" \
            f"Telefono: {self.get_propietario().get_telefono()}\n" \
            f"Domicilio: {self.get_propietario().get_domicilio()}\n"
        return datos

    # CARNET DE VACUNAS COLOCADAS
    def carnet(self):
        carnet="************VACUNAS COLOCADAS************\n"
        vacunasEspecie=self.get_lista_de_vacunas_especie()
        carnet+="**********ESPECIE**********\n"
        e=1
        for v in range(len(vacunasEspecie)):
            carnet+=f"{str(e)}. Tipo de Vacuna: {vacunasEspecie[v].get_tipo_vacuna()}\n" \
                    f"Marca: {vacunasEspecie[v].get_marca()}\n" \
                    f"Dosis: {vacunasEspecie[v].get_dosis()}\n" \
                    f"Fecha de Colocación: {vacunasEspecie[v].get_fecha_de_colocacion()}\n" \
                    f"Veterinario: {vacunasEspecie[v].get_veterinario().get_nombre()}\n"
            e+=1
        vacunasDesparasitaria=self.get_lista_de_vacunas_desparacitaria()
        carnet+="**********DESPARACITARIAS**********\n"
        d=1
        for v in range(len(vacunasDesparasitaria)):
            carnet+=f"{str(d)}. Tipo de Vacuna: {vacunasDesparasitaria[v].get_tipo_vacuna()}\n" \
                    f"Marca: {vacunasDesparasitaria[v].get_marca()}\n" \
                    f"Dosis: {vacunasDesparasitaria[v].get_dosis()}\n" \
                    f"Fecha de Colocación: {vacunasDesparasitaria[v].get_fecha_de_colocacion()}\n" \
                    f"Veterinario: {vacunasDesparasitaria[v].get_veterinario().get_nombre()}\n"
            d+=1
        vacunasAntirrabica=self.get_lista_de_vacunas_antirrabica()
        carnet+="**********ANTIRRABICAS**********\n"
        a=1
        for v in range(len(vacunasAntirrabica)):
            carnet+=f"{str(a)}. Tipo de Vacuna: {vacunasAntirrabica[v].get_tipo_vacuna()}\n" \
                    f"Marca: {vacunasAntirrabica[v].get_marca()}\n" \
                    f"Dosis: {vacunasAntirrabica[v].get_dosis()}\n" \
                    f"Fecha de Colocación: {vacunasAntirrabica[v].get_fecha_de_colocacion()}\n" \
                    f"Veterinario: {vacunasAntirrabica[v].get_veterinario().get_nombre()}\n"
            a+=1
        carnet+="**********PROXIMAS**********\n"
        i=1
        for clave, valor in self.get_lista_de_proximas_vacunas().items():
            carnet+=f"{str(i)}. {valor}\n"
        return carnet

    def enviar_mail(self):
        # construir mensaje para enviar
        datos=self.datos_mascota()
        carnet=self.carnet()
        mensaje=datos+carnet

        # Configurar cuentas
        remitente="maximiliano.70.32.10.soriano@gmail.com" #Correo de la cuenta que envia el mail
        destinatario=self.get_propietario().get_mail() #Correo al que mandar el mail

        #Configuarar Mensaje
        mensaje_correo = MIMEText(mensaje)
        mensaje_correo["From"] = remitente
        mensaje_correo["To"] = destinatario
        mensaje_correo["Subject"] = f"Carnet de {self.get_nombre()}"

        #Coneccion
        servidor = SMTP("smtp.gmail.com", 587)
        servidor.ehlo()
        servidor.starttls()

        #Inicio de sesion
        servidor.login(remitente, "vbwgzkcezkqwhtkb") #Se agrega el usuario de mail y la contraseña generada

        #Enviar mail
        servidor.sendmail(remitente, destinatario, mensaje_correo.as_string())

        #Terminar Coneccion
        servidor.quit()
        print("Correo enviado")


# propietario1=propietario.Propietario(nombre="Luis", apellido="Sanchez", mail="sanchez@gmail.com", telefono="3874132456", domicilio="Calle Falsa 123")
# mi_mascota = Mascota(nombre="Margo", fecha_de_nacimiento="2021-12-15",especie=especie.Especie.CANINO, raza="Labrador", color="Dorado", sexo=False, esterilizado=False, peso=25.5, observaciones="Ninguna",propietario=propietario1)

# # mi_mascota.vacunas()

# # mi_mascota.colocar_vacuna()

# # mi_mascota.mostrar_proximas_vacunas()

# propietario2=propietario.Propietario(nombre="Karen", apellido="Dominguez", mail="maximiliano.70.32.10.soriano@gmail.com", telefono="3875987456", domicilio="Calle Falsa 1000")
# otra_mascota = Mascota(nombre="Mia", fecha_de_nacimiento="2022-08-03", especie=especie.Especie.FELINO, raza="Siamés", color="Blanco", sexo=False, esterilizado=True, peso=4.0, observaciones="Tiene ojos azules", propietario=propietario2)

# otra_mascota.vacunas()

# # otra_mascota.colocar_vacuna()

# otra_mascota.mostrar_proximas_vacunas()

# # print(otra_mascota.datos_mascota())

# # print(otra_mascota.carnet())

# otra_mascota.enviar_mail()