import sys
def action(a, b):
    Q = (a + b)//2
    print(Q)
    sys.stdout.flush()
    
    reply = input()
    if reply == 'TOO_SMALL':
        a = Q
    elif reply == 'TOO_BIG':
        b = Q
    elif reply == 'CORRECT':
        return True
    else:
        return False
    action(a,b)

T = int(input())# number of test cases

for i in range(T):
    A, B = map(int, input().split())
    i = int(input()) # reading interaction (N) from judge system
    action(A + 1, B)

    
    
        
