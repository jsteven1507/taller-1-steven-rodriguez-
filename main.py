import numpy as np #librería en la que se define un tipo de dato que representa matrices multidimensionales
# además incluye algunas funcionalidades básicas para trabajar con ellas

import os  #libreria para el acceso portable a funciones específicas del sistema operativo
import cv2 #OpenCV es una biblioteca libre de visión artificial originalmente desarrollada por Intel

from colorimage import colorimag # Se importa la clase colorimag

if __name__ == '__main__':
    print('Ingrese ruta de la imagen(agregue al final el nombre de su imagen con su formato):')
    print('Por ejemplo:  C:/Users/Hewlett Packard/Desktop/8 semestre/Procesamiento de imagenes/lena.png:  ')

    dir = input()        # se guarda la direccion de la imagen a procesar

    imagen=colorimag(dir) # se define imagen como clase colorimag y valor de entrada la direccion de la imagen

    imagen.displayProperties() # método para obtener alto y ancho de la imagen
    gray=imagen.makeGray()     # método en que se obtiene la imagen en escala de grises
    colori=imagen.colorizeRGB('red') #metodo para obtener la imagen colorizada en el color especificado (blue,green,red)
    H = imagen.makeHue()       # método en que se devuelve una imagen que resalta los tonos (Hue) de la imagen

    # se crean las ventanas donde se muestran la imagen en escala de grises, la imagen colorizada y la imagen con realce del tono (TUE)
    cv2.namedWindow("Gray")
    cv2.imshow("Gray", gray)

    cv2.namedWindow("Colorizado")
    cv2.imshow("Colorizado", colori)

    cv2.namedWindow("Tonos (HUE)")
    cv2.imshow("Tonos (HUE)", H)
    cv2.waitKey(0)