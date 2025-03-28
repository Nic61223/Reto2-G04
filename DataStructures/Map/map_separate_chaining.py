from DataStructures.Map import map_entry as me
from DataStructures.Map import map_functions as mf
from DataStructures.List import array_list as al
from DataStructures.List import single_linked_list as sl
import random

def new_map(num_elements, load_factor, prime=109345121):
    
    capacity = mf.next_prime(int(num_elements / load_factor))
    
    map = {
        "prime" : prime,
        "capacity" : capacity,
        "scale" : 1, 
        "shift": 0, 
        "table": al.new_list(),
        "current_factor" : 0,
        "limit_factor" : load_factor,
        "size" : 0
           }

    for i in range(capacity):
        al.add_last(map["table"], sl.new_list())
    
    return map

def find_slot(map, key, index):
    for i in range(map["capacity"]):
        pos = (index + i) % map["capacity"]
        bucket = al.get_element(map["table"], pos)
        
        if bucket["first"] is None:
            return (False, pos)
        node = bucket["first"]
        while node is not None:
            if node["info"]["key"] == key:
                return (True, pos)
            node = node["next"]

    return (False, -1)
def put(my_map, key, value):
    hash_key = mf.hash_value(my_map, key)
    occupied, pos = find_slot(my_map, key, hash_key)
    bucket = al.get_element(my_map["table"], pos)

    if occupied:
        node = bucket["first"]
        while node is not None:
            if node["info"]["key"] == key:
                node["info"]["value"] = value
                return my_map
            node = node["next"]
    else:
        sl.add_last(bucket, me.new_map_entry(key, value))
        my_map["size"] += 1
        my_map["current_factor"] = my_map["size"] / my_map["capacity"]

    if my_map["current_factor"] >= my_map["limit_factor"]:
        my_map = rehash(my_map)

    return my_map

def contains(my_map, key):
    hash_value = mf.hash_value(my_map, key)
    ocuppied, pos = find_slot(my_map, key, hash_value)
    return ocuppied

def get(my_map, key):
    index = mf.hash_value(my_map, key)
    ocuppied, pos = find_slot(my_map, key, index)
    bucket = al.get_element(my_map["table"], pos)
    
    if ocuppied:
        node = bucket["first"]
        while node is not None:
            if node["info"]["key"] == key:
                return me.get_value(node["info"])
            node = node["next"]
    else:
        return None

def remove(my_map, key):
    index = mf.hash_value(my_map, key)
    occupied, pos = find_slot(my_map, key, index)
    bucket = al.get_element(my_map["table"], pos)

    if occupied:
        node = bucket["first"]
        i = 0
        while node is not None:
            if node["info"]["key"] == key:
                sl.delete_element(bucket, i)
                my_map["size"] -= 1
                return my_map
            i += 1

def size(my_map):
    return my_map["size"]

def is_empty(my_map):
    return my_map["size"] == 0
    


def key_set(my_map):
    keys = al.new_list()
    elements = my_map["table"]["elements"]
    
    for entry in elements:
        current = entry["first"]
        while current is not None:
            al.add_last(keys, current["info"]["key"])
            current = current["next"]
    
    return keys

def value_set(my_map):
    values = al.new_list()
    elements = my_map["table"]["elements"]
    
    for entry in elements:
        current = entry["first"]
        while current is not None:
            al.add_last(values, current["info"]["value"])
            current = current["next"]
    
    return values

def rehash(my_map):
    new = new_map(mf.next_prime(my_map["capacity"] * 2), my_map["limit_factor"])

    for i in range(al.size(my_map["table"])):
        element = al.get_element(my_map["table"], i)
        
        if not sl.size(element) == 0:
            nodo = element["first"]
            
            while nodo is not None:
                new = put(new, nodo["info"]["key"], nodo["info"]["value"])
                nodo = nodo["next"]

    my_map["capacity"] = new["capacity"]
    my_map["table"] = new["table"]
    my_map["current_factor"] = new["current_factor"]
    my_map["scale"] = new["scale"]
    my_map["shift"] = new["shift"]
    
    return my_map

               
def default_compare(key, element):

   if (key == me.get_key(element)):
      return 0
   elif (key > me.get_key(element)):
      return 1
   return -1