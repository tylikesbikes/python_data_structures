def reverse_vowels(s):

    """Reverse vowels in a string.

    Characters which re not vowels do not change position in string, but all
    vowels (y is not a vowel), should reverse their order.

    >>> reverse_vowels("Hello!")
    'Holle!'

    >>> reverse_vowels("Tomatoes")
    'Temotaos'

    >>> reverse_vowels("Reverse Vowels In A String")
    'RivArsI Vewols en e Streng'

    reverse_vowels("aeiou")
    'uoiea'

    reverse_vowels("why try, shy fly?")
    'why try, shy fly?''
    """

    vowels=[]

    s_list = list(s)

    for i in range(len(s)):
        if s[i] in ('AEIOUaeiou'):
            vowels.append(i)

    rev_vowels = vowels[::-1]

    for x in range(len(vowels)//2):
        s_list[vowels[x]],s_list[rev_vowels[x]] = s_list[rev_vowels[x]],s_list[vowels[x]]    

    return ''.join(s_list)
    


    

