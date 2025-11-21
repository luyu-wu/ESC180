def is_sorted(list):
    inc, dec = True, True
    for i in range(len(list)-1):
        if list[i] > list[i+1]:
            inc = False
        if list[i] < list[i+1]:
            dec = False

    print( inc != dec )

is_sorted([1, 2, 3, 4, 5]) # True
is_sorted([4, 2, 1]) # True
is_sorted([5, 2, 10]) # False
is_sorted([1, 2, 2, 3]) # False
