#!/usr/bin/env python3

#ghkpac - GUI basada en texto para hkpac.
#Escrito por Darth Venom y Tobi Emotic.
#< = >

# Importa el módulo curses de la librería standard

import curses


# Definición de la función main(). En Python esta función no es necesaria.
'''
Explicación de stdscr.

La librería Curses nos da control sobre la terminal y el espacio en la misma, por eso cuando usamos la librería curses tenemos que definir antes que nada un objeto principal que controle todo el espacio de la ventana.

Hablaremos de ventanas (windows). El objeto principal del que hablamos es una ventana especial que cubre todo el espacio de la terminal, generalmente se lo llama stdscr, que es la versión abreviada de standard screen.

El objeto stdscr es necesario para realizar cualquier operación en curses, lo podemos iniciar de la siguiente forma:

    stdscr = curses.initscr()

En este programa se usa la función Wrapper, la cual en el proceso declara stdscr, así que no hace falta hacerlo.
'''

def main(stdscr):
    pass;


# if que comprueba si el ejecutor del programa es el programa en sí o si está siendo ejecutado como módulo o desde otro programa. Si el código está siendo ejecutado por el propio programa, entonces se ejecuta el interior del if (ingresando a la función main()).

if __name__ == '__main__':

    #la función wrapper() de la librería curses se utiliza para prevenir que la sesión de terminal se vuelva un caos si el programa termina en plena ejecución debido a un error.
    curses.wrapper(main);
