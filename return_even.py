def return_even(seq):
    '''
    create a function that takes a list of lists
    return another list of lists which contain only even numbers
    '''
    even = []
    for sublist in seq:
        if all(s % 2 == 0 for s in sublist):
            even.append(sublist)
    return even

print return_even([[1,2,3],[7],[8],[2,4,6],[4],[3]])  # [[8], [2, 4, 6], [4]]
