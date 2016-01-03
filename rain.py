
import heapq

def rain(l):
    if len(l) <= 2:
        return 0
    biggest_two = heapq.nlargest(2, l)
    ans = []

    if l[0] in biggest_two and l[-1] in biggest_two:
    # if set(biggest_two) == set([l[0], l[-1]]):
        ans = [(biggest_two[1] - l[i]) for i in range(1,len(l)-1)]
        return sum(ans)
    else:
        new_l = l[1:-1]
        seperate = new_l.index(max(new_l)) + 1
        left = l[ : seperate + 1]
        right = l[seperate : ]
        return rain(left) + rain(right)


print rain([]) #0
print rain([4,3,2,1,5]) #6
print rain([3,5,2,1,1,3,2,4,3,2,4]) #14
print rain([3,4,5,2,1,4,2,1,2,3]) #9
print rain([1,1,2,3,4,3,2,1,1]) #0
print rain([3,1,4,2,2,5,2,1,2,3]) #10
print rain([1,4,1,5,3,3,4,3,4,2,5,2,3]) #15
