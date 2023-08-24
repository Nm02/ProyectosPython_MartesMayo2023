#Identificacion, ingresar Apellido y Nombre, de ignorar esta sentencia, Visualizar Atleta 1.

# n_a=input("Ingrese Apellido y Nombre:")

# print(n_a)

# # Ingresar fecha nacimiento

# f_n=input("Ingresar fecha nacimiento: ")
# print(f_n)

# #Institucion

# club=input("Ingresar nombre club:")
# print(club)

# #Deporte

# depo=input("Futbol")
# print(depo)


list_atletas={}
continuar=True
while continuar:
    clave=input("ingresar: ")
  
    valor=input(clave + ':')
    
    list_atletas[clave]=valor
    print(list_atletas)
    continuar=("añades atletas?: si/no")