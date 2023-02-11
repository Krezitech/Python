print("Este programa te dirá a que casa perteneces en Hogwarts ")

gr = 0
ra = 0
hu = 0
sl = 0

print("Pregunta 1: ¿Qué te gusta mas?")
print("     1) El amanecer")
print("     2) El anochecer")
q1 = int(input("Tus respuesta: "))
if q1 == 1:
    gr = gr+1
    ra = ra+1
elif q1 ==2:
    hu = hu+1
    sl = sl+1
else:
    print("Escogiste una opción erronea")


print("Pregunta 2: Después de que muera, me gustaría que la gente me recuerde por:")
print("     1) El bondadoso")
print("     2) El mejor")
print("     3) El sabio")
print("     4) El arriesgado")
q2 = int(input("Tus respuesta: "))
if q2 == 1:
    hu = hu+1
elif q2 ==2:
    sl = sl+1
elif q2 ==3:
    ra = ra+1
elif q2 ==4:
    gr = gr+1

else:
    print("Escogiste una opción erronea")


print("Pregunta 3: ¿Cuál es el instrumento que más disfruto?")
print("     1) El violín")
print("     2) La trompeta")
print("     3) El piano")
print("     4) El tambor")
q3 = int(input("Tus respuesta: "))
if q3 == 1:
    sl = sl+1
elif q3 ==2:
    hu = hu+1
elif q3 ==3:
    ra = ra+1
elif q3 ==4:
    gr = gr+1

else:
    print("Escogiste una opción erronea")


print(gr)
print(ra)
print(hu)
print(sl)