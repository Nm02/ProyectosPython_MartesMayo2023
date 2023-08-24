import Propietario as propietario
import Mascota as mascota
import Eespecie as especie

propietario1=propietario.Propietario(nombre="Luis", apellido="Sanchez", mail="nicobmart@gmail.com", telefono="3874132456", domicilio="Calle Falsa 123")
mi_mascota = mascota.Mascota(nombre="Margo", fecha_de_nacimiento="2021-12-15",especie=especie.Especie.CANINO, raza="Labrador", color="Dorado", sexo=False, esterilizado=False, peso=25.5, observaciones="Ninguna",propietario=propietario1)

mi_mascota.vacunas()

mi_mascota.colocar_vacuna()

mi_mascota.mostrar_proximas_vacunas()

# propietario2=propietario.Propietario(nombre="Karen", apellido="Dominguez", mail="maximiliano.70.32.10.soriano@gmail.com", telefono="3875987456", domicilio="Calle Falsa 1000")
# otra_mascota =  mascota.Mascota(nombre="Mia", fecha_de_nacimiento="2022-08-03", especie=especie.Especie.FELINO, raza="Siamés", color="Blanco", sexo=False, esterilizado=True, peso=4.0, observaciones="Tiene ojos azules", propietario=propietario2)

# otra_mascota.vacunas()

# otra_mascota.colocar_vacuna()

# otra_mascota.mostrar_proximas_vacunas()

# print(otra_mascota.datos_mascota())

# print(otra_mascota.carnet())

mi_mascota.enviar_mail()