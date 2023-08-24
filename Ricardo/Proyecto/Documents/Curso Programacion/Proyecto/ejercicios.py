#Determinacion dias

# def Aptocomprabebida(edad):
#     if edad >=18:
#         return True
#     else:
#         return False
    
# edad_comprador=int(input("ingrese edad:"))
# es_apto=Aptocomprabebida(edad_comprador)
# if (es_apto == True):
#     print("Bebida en mostrador")
# else:
#     print("Raja")


# FECHA HOY O ACTUAL
# from datetime import datetime
# from datetime import date
# fecha=date.today()
# print(fecha)

# #calculo fecha

from datetime import datetime
from datetime import date
fecha_menst=datetime.strptime(input("ingrese fecha:"),"%Y-%m-%d").date()
fecha1=datetime.now().date()
#fecha2=datetime.strptime("2023-07-28", "%Y-%m-%d")
dias=fecha1-fecha_menst
print(dias)

fechaactual=datetime.now().date()


 #DETERMINACION ENTRENO (por ahora es la qu va)
# list_ejercicios=()

# while True:
    
#     dias=int(input("ingresar dias:"))
#     if dias <=3:
#         print("fuerza")
#     elif dias <=14:
#         print("HITT")

#     else:
#         print("seguir instrucciones Profe")
