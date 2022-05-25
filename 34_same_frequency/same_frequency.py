def same_frequency(num1, num2):
    """Do these nums have same frequencies of digits?
    
        >>> same_frequency(551122, 221515)
        True
        
        >>> same_frequency(321142, 3212215)
        False
        
        >>> same_frequency(1212, 2211)
        True
    """
    dict1 = {}
    dict2 = {}

    s1 = str(num1)
    s2 = str(num2)

    for n in s1:
        dict1[n]=s1.count(n)

    for n in s2:
        dict2[n]=s2.count(n)

    return dict1 == dict2

