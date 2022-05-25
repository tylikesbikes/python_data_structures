def mode(nums):
    """Return most-common number in list.

    For this function, there will always be a single-most-common value;
    you do not need to worry about handling cases where more than one item
    occurs the same number of times.

        >>> mode([1, 2, 1])
        1

        >>> mode([2, 2, 3, 3, 2])
        2
    """
    dic = {}

    for num in nums:
        if num in dic.keys():
            dic[num]+=1
        else:
            dic[num]=1

    max_val=0
    max_key=0


    for (k,v) in dic.items():
        if v> max_val:
            max_val = v
            max_key = k

    return max_key


