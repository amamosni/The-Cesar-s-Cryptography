# Base 64 hostoria
Base64 es un algoritmo de codificación que permite transformar cualquier carácter de cualquier idioma en un alfabeto que consta de letras, dígitos y signos latinos. Con esto podemos convertir caracteres especiales como logogramas chinos, emojis e incluso imágenes en una secuencia "legible" (para cualquier ordenador), que se puede guardar y/o transferir en cualquier otro lugar. A menudo se utiliza para transmitir datos binarios por medio de transmisiones que tratan sólo con texto, como para enviar imágenes y archivos adjuntos por correo electrónico.

Su alfabeto consta de 64 caracteres (,,, [A-Z][a-z]"[0-9]/" y "+"), que dieron lugar a su nombre. El carácter – se utiliza como un sufijo especial, y la especificación original (RFC 989) ha definido que el símbolo * se puede utilizar para delimitar los datos convertidos pero sin cifrar dentro de una secuencia.

En resumen es tomar cada caracter y pasarlo a su respectiva tabla ASCII de 256 caracteres y de alli a base 64, codigo binario de 6 bits (2^6). Para descifrar se representa cada caracter en su valor binario y agrupando de 8 en 8 bits y asignando a cada bloque el codigo ASCII correspondiente.
Tomado de:  https://marquesfernandes.com/es/tecnologia-es/que-y-base64-para-que-serve-y-como-funciona/
            https://www.youtube.com/watch?v=TvlHDA0J7QM
            https://hackwise.mx/cual-es-la-diferencia-entre-codificacion-cifrado-y-hashing/


Uso del archivo cryptocodePY.py

El archivo contiene dos funciones.
1. #Funcion para codificar, agregamos un texto y entrega la salida codificada en base64
2. #Funcion para descodificar, agregamos un texto codificado en base64, se descodifica y valida si es igual a la entrda original.

Una vez corras el programa se pedira el texto a codificar y entregara una salida del texto en base64,
luego te pedira que introduzcas la salida para descodificar y validar si es igual a tu texto inicial.