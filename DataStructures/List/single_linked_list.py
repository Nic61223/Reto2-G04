from DataStructures.List import list_node as n

def new_list():
    newlist = {
        "first": None,
        "last": None,
        "size": 0,
    }
    return newlist

def get_element(my_list, pos):
    searchpos = 0
    node = my_list["first"]
    while searchpos < pos:
        node = node["next"]
        searchpos += 1
    return node["info"] 

def is_present(my_list, element, cmp_function):
    is_in_array= False
    temp = my_list["first"]
    count = 0
    while not is_in_array and temp is not None:
        if cmp_function(element, temp["info"]) == 0:
            is_in_array = True
        else:
            temp = temp["next"]
            count += 1
    if not is_in_array:
        count = -1
    return count

def add_first(my_list, element):
    node = n.new_single_node(element)
    if my_list["size"]== 0:
        my_list["first"] = node
    
    else:
        node["next"] = my_list["first"]
        my_list["first"] = node
    
    if my_list["last"] is None:
        my_list["last"] = node
    my_list["size"] += 1
    
    return my_list


def add_last(my_list, element):
    
    node = {
        "info": element,
        "next": None
    }
    if my_list["size"] == 0:
        my_list["first"] = node
        my_list["last"] = node
    else:
        my_list["last"]["next"] = node
        my_list["last"] = node
    my_list["size"] += 1

def size(my_list):
    
    return my_list["size"]   

def first_element(my_list):

    return my_list["first"]["info"]


def is_empty(my_list):
    
    if my_list["size"]==0:
        empty = True
    else:
        empty = False 
    return empty


def last_element(my_list):


    return my_list["last"]["info"]


def remove_first(my_list):
    if my_list["size"] == 0:
        return None
    
    node = my_list["first"]["info"]

    my_list["first"] = my_list["first"]["next"] 

    my_list["size"] -= 1

    if my_list["size"] == 0:  
        my_list["last"] = None
        my_list["first"] = None
    
    
    return node
#final test

def remove_last(my_list):
    if my_list["size"] == 0:
        return None
    element = my_list["last"]["info"]
   
    if my_list["size"] == 1:
        my_list["first"] = None
        my_list["last"] = None
        my_list["size"] = 0
    
    else:

        node = my_list["first"]
        
        while node["next"] != my_list["last"]:

            node = node["next"]
        node["next"] = None
        my_list["last"] = node
        my_list["size"] -= 1
    return element

def insert_element(my_list, element, pos):
    node = n.new_single_node(element)
    if pos < 0 or pos > size(my_list):
        print("posicion no valida")
        return my_list
    elif pos == 0:
        node["next"] = my_list["first"]
        my_list["first"] = node
        if my_list["last"] is None:
            my_list["last"] = node
        my_list["size"] += 1
        return my_list
    
    temp = my_list["first"]
    for i in range(pos - 1):
        temp = temp["next"]
    
    node["next"] = temp["next"]
    temp["next"] = node
    my_list["size"] += 1
    return my_list


def delete_element(my_list, pos):

    if pos == 0:
        my_list["first"] = my_list["first"]["next"]

    else:
        temp = my_list["first"]
        actual_pos = 0

        while actual_pos < pos-1:
            temp = temp["next"]
            actual_pos +=1
        temp["next"]= temp["next"]["next"]
        my_list["size"] -= 1

    return my_list


def change_info(my_list, pos, new_info):
    
    temp= my_list["first"]
    actual_pos = 0
    while actual_pos < pos:
        temp = temp["next"]
        actual_pos += 1
    temp["info"] = new_info
    
    return my_list

def sub_list(my_list, pos, newelem):
    sublst = new_list()
    i = 0

    while i < newelem and pos < size(my_list):
        element = get_element(my_list, pos)
        add_last(sublst, element)
        pos += 1
        i += 1

    return sublst


def exchange(my_list, pos1, pos2):
    p1= my_list["first"]
    p2 = my_list["first"]
    c1 = 0
    c2 = 0
    while c1< pos1:
        p1 = p1["next"]
        c1 +=1
    e1= p1["info"]


    while c2 < pos2:
        p2 = p2["next"]
        c2 += 1
    e2 = p1["info"]


    p1["info"] = e2
    p2["info"] = e1

    return my_list

def default_sort_criteria(element_1, element_2):

   is_sorted = False
   if element_1 < element_2:
      is_sorted = True
   return is_sorted

def insertion_sort(my_list, sort_crit):
    n = size(my_list)
    if n == 0:
        return my_list
    i = 1
    while i < n:
        j = i
        while j > 0 and sort_crit(get_element(my_list, j - 1), get_element(my_list, j)) == 1:
            exchange(my_list, j - 1, j)
            j -= 1
        i += 1
    return my_list


    
def selection_sort(my_list, sort_crit):
    if my_list["size"] <= 1:
        return my_list
    current = my_list["first"]
    while current:
        min = current
        i = current["next"]
        while i:
            if sort_crit(i["info"], min["info"]):
                min = i
            i = i["next"]
        current["info"], min["info"] = min["info"], current["info"]
        current = current["next"]

    return my_list



def shell_sort(my_list, sort_criteria):

    inc = size(my_list) // 2
    while inc:
        for i in range(inc, size(my_list)):
            temp = get_element(my_list, i)
            j = i
            while j >= inc and sort_criteria(temp, get_element(my_list, j - inc)):
                change_info(my_list, j, get_element(my_list, j - inc))
                j -= inc
            change_info(my_list, j, temp)
        inc = 1 if inc == 2 else inc * 5 // 11

def merge_sort(my_list, sort_criteria):
    if size(my_list) <= 1:
        return my_list
    
    else:
        mitad = size(my_list) // 2
        iz = sub_list(my_list, 0, mitad)
        der = sub_list(my_list, mitad, size(my_list) - mitad)
        iz = merge_sort(iz, sort_criteria)
        der = merge_sort(der, sort_criteria)
        return merge(iz, der, sort_criteria)

def merge(left, right, sort_criteria):
    result = new_list()
    while not is_empty(left) and not is_empty(right):
        if sort_criteria(first_element(left), first_element(right)):
            add_last(result, remove_first(left))
        else:
            add_last(result, remove_first(right))
    
    while not is_empty(left):
        add_last(result, remove_first(left))
    
    while not is_empty(right):
        add_last(result, remove_first(right))
    
    return result


def quick_sort(my_list, sort_crit):
    
    if size(my_list) <= 1:
        return my_list

    marca = get_element(my_list, 0)
    menor, igual, mayor = new_list(), new_list(), new_list()
    
    i = 0
    
    while i < size(my_list):
        elem = get_element(my_list, i)
        if sort_crit(elem, marca) == -1:
            add_last(menor, elem)
        elif sort_crit(elem, marca) == 0:
            add_last(igual, elem)
        else:
            add_last(mayor, elem)
        i += 1

    menor = quick_sort(menor, sort_crit)
    mayor = quick_sort(mayor, sort_crit)

    result = new_list()
    
    while size(menor) > 0:
        add_last(result, remove_first(menor))
    while size(igual) > 0:
        add_last(result, remove_first(igual))
    while size(mayor) > 0:
        add_last(result, remove_first(mayor))

    return result

