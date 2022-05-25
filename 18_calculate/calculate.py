def calculate(operation, a, b, make_int=False, message='The result is'):
    """Perform operation on a + b, ()possibly truncating) & returning w/msg.

    - operation: 'add', 'subtract', 'multiply', or 'divide'
    - a and b: values to operate on
    - make_int: (optional, defaults to False) if True, truncates to integer
    - message: (optional) message to use (if not provided, use 'The result is')

    Performs math operation (truncating if make_int), then returns as
    "[message] [result]"

        >>> calculate('add', 2.5, 4)
        'The result is 6.5'

        >>> calculate('subtract', 4, 1.5, make_int=True)
        'The result is 2'

        >>> calculate('multiply', 1.5, 2)
        'The result is 3.0'

        >>> calculate('divide', 10, 4, message='I got')
        'I got 2.5'

    If a valid operation isn't provided, return None.

        >>> calculate('foo', 2, 3)
        
    """
    def add(a,b):
        return a+b

    def subtract(a,b):
        return a-b
    
    def multiply(a,b):
        return a*b
    def divide(a,b):
        return a/b

    d = {'add':add,
    'subtract':subtract,
    'multiply':multiply,
    'divide':divide}

    if d.get(operation,None) == None:
        return None

    if make_int:
        return f"{message} {str(int(d[operation](a,b)))}"

    return f"{message} {str(d[operation](a,b))}"







