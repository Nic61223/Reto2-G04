import time
import csv
csv.field_size_limit(2147483647)
import sys
default_limit = 1000
sys.setrecursionlimit(default_limit*10)
import os
from DataStructures.List import array_list as lt
from DataStructures.List import single_linked_list as sl
from DataStructures.Map import map_linear_probing as lp
from DataStructures.Map import map_separate_chaining as sp

data_dir = os.path.dirname(os.path.realpath('__file__')) + '/Data/'
def new_logic():
    """
    Crea el catalogo para almacenar las estructuras de datos
    """




def new_logic():
    """
    Inicializa el catálogo de libros. Crea una lista vacía para guardar
    los libros y utiliza tablas de hash para almacenar los datos restantes con diferentes índices
    utilizando linear probing como tipo de tabla de hash
    """
    catalog =  lp.new_map(500000, 0.5)

    return catalog


# Funciones para la carga de datos

def sort_criteria(element_1, element_2):
    fecha1 = element_1[:10]
    año1, mes1, dia1 = map(int, fecha1.split("-"))
    año2, mes2, dia2 = map(int, fecha2.split("-"))

    if int(año1) < int(año2):
        return True
    elif int(año1) == int(año2):
        if int(mes1) < int(mes2):
            return True
        elif int(mes1) == int(mes2):
            if int(dia1) < int(dia2):
                return True
    return False


def load_data(catalog, filename):
    """
    Carga los datos del reto
    """
    t1 = get_time()

    input_file = csv.DictReader(open(data_dir, encoding='utf-8'))
    indice = 0
    total = 0
    menor = float('inf')
    mayor = 0
    primeros = lt.new_list
    ultimos = lt.new_list
    for registro in input_file:
        lp.put(catalog, indice, registro )
        año = registro["year_collection"]
        
        if año > mayor:
            mayor = año
        if año < menor:
            menor = año


        indice += 1
        total += 1
    print ("registros cargados")   
    lt.quick_sort(catalog,sort_criteria)
    Print(" catalogo ordenado")
    
    
    
    primero = total - 6
    for i in range(5):
        lt.add_last(ultimos, lp.get(catalog,primero))
        primer += 1
        
    t2 = get_time()
    times = round(delta_time(t1,t2),2)
    respuesta =( catalog, times, total, menor, mayor, primeros, ultimos)

    return respuesta


        
    
    

# Funciones de consulta sobre el catálogo

def get_data(catalog, id):
    """
    Retorna un dato por su ID.
    """
    #TODO: Consulta en las Llamar la función del modelo para obtener un dato
    pass


def req_1(catalog):
    """
    Retorna el resultado del requerimiento 1
    """
    # TODO: Modificar el requerimiento 1
    pass


def req_2(catalog):
    """
    Retorna el resultado del requerimiento 2
    """
    # TODO: Modificar el requerimiento 2
    pass


def req_3(catalog):
    """
    Retorna el resultado del requerimiento 3
    """
    # TODO: Modificar el requerimiento 3
    pass


def req_4(catalog):
    """
    Retorna el resultado del requerimiento 4
    """
    # TODO: Modificar el requerimiento 4
    pass


def req_5(catalog):
    """
    Retorna el resultado del requerimiento 5
    """
    # TODO: Modificar el requerimiento 5
    pass

def req_6(catalog):
    """
    Retorna el resultado del requerimiento 6
    """
    # TODO: Modificar el requerimiento 6
    pass


def req_7(catalog):
    """
    Retorna el resultado del requerimiento 7
    """
    # TODO: Modificar el requerimiento 7
    pass


def req_8(catalog):
    """
    Retorna el resultado del requerimiento 8
    """
    # TODO: Modificar el requerimiento 8
    pass


# Funciones para medir tiempos de ejecucion

def get_time():
    """
    devuelve el instante tiempo de procesamiento en milisegundos
    """
    return float(time.perf_counter()*1000)


def delta_time(start, end):
    """
    devuelve la diferencia entre tiempos de procesamiento muestreados
    """
    elapsed = float(end - start)
    return elapsed
