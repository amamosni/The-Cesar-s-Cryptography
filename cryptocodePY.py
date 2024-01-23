#Se importa la libreria base64
import base64

#Funcion para codificar, agregamos un texto y entrega la salida codificada en base64
def codificar(texto):
    result = base64.b64encode(texto)
    print(f"       Texto codificado: {result.decode('utf-8')}")
    return result

#Funcion para descodificar, agregamos un texto codificado en base64, se descodifica y valida si es igual a la entrda original.
def descodificar(texto, codificado):
    descodificado = base64.b64decode(codificado)
    print(f"    Texto descodificado: {descodificado.decode('utf-8')}")
    if descodificado == texto:
        print("************** Si son iguales!")
    else:
        print("********** Algo muy malo paso!")


#Inicio del programa
texto1 = input("     Introduce tu texto: ").encode('utf-8')
result = codificar(texto1)
texto2 = input("Introduce el codificado: ").encode('utf-8')
descodificar(texto1, texto2)
