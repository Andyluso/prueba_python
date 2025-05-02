caja1 = 45
caja2 = 3.1416
caja3 = "Hola soy andres"
caja4 = False
caja5 = [1, 2, 3, 4]
caja6 = ("luna", "sol")
caja7 = {"nombre": "Andres", "edad" : 18}
caja8 = {"manzana", "pera", "manzana"}


print("caja 1:", type(caja1))
print("caja 2:", type(caja2))
print("caja 3:", type(caja3))
print("caja 4:", type(caja4))
print("caja 5:", type(caja5))
print("caja 6:", type(caja6))
print("caja 7:", type(caja7))
print("caja 8:", type(caja8))

#Actividad de int
años_perro = 7
años_gato = 6

nombre = input("Cual es tu nombre? ")
edad_humana = int(input("¿Que edad tiene tu mascota en años humanos? "))
tipo_mascota = input("Tu mascota es perro o gato? ").lower()

if tipo_mascota == "perro":
    edad_mascota = edad_humana * años_perro

elif tipo_mascota == "gato":
    edad_mascota = edad_humana * años_gato

else:
    print("No se reconoce el tipo de mascota, coloca en minuscola perro o gato")

   
if edad_mascota:
        print(f"{nombre}, tu {tipo_mascota} tiene {edad_mascota} años de edad de {tipo_mascota}")