for i in range(100):
    i = i + 1
    if i % 15 != 0 and i % 3 != 0 and i % 5 != 0:
        print(i)
    elif i % 15 == 0:
        print(i," Es multiplo de 15")
    elif i % 3 == 0:
        print(i," Es multiplo de 3")
    elif i % 5 ==0:
        print(i, " Es mulitplo de 5")


# Respuesta del curso:
"""
for num in range(1, 101):
  if num % 3 == 0 and num % 5 == 0:
    print('FizzBuzz')
  elif num % 3 == 0:
    print('Fizz')
  elif num % 5 == 0:
    print('Buzz')
  else:
    print(num)
"""