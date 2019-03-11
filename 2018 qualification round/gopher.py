import sys

def prepare(a):
   # r = c = 10
    i = 10
    j = 10
    for _ in range(1000):
            
        print(i, j)
        sys.stdout.flush()
        x, y = map(int, input().split())
        if x == 0 and y == 0:
            return True
        elif x == -1 and y == -1:
            return False
        else:
            i = (abs(x - i) + 10) % 1000 
            j = (abs(y - j) + 10) % 1000 
            x, y = map(int, input().split())
    return False
        
    

#        _ = input() # reading interaction (1000)

t = int(input())
for _ in range(t):
    a = input() # min required prepared rectangle area
#     _ = input() # reading interaction (1000)

    if not prepare(a):
        break
    