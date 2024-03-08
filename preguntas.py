"""
Laboratorio de Programación Básica en Python para Manejo de Datos
-----------------------------------------------------------------------------------------

Este archivo contiene las preguntas que se van a realizar en el laboratorio.

No puede utilizar pandas, numpy o scipy. Se debe utilizar solo las funciones de python
básicas.

Utilice el archivo `data.csv` para resolver las preguntas.


"""
def pregunta_01():
    with open("./data.csv") as data:
        datos = data.readlines()
        datos = [linea.split("\t") for linea in datos]
        suma = sum([int(x[1]) for x in datos])
    
    return suma




def pregunta_02():
    """
    Retorne la cantidad de registros por cada letra de la primera columna como la lista
    de tuplas (letra, cantidad), ordendas alfabéticamente.

    Rta/
    [
        ("A", 8),
        ("B", 7),
        ("C", 5),
        ("D", 6),
        ("E", 14),
    ]

    """
    list_letras = []
    with open("./data.csv") as data:
        datos = data.readlines()
        datos = [linea.split("\t") for linea in datos]
        letras = set([x[0] for x in datos])

        for letra in letras:
            cant_letras = [1 for x in datos if x[0]==letra]
            list_letras.append((letra, sum(cant_letras)))

    list_letras.sort(key= lambda x: x[0])

    return list_letras


def pregunta_03():
    """
    Retorne la suma de la columna 2 por cada letra de la primera columna como una lista
    de tuplas (letra, suma) ordendas alfabeticamente.

    Rta/
    [
        ("A", 53),
        ("B", 36),
        ("C", 27),
        ("D", 31),
        ("E", 67),
    ]

    """
    list_letras = []
    with open("./data.csv") as data:
        datos = data.readlines()
        datos = [linea.split("\t") for linea in datos]
        letras = set([x[0] for x in datos])

        for letra in letras:
            cant_letras = [int(x[1]) for x in datos if x[0]==letra]
            list_letras.append((letra, sum(cant_letras)))

    list_letras.sort(key= lambda x: x[0])

    return list_letras

def pregunta_04():
    """
    La columna 3 contiene una fecha en formato `YYYY-MM-DD`. Retorne la cantidad de
    registros por cada mes, tal como se muestra a continuación.

    Rta/
    [
        ("01", 3),
        ("02", 4),
        ("03", 2),
        ("04", 4),
        ("05", 3),
        ("06", 3),
        ("07", 5),
        ("08", 6),
        ("09", 3),
        ("10", 2),
        ("11", 2),
        ("12", 3),
    ]

    """
    list_meses = []
    with open("./data.csv") as data:
        datos = data.readlines()
        datos = [linea.split("\t") for linea in datos]
        
        for mes in range(1, 13):
            cant_meses = [1 for elemento in datos if int(elemento[2].split("-")[1]) == mes]
            mes = str(mes).rjust(2, "0")
            list_meses.append((str(mes), len(cant_meses)))

    return list_meses

def pregunta_05():
    """
    Retorne una lista de tuplas con el valor maximo y minimo de la columna 2 por cada
    letra de la columa 1.

    Rta/
    [
        ("A", 9, 2),
        ("B", 9, 1),
        ("C", 9, 0),
        ("D", 8, 3),
        ("E", 9, 1),
    ]

    """    
    list_letras = []
    with open("./data.csv") as data:
        datos = data.readlines()
        datos = [linea.split("\t") for linea in datos]
        letras = set([x[0] for x in datos])

        for letra in letras:
            cant_letras = [int(x[1]) for x in datos if x[0]==letra]
            max_l = max(cant_letras)
            min_l = min(cant_letras)
            list_letras.append((letra, max_l, min_l))

    list_letras.sort(key= lambda x: x[0])

    return list_letras




def pregunta_06():
    """
    La columna 5 codifica un diccionario donde cada cadena de tres letras corresponde a
    una clave y el valor despues del caracter `:` corresponde al valor asociado a la
    clave. Por cada clave, obtenga el valor asociado mas pequeño y el valor asociado mas
    grande computados sobre todo el archivo.

    Rta/
    [
        ("aaa", 1, 9),
        ("bbb", 1, 9),
        ("ccc", 1, 10),
        ("ddd", 0, 9),
        ("eee", 1, 7),
        ("fff", 0, 9),
        ("ggg", 3, 10),
        ("hhh", 0, 9),
        ("iii", 0, 9),
        ("jjj", 5, 17),
    ]

    """
    rta_dict = {}
    my_list = []
    with open("./data.csv") as data:
        datos = data.readlines()
        datos = [linea.replace("\n", "").split("\t") for linea in datos]
        cad_dict = [linea[4].split(",") for linea in datos]

        # Pasar cada elemento a un diccionario
        for elementos in cad_dict:
            
            for elemento in elementos:
                valores = elemento.split(":")
                if valores[0] in rta_dict:
                    rta_dict[valores[0]] += [int(valores[1])]
                else:
                    rta_dict[valores[0]] = [int(valores[1])]
        
        for llave, valor in rta_dict.items():
            my_list.append((llave, min(valor), max(valor)))

        my_list.sort(key=lambda x: x[0])


    return my_list



def pregunta_07():
    """
    Retorne una lista de tuplas que asocien las columnas 0 y 1. Cada tupla contiene un
    valor posible de la columna 2 y una lista con todas las letras asociadas (columna 1)
    a dicho valor de la columna 2.

    Rta/
    [
        (0, ["C"]),
        (1, ["E", "B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E", "E", "D"]),
        (4, ["E", "B"]),
        (5, ["B", "C", "D", "D", "E", "E", "E"]),
        (6, ["C", "E", "A", "B"]),
        (7, ["A", "C", "E", "D"]),
        (8, ["E", "D", "E", "A", "B"]),
        (9, ["A", "B", "E", "A", "A", "C"]),
    ]

    """
  
    with open("./data.csv") as data:
        datos = data.readlines()
        datos = [linea.split("\t") for linea in datos]
        
        my_letters = []
        for i in range(10):

            letras = [linea[0] for linea in datos if int(linea[1]) == i]
            my_letters.append((i, letras))
            letras = []

    
    return my_letters

def pregunta_08():
    """
    Genere una lista de tuplas, donde el primer elemento de cada tupla contiene  el valor
    de la segunda columna; la segunda parte de la tupla es una lista con las letras
    (ordenadas y sin repetir letra) de la primera  columna que aparecen asociadas a dicho
    valor de la segunda columna.

    Rta/
    [
        (0, ["C"]),
        (1, ["B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E"]),
        (4, ["B", "E"]),
        (5, ["B", "C", "D", "E"]),
        (6, ["A", "B", "C", "E"]),
        (7, ["A", "C", "D", "E"]),
        (8, ["A", "B", "D", "E"]),
        (9, ["A", "B", "C", "E"]),
    ]

    """
    with open("./data.csv") as data:
        datos = data.readlines()
        datos = [linea.split("\t") for linea in datos]
        
        my_letters = []
        for i in range(10):

            letras = set(linea[0] for linea in datos if int(linea[1]) == i)
            letras = list(letras)
            letras.sort()
            my_letters.append((i, letras))
      

    return my_letters





def pregunta_09():
    """
    Retorne un diccionario que contenga la cantidad de registros en que aparece cada
    clave de la columna 5.

    Rta/
    {
        "aaa": 13,
        "bbb": 16,
        "ccc": 23,
        "ddd": 23,
        "eee": 15,
        "fff": 20,
        "ggg": 13,
        "hhh": 16,
        "iii": 18,
        "jjj": 18,
    }

    """
    rta_dict = {}
    with open("./data.csv") as data:
        datos = data.readlines()
        datos = [linea.replace("\n", "").split("\t") for linea in datos]
        cad_dict = [linea[4].split(",") for linea in datos]

        # Pasar cada elemento a un diccionario
        for elementos in cad_dict:
            
            for elemento in elementos:
                valores = elemento.split(":")
                if valores[0] in rta_dict:
                    rta_dict[valores[0]] += 1
                else:
                    rta_dict[valores[0]] = 1

        rta_dict = dict(sorted(rta_dict.items()))

    return rta_dict

def pregunta_10():
    """
    Retorne una lista de tuplas contengan por cada tupla, la letra de la columna 1 y la
    cantidad de elementos de las columnas 4 y 5.

    Rta/
    [
        ("E", 3, 5),
        ("A", 3, 4),
        ("B", 4, 4),
        ...
        ("C", 4, 3),
        ("E", 2, 3),
        ("E", 3, 3),
    ]


    """
    my_list = []

    with open("./data.csv") as data:
        datos = data.readlines()
        datos = [linea.split("\t") for linea in datos]

        for linea in datos: 
            col_cnco = linea[4].count(",") + 1
            col_ctro = linea[3].count(",") + 1
            my_list.append((linea[0], col_ctro, col_cnco))
    
    return my_list
    


def pregunta_11():
    """
    Retorne un diccionario que contengan la suma de la columna 2 para cada letra de la
    columna 4, ordenadas alfabeticamente.

    Rta/
    {
        "a": 122,
        "b": 49,
        "c": 91,
        "d": 73,
        "e": 86,
        "f": 134,
        "g": 35,
    }


    """
    my_dict = {}
    with open("./data.csv") as data:
        datos = data.readlines()
        datos = [linea.split("\t") for linea in datos]

        for linea in datos:
            letras = linea[3].split(",")

            for letra in letras:
                if letra in my_dict:
                    my_dict[letra] += int(linea[1])
                else:
                    my_dict[letra] = int(linea[1])
        
    my_dict = dict(sorted(my_dict.items()))
    return my_dict




def pregunta_12():
    """
    Genere un diccionario que contengan como clave la columna 1 y como valor la suma de
    los valores de la columna 5 sobre todo el archivo.

    Rta/
    {
        'A': 177,
        'B': 187,
        'C': 114,
        'D': 136,
        'E': 324
    }

    """
    rta_dict = {}
    with open("./data.csv") as data:
        datos = data.readlines()
        datos = [linea.replace("\n", "").split("\t") for linea in datos]
        cad_dict = [linea[4].split(",") for linea in datos]

        # Pasar cada elemento a un diccionario
        for linea in datos:
            col_cin = linea[4].split(",")
            sum_col = sum([int(x[4::]) for x in col_cin])

            if linea[0] in rta_dict:
                
                rta_dict[linea[0]] += sum_col
            else:
                rta_dict[linea[0]] = sum_col

        rta_dict = dict(sorted(rta_dict.items()))
    return rta_dict

   



