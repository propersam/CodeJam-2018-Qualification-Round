import sys

def troubleSort(l):
    done = False
    while not done:
        done = True
        for i in range(len(l) - 2):
            if l[i] > l[i+2]:
                done = False
                # reversing the range of values
                #for j in range(i+2, i-1, -1):
                temp = l[i]
                l[i] = l[i+2]
                l[i+2] = temp

    return l

def validate(list):
    sorted_l = troubleSort(list)
    for i in range(len(list)-1):
        if sorted_l[i] > sorted_l[i+1]:
            return i

    return 'OK'    
    

T = int(input())
for t in range(1, T+1):
    N = int(input()) # length of the List
    L = sys.stdin.readline().split()
    sys.stdin.flush()
    print("Case #{}: {}".format(t, validate(L)))
