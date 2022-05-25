def valid_parentheses(parens):
    """Are the parentheses validly balanced?

        >>> valid_parentheses("()")
        True

        >>> valid_parentheses("()()")
        True

        >>> valid_parentheses("(()())")
        True

        >>> valid_parentheses(")()")
        False

        >>> valid_parentheses("())")
        False

        >>> valid_parentheses("((())")
        False

        >>> valid_parentheses(")()(")
        False
    """

    while True:
        loc = parens.find('()')
        if loc == -1:
            return False
        
        parens = parens[:loc]+parens[loc+2:]
        if len(parens) == 0:
            return True

        
        
        