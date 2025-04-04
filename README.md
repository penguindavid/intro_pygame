# estructura de un juego en pygame

## inicializacion

- como en todo programa en python, se debe importar los modulos o librerias a utilizar
`import pygame`

-inicializar pygame usando la funcion init (). inicializa todos los modulos de pygame importados.
`pygame.init()`

## visualizacion de la ventana 

`ventana = pygame.dislay.set_mode((600,400))`

- set mode() es la funcion encargada de definir el tamaño de la ventana. En el ejemplo. se esta definiendo una ventana de 600 px de ancho, por 400 px de alto.

`pygame.display.set_caption("Mi ventana)`

-set caption() es la funcion que añade un titulo a la ventana.

### funcion set_mode () 

`set_mode(size = (0.01),flags = 0, depth = 0,display = 0)`

-size = (600,400) : define uno o mas comportamientos para la ventana.
    - valores: 
        - pygame.FULLSCREEN
        - pygame.RESISTABLE
    - ejemplo 
        - flags = pygame.FULLSCREEN | pygame.RESIZABLE : pantalla completa, dimensiones modificables. 

## bucle de juego o game loop 

- bucle infinito que se interrumpira al cumplir ciertos criterios.

- reloj interno

- en cada iteracion de bucle del juego podemos mover un personaje, o tener en cuenta que un objeto a alcanzado a otro,o que se han cruzado la linea de llegada quiere decir que a partida ha terminado

- cada iteracion es una oportunidad para actualizar todos los datos relacionados con el estado actual dela partida

- en cada iteracion se realizan ls siguentes tareas:
    1. comprobar que no se alcanzan las condicones de parada, en cuyo caso se interrumpe el bucle.
    2. actualizar los recursos necesarios para la iteracion actual
    3. obtener las entradas de sistemas, o de interaccion del jugador
    4. actualizar todas las identidades que caracterizan el  juego
    5. refrescar la pantalla.

## superficies pygame 
- superficie: 
    - elemento geometrico
    - linea, poligono, imagen, texto que se muestra en la pantalla 
    - el poligono se puede o no rellenar de color 
    - las superficies se cean de diferente manera dependiendo del tipo:
        - image: image.load()
        - texto: font.render()
        - suoerficie generica: pygame.surface()
        - ventana de juego: pygame.display.set_mode()




