def flip_case(phrase, to_swap):
    """Flip [to_swap] case each time it appears in phrase.

        >>> flip_case('Aaaahhh', 'a')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'A')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'h')
        'AaaaHHH'
    """

    list_phrase = list(phrase)

    def swap_case(letter):
        if ord(letter) in range(ord('a'),ord('z')+1):
            return letter.upper()
        return letter.lower()

    out_string = ''
    
    for ltr in list_phrase:
        if ltr.lower() == to_swap.lower():
            out_string+=swap_case(ltr)
        else:
            out_string+=ltr
    
    return out_string