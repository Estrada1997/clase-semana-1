#EJEMPLO 8:
#Diseñar un algoritmo tal que dados como datos 
#dos variables de tipo entero, obtenga el resultado de la siguiente función.
class variable: 
    def num_entero(self):
        val_1 = input("Ingrese el primer numero: ")
        val_2 = input("Ingrese el segundo numero: ")
        if int(val_1) == 1:
            resp = 100 * int(val_2)
        elif int(val_1) == 2:
            resp = 100 ** int(val_2)
        elif int(val_1) == 3:
            resp = 100 / int(val_2)
        else:
            print("El resultado es: {:. 2f}".format(resp))
dato = variable()
dato.enteros()

#EJEMPLO 9:
#Una escuela aplica dos exámenes a sus aspirantes, 
#por lo que cada uno de ellos obtiene dos calificaciones denotadas como C1 y C2. El aspirante que obtenga 
#calificaciones mayores que 80 en ambos exámenes es aceptado; en caso contrario es rechazado.
Nom = input("Ingrese el Nombre del Aspirante: ")
cal_1 = input("Ingrese su nota del primer examen: ")
cal_2 = input("Ingrese su segunda nota del examen: ")
if int(float(cal_2)) and int(float(cal_1)) < 80:
        print("Lo sentimos")
elif int(float(cal_1)) and int(float(cal_2)) > 80:
    print("Usted Sr.:", Nom)
    print("Esta Aprobado")    
else:
    print("Rechazado")

#EJEMPLO 10:
#Debe notar que el cambio de las variables contadoras se realiza de uno en 
#uno y el de las variables acumuladoras de la suma de los números.
suma = 0
while True:
    usuario = input("Escriba 's' continuar, 'n'para cancelar: ")
    if(usuario == "s"):
        num = input("Ingrese un numero: ")   
        suma = suma + int(num)
    elif (usuario == "n"):
        break
if (suma > 0):
    print("La suma es: ",suma)
else:
    print("Usted a salido")