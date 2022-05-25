def multiple_letter_count(phrase):
    """Return dict of {ltr: frequency} from phrase.

        >>> multiple_letter_count('yay')
        {'y': 2, 'a': 1}

        >>> multiple_letter_count('Yay')
        {'Y': 1, 'a': 1, 'y': 1}
    """
    dict_counts = {}

    for ltr in phrase:
        
        if ltr not in dict.keys():
            dict[ltr]=1
        else:
            dict[ltr]+=1