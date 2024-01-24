#Practica 1.4 Pila-Colas
#Hacer un programa que cumpla con las instrucciones de la Practica 1.4
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
                #Se agrega el valor deseado en la ultima posicion
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
                print('La pila esta vacia...')
                return False
            #Si contiene un valor se extrae el ultimo que fue agregado
            else:
                #Se saca el ultimo de la fila
                save = self.lista.pop(self.top)
                #Se guarda el valor extraido en caso de ser necesario
                self.top -=1
            #Se regresa el valor guardado
            return save

        #Metodo para identificar el valor maximo en la lista
        def max(self):
            #Si la lista esta vacia se imprimira un mensaje diciendo que no hay valor maximo
            if self.esta_vacia() == True:
                print('La pila esta vacia y por ello no hay valor maximo...')
                return False
            #Si no es asi por medio de un for se ira comparando la posicion 0 actualizando la variable mayor cada vez que se encuentre un valor mayor al de la posicion 0
            else:
                mayor = self.lista[0]
                for i in range(self.top+1):
                    if self.lista[i] > mayor:
                        mayor = self.lista[i]
                #Se regresa e imprimer el numero identificado como el mayor
                print(mayor)
                return mayor

class Cola:
    # Se crea el constructor con la variable tamano como variable
    def __init__(self, tamano):
        # Self. tamano sera usado para referenciar la cantidad de elementos en la lista
        self.tamano = tamano
        # Se muestra la lista iniciando en un arreglo vacio
        self.lista = []
        # Se inicia self.top para saber la ultima posicion del arreglo
        self.top = -1

    # Metodo para determinar si la lista esta vacia
    def esta_vacia(self):
        # En caso de que el top no haya avanzado la lista estara vacia
        if self.top == -1:
            return True
        # De lo contrrario no lo estara
        else:
            return False

    # Metodo para determinar si la lista esta llena
    def esta_llena(self):
        # En caso de que el top sea igual que la ultima posicion la lista estara llena
        if self.top == (self.tamano - 1):
            return True
        # De lo contrrario no lo estara
        else:
            return False

    # Metodo para insertar un valor
    def inserar(self, item):
        if self.esta_llena() == False:
            # Se agrega e; valor deseado en la ultima posicion
            self.lista.append(item)
            # Top aumentara en 1 indicando la ultima posicion de la lista
            self.top += 1
        else:
            # print('La pila esta llena...')
            return False

    # Metodo para extraer un valor
    def extraer(self):
        # Si la lista esta vacia no se extrae ningun valor
        if self.esta_vacia() == True:
            # print('La pila esta vacia...')
            return False
        # Si contiene un valor se extrae el ultimo que fue agregado
        else:
            # Se saca el ultimo de la fila
            save = self.lista.pop(0)
            # Se guarda el valor extraido en caso de ser necesario
            self.top -= 1
        #Se regresa el valor guardado
        return save

def ask_for_integer(text_to_show): #Metodo para pedir un entero sacado de la clase de Programacion Orientada a Objetos
        while True:
            try:
                num = int(input(text_to_show))
                break
            except ValueError:
                print('INVALID: Please input integer only. . .')
                continue
            except SyntaxError:
                print('INVALID: Please input integer only. . .')
                continue
            except NameError:
                print('INVALID: Please input integer only. . .')
                continue

        return num

def validar_int (numero,text): #Funcion para validar que lo que se teclea sea un numero

    while True:
        try:
            #En caso de lo que se mande sea un 0 se regresara un 0, esto se hizo denbido a que int('0') no era detectado
            if numero == ' 0':
                break
                return 0
            #num sera la cadena que se mande convertida a entero
            num = int(numero)
            #Se regresa el numero y se acaba la funcion
            return num
            break
        #Excepts para errores comunes que pasan si la cadena que se envia no es verdadero
        except ValueError:
            #Se imprime el mismo mensaje que en los otros errores
            print(f'INVALIDO: Solo digite enteros despues de "{text}". . .')
            # En todos los errores se regresa un False y se acaba la funcion
            return False
            break
        except SyntaxError:
            print(f'INVALIDO: Solo digite enteros despues de "{text}". . .')

            return False
            break
        except NameError:
            print(f'INVALIDO: Solo digite enteros despues de "{text}". . .')

            return False
            break

if __name__ == "__main__":

    #Se llama el metodo para pedir un numero para pedir el numero de instrucciones que se van a usar
    n = ask_for_integer('')

    #Ciclo while para validar que el numero no sea ni mayor a 400,000 ni menor a 1 como indican las instrucciones
    while n < 1 or n > 400000:
        n= ask_for_integer('ERROR!...... el numero debe estar en un rango de 1 a 400,000...Digite de nuevo: ')
    #Se crea el objeto lista que pertenecera a la clase Pila con el numero de instrucciones como parametro
    lista = Pila(n)

    #Se crea el objeto ordenes que pertenecera a la clase Cola con el numero de instrucciones como parametro
    ordenes = Cola(n)

    #contador i para el segundo ciclo while que no acabara hasta que llegue al numero de instrucciones sea alcanzado
    i = 0
    while i < n:
        #Se crea la entrada orden que recibira lo que el usuario teclee
        orden = input('')

        #Si las primeras 4 letras son "push" se cumplira
        if orden[:4] == 'push':
            #Cuando la funcion validar_int regrese un False el contador retrocera en 1
            if validar_int(orden[4:],'push') == False:
                i -= 1
            #Si la misma funcion regresa un numero que no este dentro de [0-105] se regresara la cuenta e imprimira un mensaje de que no es valido
            elif int(orden[4:]) < 0 or int(orden[4:]) > 105:
                print('INVALIDO:.. No digitar un numero mayor a 105 ni menor a 0...')
                i-= 1
            #Si pasa los 2 flintros se enviara lo tecleado como parametro a la cola ordenes
            else:
                ordenes.inserar(orden)

        #Si se digita max o pop
        elif orden == 'max' or orden == 'pop':
            #Si es lo primero que se teclea enviara un mensaje diciendo que la pila se encuentra vacia y la cuenta no avanzara
            if i <= 0:
                print('Opcion no valida... la pila se encuentra vacia')
                i -= 1
            #Si pasa el filtro anterior se manda lo escrito como parametro a la cola
            else:
                ordenes.inserar(orden)
        #Si no se digita ninguna de las opciones la cuenta no avanzara
        else:
            print('Opcion no valida... digita de nuevo...')
            i -= 1
        i += 1

    #print(ordenes.lista)

    #Ciclo for para ejecutar las ordenes dadas en la cola
    for j in range (n):
        #Orden sera el valor extraido de la cola cuando se llama el metodo extraer
        orden = ordenes.extraer()

        #Si los primeros 4 cuaracteres son 'push' se llamara el metodo insertar con el numero que va despues del push
        if orden[:4] == 'push':

            lista.insertar(int(orden[4:]))

        #Si orden es igual a max se llama el metodo max que imprimira cual es el valor maximo de la lista
        elif orden == 'max':
            lista.max()

        #Si los caracteres del orden son igual pop se llamara el metodo extraer
        elif orden == 'pop':
            lista.extraer()

    #Finalmente se imprimira la lista
    print(lista.lista)

# ULTIMA MODIFICACION 9 DE SEPTIEMBRE DEL 2021 A LAS 7:55 PM, TIJUANA BAJA CALIFORNIA