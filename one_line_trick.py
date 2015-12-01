def shortest(solutions):
    """return the shortest solution"""
    
    #way 1
    if solutions == []:
        return []
    shortest_path = solutions[0]
    shortest_len = len(solutions[0])
    for solution in solutions:
        if len(solution) < shortest_len:
            shortest_len = len(solution)
            shortest_path = solution
    return shortest_path

    #way 2
    return min(solutions, key=len)

# print shortest([[1,2,3],[5,2],[7,8,5,0]]) #[5, 2]



def longest(solutions):
    """return the longest path"""
    
    #way 1
    if len(solutions) == 0:
        return []
    longest_path = solutions[0]
    longest_len = len(solutions[0])
    for n in solutions:
        if len(n) > longest_len:
            longest_len = len(n)
            longest_path = n
    return longest_path

    #way 1
    return max(solutions, key=len)


# print longest([[1,2,3],[5,2],[7,8,5,0]]) #[7, 8, 5, 0]



def greatest_sum(l):
    """return the sublist with greatest sum, three ways to do it"""
    
    #way 1
    if len(l) == 0:
        return 0
    sum_of_each = []
    for m in l:
        sum_of_each.append(sum(m))
    for n in l:
        if sum(n) == max(sum_of_each):
            return n

    #way 2
    if len(l) == 0:
        return 0
    biggest_list = l[0]
    biggest_sum = sum(l[0])
    for m in l:
        if sum(m) > biggest_sum:
            biggest_sum = sum(m)
            biggest_list = m
    return biggest_list


    #way 3
    return max(l, key=sum)

# print greatest_sum([[1,2,3,4],[5,7],[3,4,55],[6,7,21]]) #[3, 4, 55]



def return_even(seq):
    '''
    create a function that takes a list of lists
    return another list of lists which contain only even numbers
    '''
    
    #way 1
    even = []
    for sublist in seq:
        a = []
        for s in sublist:
            a.append(s % 2 == 0)
        if all(a):
            even.append(sublist)
    return even

    #way 2
    return [sublist for sublist in seq if all(s%2==0 for s in sublist)]

# print return_even([[1,2,3],[7],[8],[2,4,6],[4],[3]]) #[[8],[2, 4, 6],[4]]
