
import pygame
import random
from sys import exit

#Inicialmos pygame
pygame.init()

#Objetivo de hoy 15-11-2025: Abrir la pantalla negra 

#Variables de ancho, largo y alto 
ancho = 1000
alto = 500
dimensiones = (ancho, alto)

#Creamos la pantalla
pantalla = pygame.display.set_mode(dimensiones)

#Esto sirve para Cambiarle el nombre. 
pygame.display.set_caption("Pascale Pong!")

#Creamos el reloj y la fuente para el temporizador 
# 
clock = pygame.time.Clock()
font = pygame.font.SysFont("Consolas", int(ancho/20))
counter = 60 
text = font.render(str(counter), True, (0, 128, 0))

timer_event = pygame.USEREVENT+1
pygame.time.set_timer(timer_event, 1000)






runnig = True

#paddles 
player = pygame.Rect(ancho - 100, alto/2-50, 10, 100)
opponet = pygame.Rect(100, alto/2- 50, 10, 100)

#puntuacion
player_score = 0 
opponet_score = 0 


# Pelota
# Significa las dimensiones que tienen la pelota.  
pelota = pygame.Rect(ancho/2 - 10, alto/2-10, 20, 20)
x_speed, y_speed = 1, 1
                     

#Ciclo principal del juego, en este ciclo se van a ejecutar todos los eventos del juego. 
while True: 
    keys_pressed = pygame.key.get_pressed()

    #Mecanismo para mover la paleta derecha 
    if keys_pressed[pygame.K_UP]: 
        if player.top > 0: 
            player.top -= 1
    elif keys_pressed[pygame.K_DOWN]:
        if player.bottom < alto : 
            player.bottom += 1
    
    #Cambiar a k_UP AND K_DOWN para hacer trampa. 
    if keys_pressed[pygame.K_w]: 
        if opponet.top > 0: 
            opponet.top -= 1
    elif keys_pressed[pygame.K_s]:
        if opponet.bottom < alto : 
            opponet.bottom += 1

    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            pygame.quit()
            sys.exit()
        elif event.type == timer_event:
            counter -= 1
            text = font.render(str(counter), True, (0, 128, 0))
        if counter == 0:
            pygame.time.set_timer(timer_event, 0)
    

    
    if pelota.y >= alto: 
        y_speed = -1
    if pelota.y <= 0: 
        y_speed = 1
    if pelota.x <= 0: 
        player_score += 1
        pelota.center = (ancho/2, alto/2)
        x_speed, y_speed = random.choice([1, -1]), random.choice([1, -1])
    if pelota.x >= ancho: 
        opponet_score += 1
        x_speed, y_speed = random.choice([1, -1]), random.choice([1, -1])


    pelota.x += x_speed * 2
    pelota.y += y_speed * 2

    pantalla.fill("BLACK")
    pygame.draw.rect(pantalla, "white", player)
    pygame.draw.rect(pantalla, "white", opponet)
    pygame.draw.circle(pantalla, "White", pelota.center, 10)
    text_rect = text.get_rect(center = pantalla.get_rect().center)
    pantalla.blit(text, text_rect)
    pygame.display.flip()
    


# Quiero que cuando presione salir se cierre la ventana (Logrado)
# Quiero que el reloj se vea en la pantalla (Logrado)

# Quiero centrar el reloj en la pantalla en la parte de arriba qye se de color blanco (Logrado) 
# hacer las barras. 
# Hacer la pelota.
# Quiero poner de fondo una imagen (No logrado) (bajarla para después)




