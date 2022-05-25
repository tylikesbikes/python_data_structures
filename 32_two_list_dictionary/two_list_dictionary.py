def two_list_dictionary(keys, values):
    """Given keys and values, make dictionary of those.
    
        >>> two_list_dictionary(['x', 'y', 'z'], [9, 8, 7])
        {'x': 9, 'y': 8, 'z': 7}
        
    If there are fewer values than keys, remaining keys should have value
    of None:
    
        >>> two_list_dictionary(['a', 'b', 'c', 'd'], [1, 2, 3])
        {'a': 1, 'b': 2, 'c': 3, 'd': None}
    
    If there are fewer keys, ignore remaining values:

        >>> two_list_dictionary(['a', 'b', 'c'], [1, 2, 3, 4])
        {'a': 1, 'b': 2, 'c': 3}
   """
    d = {}

    key_count = len(keys)
    value_count = len(values)

    for i in range(key_count if key_count < value_count else value_count):   #this loop works when keys & values have the same legnth AND when len(keys) > len(values)
        d[keys[i]] = values[i]

    if key_count>value_count:   # this loop fills in the remaining values where values < keys
        for i in range(value_count,key_count):
            d[keys[i]]=None
    
    return d







