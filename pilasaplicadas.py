#META 1.6 Pila-Palindromos
"""
1.- Crear un TAD (tipo abstracto de dato), una clase que cumpla con los atributos y metodos que debe tener una pila.

2.- Elaborar un programa en Python que permita identificar si la oracion o palabra capturada por el usuario es un palindromo, usando para ello la estructura creada en el punto anterior.

Entrada de datos: Permitir al usuario la captura de la palabra u oracion a revisar.

Salida: La salida debe incluir lo siguiente: La palabra <capturada por el usuario> SI es un palindromo ó La palabra <capturada por el usuario> NO es un palindromo (Según corresponda).

Y el nombre del alumno que realizo el programa: Programa elaborado por: Mónica Garcia Ruiz

3.- Es indispensable que uses la estructura de datos pila, para resolver este problema.

4- No olvides incluir los comentarios que documentan tu programa.
"""
#EDUARDO MENDOZA GOMEZ

class Pila:
    #Se crea el constructor con la variable tamano como variable
    def __init__(self, tamano):
        #Self. tamano sera usado para referenciar la cantidad de elementos en la lista
        self.tamano = tamano
        #Se muestra la lista iniciando en un arreglo vacio
        self.lista = []
        #Se inicia self.top para saber la ultima posicion del arreglo
        self.top = -1

    #Metodo para determinar si la lista esta vacia
    def esta_vacia(self):
        #En caso de que el top no haya avanzado la lista estara vacia
        if self.top == -1:
            return True
        #De lo contrrario no lo estara
        else:
            return False
    #Metodo para determinar si la lista esta llena
    def esta_llena(self):
        #En caso de que el top sea igual que la ultima posicion la lista estara llena
        if self.top == (self.tamano-1):
            return True
        #De lo contrrario no lo estara
        else:
            return False

    #Metodo para insertar un valor
    def insertar(self, item):
        if self.esta_llena() == False:
            #Se agrega e; valor deseado en la ultima posicion
            self.lista.append(item)
            #Top aumentara en 1 indicando la ultima posicion de la lista
            self.top += 1
        else:
            #print('La pila esta llena...')
            return False

    #Metodo para extraer un valor
    def extraer(self):
        #Si la lista esta vacia no se extrae ningun valor
        if self.esta_vacia() == True:
            #print('La pila esta vacia...')
            return False
        #Si contiene un valor se extrae el ultimo que fue agregado
        else:
            #Se saca el ultimo de la fila
            save = self.lista.pop(self.top)
            #Se guarda el valor extraido en caso de ser necesario
            self.top -=1
        #Se regresa el valor guardado
        return save

#Se pide una palabra
palabra = input('Escribe un palindromo con no mas de 15 letras: ')
# n sera el tamano de la pila
n = int(len(palabra))
#Se valida que el tamano no sea mayor a quince
if n > 15:
    print('ERROR!.... Palabra con mas de 15 letras...')
#De ser menor a quince el programa se ejecuta
else:
    #Se crea la pila a
    a = Pila(n)
    #Ciclo for para copiar las letras de la palabra en la pila
    for i in range (n):
        a.insertar(palabra[i])
    #Variables j para comprobar que las letras sean iguales
    j= False
    #j_2 sera True desde un inicio hasta que haya una diferencia en letras, esta sirve para evitar que palabras que solo comparten las letras del centro sean detectadas como palindromos
    j_2 = True
    #Ciclo for para ir comparando la primer letra con la ultima
    for i in range(n//2):
        #Si son iguales
        if a.extraer() == a.lista[i]:
            #J sera verdadera
            j = True
        else:
            #Si no, ambas seran negativas
            j = False
            j_2 = False
    #Si ambas j son verdaderas la palabra es palindromo
    if j == True and j_2 == True:
        print('La palabra es palindromo!!')
    #Si j no es verdadero la palabra no es palindromo
    else:
        print('La palabra no es palindromo...')

#ULTIMA MODIFICACION 7 DE SEPTIEMBRE DEL 2021 A LAS 11:55 AM, TIJUANA BAJA CALIFORNIA