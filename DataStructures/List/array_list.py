def new_list():
    newlist ={
        'elements': [],
        'size':0,
    }
    return newlist

def get_element(my_list, index):
    
    return my_list["elements"][index]


def is_present(my_list, element, cmp_function):
    size = my_list["size"]
    if size > 0 :
        keyexist = False
        for keypos in range(0, size):
            info = my_list["elements"][keypos]
            if cmp_function(element, info) == 0 :
                keyexist = True
                break
        if keyexist:
            return keypos
    return -1


def first_element(my_list):
    if my_list["size"] == 0:
        return None
    else:
        return my_list["elements"][0]

def last_element(my_list):
    if is_empty(my_list):
        return None
    else:
        return my_list["elements"][my_list["size"] - 1]


def size(my_list):
    return my_list["size"]
       
def add_first(my_list, element):
    my_list["elements"].insert(0, element)
    my_list["size"] += 1
    return my_list

def is_empty(my_list):
    
    if my_list["size"]==0:
        empty = True
    else:
        empty = False 
    return empty
    
    
def add_last(my_list, element):
    my_list["elements"].append(element)
    my_list["size"] += 1
    return my_list


def get_last_element(my_list):
    return my_list[-1]



def get_element(my_list, pos):
    return my_list["elements"][pos]
   #prueba final
   #  
    
def delete_element(my_list, pos):
    new_elements = []
    count = 0
    for item in my_list["elements"]:
        if count == pos:
            count = count + 1
        else:
            new_elements += [item]
            count = count + 1

    my_list["elements"] = new_elements
    my_list["size"] =   my_list["size"] - 1
    return my_list


def remove_first(my_list):
    if my_list["size"] == 0:
        return None
    else:

        element = my_list["elements"].pop(0)
        my_list["size"] = my_list["size"]-1
    
    return element


def remove_last(my_list):
    if my_list["size"] == 0:
        return None
    else:

        element = my_list["elements"].pop(-1)
        my_list["size"] = my_list["size"]-1
    
    return element


def insert_element(my_list, element, pos):
    new_elements = []
    count = 0
    for item in my_list["elements"]:
        if count == pos:
            new_elements += [element]
        new_elements += [item]
        count = count + 1

    if pos == count:
        new_elements += [element]

    my_list["elements"] = new_elements
    my_list["size"] = my_list["size"] + 1
    return my_list



def change_info(my_list, pos, new_info):
    my_list[pos] = new_info
    return my_list


def exchange(my_list, pos_1, pos_2):
    el1 = my_list["elements"][pos_1]
    el2 = my_list["elements"][pos_2]
    my_list["elements"][pos_1] = el2
    my_list["elements"][pos_2] = el1
    return my_list

def sub_list(my_list, pos, numelem):
    i = pos
    contador = 0
    new = new_list()

    while i < len(my_list["elements"]) and contador < numelem:
        new["elements"].append(my_list["elements"][i])
        i +=1
        contador +=1
    
    new["size"] = len(new["elements"])
    return new
        
def default_sort_criteria(element_1, element_2):
   is_sorted = False
   if element_1 < element_2:
      is_sorted = True
   return is_sorted


def insertion_sort(my_list, sort_crit):
 
    e = my_list["elements"]
    for i in range(1, len(e)):
        llave = e[i]
        j = i-1 
        while j >= 0 and sort_crit(llave, e[j]) == True:
            e[j + 1] = e[j]
            j -= 1
        e[j + 1] = llave
    return my_list

def selection_sort(my_list, sort_crit):
    elements = my_list["elements"]
    s = len(elements)

    for i in range(s - 1):
        min_idx = i

        for j in range(i + 1, s):
            if sort_crit(elements[j], elements[min_idx]):
                min_idx = j

        elements[i], elements[min_idx] = elements[min_idx], elements[i]

    return my_list


def shell_sort(list, sort_crit):
    inc = size(list) // 2
    while inc:
        for i, e in enumerate(sub_list(list,0,size(list))["elements"]):  
            while i >= inc and sort_crit(list[i - inc], e):
                list[i] = list[i - inc]
                i -= inc
            list[i] = e
        inc = 1 if inc == 2 else int(inc * 5.0 / 11)
    return list


def merge_sort(my_list, sort_crit):
    if len(my_list["elements"]) <= 1:
        return my_list
    
    else:
        mitad = len(my_list["elements"]) // 2
        iz = merge_sort({'elements': my_list["elements"][:mitad], 'size': mitad}, sort_crit)
        der = merge_sort({'elements': my_list["elements"][mitad:], 'size': my_list["size"] - mitad}, sort_crit)
        return {'elements': merge(iz["elements"], der["elements"], sort_crit), 'size': my_list["size"]}


def merge(iz, der, sort_crit):
    result = []
    i = 0
    j = 0
    while(i < len(iz) and j < len(der)):
        if sort_crit(iz[i], der[j]):
            result.append(iz[i])
            i += 1
        else:
            result.append(der[j])
            j += 1
    result += iz[i:]
    result += der[j:]
    return result

def quick_sort(my_list, sort_crit):
    
    elements = my_list["elements"]
    
    if len(elements) <= 1:
        return my_list
    
    marcador = elements[0]
    menos = [i for i in elements[1:] if sort_crit(i, marcador) == -1]
    igual = [marcador]
    greater = [i for i in elements[1:] if sort_crit(i, marcador) == 1]
    
    sorted_menor = quick_sort({"elements": menos, "size": len(menos)}, sort_crit)
    sorted_menor = quick_sort({"elements": greater, "size": len(greater)}, sort_crit)
    
    sorted_elements = sorted_menor["elements"] + igual + sorted_menor["elements"]
    
    return {"elements": sorted_elements, "size": len(sorted_elements)}
