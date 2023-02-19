# Clases

# Una clase tiene q tener cosas relacionadas con la clase, ejmplo clase = persona, variables bien seria "dormir", una que no cuadra sería "avión"

class MyPersonaVacia:              # OJO que lleva mayúscula al inicio las clases
    pass 

print(MyPersonaVacia)
print(MyPersonaVacia())

class MyPersona2:
    def __init__(self) -> None:         # "init" es un contructor de clase, o sea que reciba un parámetro
        pass

class Persona:
    def __init__(self, name, surename):     # Se le dan las clases a utilizar (nombre y apellido)
        self.name = name                    # Se asigna la variable a self
        self.surename = surename

my_persona = Persona("David", "Ochoa")      # se ponen los valores
print(f"{my_persona.name} {my_persona.surename}")   # Se imprimen con las asignaciones


class Persona:
    def __init__(self, name, surename):
        self.full_name = f"{name} {surename}"   # O bien se agrega todo como una especie de función

my_persona = Persona("Adrian", "Gaona")         # se ponen los valores
print(my_persona.full_name)                     # se imprime la función (linea 26)

a=1