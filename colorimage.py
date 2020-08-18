import numpy as np #librería en la que se define un tipo de dato que representa matrices multidimensionales
# además incluye algunas funcionalidades básicas para trabajar con ellas

import os  #libreria para el acceso portable a funciones específicas del sistema operativo
import cv2 #OpenCV es una biblioteca libre de visión artificial originalmente desarrollada por Intel


class colorimag:

    def __init__(self,imag):
        image=cv2.imread(imag) #Se importa la imagen de la direccion fijada
        self.image=image       #Se guarda la imagen en self

    def displayProperties(self):   # método para obtener alto y ancho de la imagen
        alto,ancho,canales=self.image.shape #se obtienen las dimensiones de la imagen
        print ('ancho:',ancho,'alto:',alto) #se imprime el alto y el ancho de la imagen

    def makeGray(self):            # método en que se obtiene la imagen en escala de grises
        return cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY) #retorna la imagen convertida a escala de grises

    def colorizeRGB(self,color):   #metodo para obtener la imagen colorizada en el color especificado (blue,green,red)
        gris=cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY) #convierte la imagen a escala de grises
        b, g, r = cv2.split(self.image) #se separa la imagen en los canales b,g,r

        if color=='blue': #si se selecciona blue vuelve la imagen azuloza
            b = gris     #se iguala el canal seleccionado a la imagen en escala de grises
            only_c = cv2.merge((b, g, r)) #se unen los canales para obtener imagen bgr
            only_c[:, :, 1] = 0 #se hace 0 la componente green de la imagen
            only_c[:, :, 2] = 0 #se hace 0 la componente red de la imagen

        elif color =='green': #si se selecciona green vuelve la imagen verdoza
            g = gris  #se iguala el canal seleccionado a la imagen en escala de grises
            only_c = cv2.merge((b, g, r)) #se unen los canales para obtener imagen bgr
            only_c[:, :, 0] = 0 #se hace 0 la componente blue de la imagen
            only_c[:, :, 2] = 0 #se hace 0 la componente red de la imagen

        elif color =='red': #si se selecciona red vuelve la imagen rojiza
            r = gris #se iguala el canal seleccionado a la imagen en escala de grises
            only_c = cv2.merge((b, g, r))
            only_c[:, :, 0] = 0 #se hace 0 la componente blue de la imagen
            only_c[:, :, 1] = 0 #se hace 0 la componente green de la imagen

        return only_c #se retorna la imagen colorizada

    def makeHue(self):   # método en que se devuelve una imagen que resalta los tonos (Hue) de la imagen
        hsv=cv2.cvtColor(self.image, cv2.COLOR_BGR2HSV) #convierte la imagen a escala de espacio BGR a HSV
        hsv[:, :, 1] = 255   #se hace maxima la componente S de la imagen
        hsv[:, :, 2] = 255   #se hace maxima la componente V de la imagen
        bgr=cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR) #convierte la imagen a escala de espacio HSV a BGR

        return  bgr #retorna la imagen que resalta los tonos (Hue) de la imagen original.






