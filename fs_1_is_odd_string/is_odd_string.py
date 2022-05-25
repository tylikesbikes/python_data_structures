def is_odd_string(word):
    """Is the sum of the character-positions odd?

    Word is a simple word of uppercase/lowercase letters without punctuation.

    For each character, find it's "character position" ("a"=1, "b"=2, etc).
    Return True/False, depending on whether sum of those numbers is odd.

    For example, these sum to 1, which is odd:
    
        >>> is_odd_string('a')
        True

        >>> is_odd_string('A')
        True

    These sum to 4, which is not odd:
    
        >>> is_odd_string('aaaa')
        False

        >>> is_odd_string('AAaa')
        False

    Longer example:
    
        >>> is_odd_string('amazing')
        True
    """

    def chr_position(chr):
        if ord(chr) in range(65,91):
            return ord(chr)-64
        elif ord(chr) in range(97,123):
            return ord(chr)-96
    
    # sum_total = 0

    # for ltr in word:
    #     sum_total+=chr_position(ltr)

    # return sum_total %2 == 1

    return sum([chr_position(ltr) for ltr in word]) %2 == 1




    # Hint: you may find the ord() function useful here