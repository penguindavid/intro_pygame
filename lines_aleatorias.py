import pygame
import sys
import random


rojo = (255, 0, 0)
azul = (0, 0, 255)
verde = (0,255,0)
rosado = (255,192,203)
negro = (0,0,0)
amarillo = (255,255,0)
blanco = (225,225,225)
naranja = (255,165,0)
cian = (0, 255, 255)



color_aleatorio = random.randint (0, 255)

pygame.init()

ventana = pygame.display.set_mode((500, 500))

pygame.display.set_caption("ejercicio 1")

clock = pygame.time.Clock()

XX = 300
MOVIMIENTO = 3

###########################
# Bucle principal del juego
###########################
while 1:
    clock.tick(50)

    # Ciclo para la deteccion de los eventos del juego
    for event in pygame.event.get():
        # Si se hace click sobre boton de cerrar de la ventana, el juego termina
        if event.type == pygame.QUIT:
            sys.exit()

    # Rellenar la ventana de color 
    ventana.fill(negro)

    #dibujar linea 
    for _ in range(100):
   
        linea = random.randint(50, 50 + 400)
        lineas = random.randint(100, 100 + 350)
        lineac = random.randint(50, 50 + 400)
        lineav = random.randint(100, 100 + 350)
        
        color_linea = random.choice([rojo, azul, verde, rosado, amarillo, naranja, cian])

        pygame.draw.line(ventana, color_linea, (linea, lineas), (lineac, lineav))

    # Dibujar un rectangulo

    # rectangulo sin relleno,esquina sup. izq: (100,100),esquina. inf. der: (150,200).

    pygame.draw.rect(ventana,verde , ((90,90),(400,400)), 1)


    # Agregar texto
    # Fuente tipo Arial, tamaño 35, negrilla y cursiva.
    fuente_arial = pygame.font.SysFont("Arial", 23, 1, 1)
    texto = fuente_arial.render("Colegio San Jose de Guanenta", 1, blanco)
    ventana.blit(texto,(30,20))

    fuente_arial = pygame.font.SysFont("Arial", 23, 1, 1)
    texto = fuente_arial.render("David Santiago Mácias Maldonado", 1, blanco)
    ventana.blit(texto,(80,400))
    # Actualiza la visualizacion de la ventana
    pygame.display.flip()
####################################
# Fin del bucle principal del juego
####################################