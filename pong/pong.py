
import pygame

pygame.init()

#Objetivo de hoy 15-11-2025: Abrir la pantalla negra 

#Variables de ancho, largo y alto 
ancho = 500
alto = 500
dimensiones = (ancho, alto)
pantalla = pygame.display.set_mode(dimensiones)


runnig = True

while runnig: 
    for event in pygame.event.get():
        if event.type == pygame.quit: 
            runnig = False

pygame.quit()



