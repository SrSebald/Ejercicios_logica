jugador_1 = input('ingresa piedra, papel o tijeras:')

jugador_2 = input('ingresa piedra, papel o tijeras:')

if jugador_1 == jugador_2:
    print('empate') 
elif jugador_1 == 'piedra' and jugador_2 == 'tijeras' or jugador_1 == 'tijeras' and jugador_2 == 'papel' or jugador_1 == 'papel' and jugador_2 == 'piedra':
    print('gana jugador 1')
elif jugador_2 == 'piedra' and jugador_1 == 'tijeras' or jugador_2 == 'tijeras' and jugador_1 == 'papel' or jugador_2 == 'papel' and jugador_1 == 'piedra':
    print('gana jugador 2')
else:
    print('ingreso invalido de jugador 1 o jugador 2')
     
#1ra mejora hacer un bucle para que se repita el juego hasta que uno de los jugadores quiera salir
#2da mejora llevar la cuenta de las veces que gana cada jugador y mostrar el resultado al
#3ra permitir que ingresen diferentes formas de escribir piedra, papel o tijeras                                        
#4ta poder jugar contra la computadora que elige al azar entre piedra, papel o tijeras
#5ta hacer una interfaz grafica con botones para elegir piedra, papel o tijeras
