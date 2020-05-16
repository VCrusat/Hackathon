
# esto es una prueba de python
import random

nombre = input('Introduce tu nombre: ')
print('Hola ' + nombre)
if(nombre == 'Victor'):
    print('Bienvenido de nuevo')
else:
    print('Usted no es el propietario de este equipo')   

aleatorio = random.randrange(10)
numero = int(input('Introduce un numero entre el 1 y el 10: '))
if(numero == aleatorio):
    print('HAS GANADO EL PREMIO!!!')
else:
    mensaje = "A la próxima, el numero ganador era el "
    print(mensaje + str(aleatorio))

