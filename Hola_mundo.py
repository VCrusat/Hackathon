import random

print('Hola Victor, desea girar la ruleta?')
eleccion = int(input('1 = SI 0 = NO: '))
if(eleccion == 1):
    numero = int(input('Introduce un numero entre el 0 y el 36: '))
    apuesta = int(input('Introduce la cantidad a apostar: '))
    contador = 0
    premio_acumulado = 0
    repeticion = 10000
    for i in range(repeticion):
        suceso = random.randrange(37)
        if(suceso == numero):
            premio = apuesta * 37
            premio_acumulado += premio
            print('HAS GANADO!!! Tu premio es '+str(premio)+ ' euros')
            contador = contador + 1
        else:
            print('Mala suerte... El número ganador era el '+str(suceso))  
    apuesta_acumulada = apuesta * repeticion        
    porcentaje = (contador / 10000) * 100  
    balance = premio_acumulado - apuesta_acumulada       
    print('Has ganado '+str(contador)+ ' veces, eso supone un '+ str(porcentaje) + ' por ciento de acierto')
    print('Tu balance es de '+ str(balance) + ' euros')
if(eleccion == 0):
    print('Hasta la próxima!!')
    SystemExit