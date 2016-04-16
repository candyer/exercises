#problem A  The Last Word

#Solution one, O(n^2)
def solve(s):
    res = s[0]
    for c in s[1:]:
        if c >= res[0]:
            res = c + res
        else:
            res = res + c
    return res

#Solution two, O(n)
def solve(s):
    left, right = [s[0]], []
    for c in s[1:]:
        if c >= left[-1]:
            left.append(c)
        else:
            right.append(c)
    return ''.join(list(reversed(left)) + right)

def a():
    T = int(raw_input())
    for t in range(1,T+1):
        S = raw_input()
        print "Case #{}:".format(t), solve(S)

if __name__ == '__main__':
    a()


######################################################################################################################################
#Problem B. Rank and File

# solution one  
def solve(l):
    new_l = [s for sub in l for s in sub ]
    d = {}
    for n in new_l:
        d[n] = d.get(n,0)+1
    res = [k for k,v in d.items() if v%2 != 0]
    return " ".join(map(str, sorted(res)))


# solution two 
import collections
def solve(pieces):
    count= collections.defaultdict(lambda: 0)
    for piece in pieces:
        for num in piece:
           count[num] += 1
    res = [k for k,v in count.items() if v%2]
    return ' '.join(map(str,sorted(res)))


def b():
    T = int(raw_input())
    for t in range(1,T+1):
        N = int(raw_input())
        p = []
        for n in range(2*N-1):
            positions = map(int,raw_input().split())
            p.append(positions)
        print "Case #{}:".format(t), solve(p)

if __name__ == '__main__':
    b()
