# importamos la libreria pygame
import pygame
import random

# inicializamos los modulos de pygame
pygame.init()

# Establecer titulo de la ventana
pygame.display.set_caption("surface")

# Establecemos las ordenes de la ventana 
ventana = pygame.display.set_mode((400,400))

# definidos un color
AZUL = random.randint (0,256)
ROJO = random.randint ( 0,256)
VERDE = random.randint (0, 256)
COLOR_ALETORIO = (AZUL,ROJO,VERDE)

# crear una superficie
azul_superficie = pygame.Surface((400,400))

# rellenamos la superficie de azul 
azul_superficie.fill(COLOR_ALETORIO)

# inserto la superficie de la ventana 
ventana.blit(azul_superficie, (0,0))

# actualiza la visualizacion de la ventana
pygame.display.flip()

# bucle del juego
while True:
        event = pygame.event.wait()
        if event.type == pygame.QUIT :
            break

pygame.QUIT ()

AZUL = random.randint (0,256)
ROJO =  random.randint ( 0,256)
VERDE = random.randint (0, 256)
COLOR_ALETORIO = (ROJO,AZUL,VERDE)