def dict_intersection(dict1, dict2):
    result = {}
    for key in dict1:
        if key in dict2 and dict1[key] == dict2[key]:
            result[key] = dict1[key]
    return result

dict1 = {"a": 1, "b": 2, "c": 3}
dict2 = {"b": 2, "c": 4, "d": 5}
print("Intersection:", dict_intersection(dict1, dict2))