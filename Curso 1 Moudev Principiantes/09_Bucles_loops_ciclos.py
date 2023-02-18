# Bucles, loops y ciclos

# While

my_condition = 0

#while my_condition < 10:
 #   print("Mi condicion se cumple porque es menor que 10")      # Se continuaria imprimiendo eternamente pq siempre será menor que 10
 

while my_condition < 15:
    print(my_condition)                        # Se continuaria imprimiendo hasta q la condicion cambie
    my_condition +=3                           # Va a sumar tres mas cada iteración por lo que se imprime hasta que se cumpla la condición, o sea hasta 12, que es menor que 15
else:
    print("Ya la condición es mayor que 15")    # Se pueden usar "else" en los while, pero no "if" o "elif"

print("Se acaba el primer While")
print(my_condition)                             # La condición estpá en 15

while my_condition < 20:
    print("Mi condición es menor que 20") 
    print(my_condition)      # Imprimirá  4 veces esto pq es menor a 20
    my_condition += 1
    if  my_condition == 18:                     # Pero cuando sea 19
        print("La condición está en 19")        # Iimprimirá esto, y además el texto anterior pq sigue cumpliéndose la condición de ser menor a 20

print("Se acaba el segundo While")

my_condition = 10
while my_condition < 20:
    print(my_condition)     
    print("Mi condición es menor que 20") 
    my_condition += 1
    if  my_condition == 18: 
        print("Se detiene en 18")               # Cuando sea 18 has... (break)
        break                                   # Rompe el ciclo Aqui
        print("La condición está en 19")        # Ya no lo toma en cuenta pq ya se detuvo en 18       

# For









