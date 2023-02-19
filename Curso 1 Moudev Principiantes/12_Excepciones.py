##########################################################
#################      Excepciones      ##################
##########################################################

# Se usan para en caso de errores, el programa no muera, sino contenga el problema

print("#################################################")
print("#################      1      ###################")
print("#################################################")

numero1 = 5
numero2 = "5"

#print(numero1 + numero2)              # No puede sumarlos pq uno es "str" y el otro "int"


print("#################################################")
print("#################      2      ###################")
print("#################################################")

# con el "try" intenta realizar lo solicitado, y con "except", crea un camino alterno en caso de que el "try" no pueda ejecutarse


numero1 = 5
numero2 = "5"

try:
    print(numero1 + numero2)                # No se pudo, pq el num2 es "str"
except:
    print("Hubo un error en la suma")       # Despliega este texto al no habers podido anteriormente



numero3 = 5
numero4 = 5

try:
    print(numero3 + numero4)                # como son los dos "int", se realiza y despliega lo solicitado
    print("No hubo error!!!")   
except:
    print("Hubo un error en la suma")       # No aplica pq si se pudo realizar la acción


print("#################################################")
print("#################      3      ###################")
print("#################################################")


numero1 = 5
numero2 = 5

try:
    print(numero1 + numero2)                         # se ejecuta pq no pasa una excepcion
    print("No hubo error!!!")                        # se ejecuta pq no pasa una excepcion

except:
    print("Hubo un error en la suma")   

else:
    print("La ejecución continúa correctamente")    # se ejecuta pq no pasa una excepcion    

print("#################################################")
print("#################      4      ###################")
print("#################################################")

a = 09_13_51