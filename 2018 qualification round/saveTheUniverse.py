def alienDamage(program):
    if type(program) == 'list':
        program = ''.join(program)
    damageRate = 1
    damage = 0
    for c in program:
        if c == 'S':
            damage += damageRate
        else:
            damageRate *= 2

    return damage


def modify(D, P):
    #P = P.split()
    numOfSwitch = 0
    i = 0
    j = 1
    
    while True:      
        r_damage = alienDamage(P)
        if r_damage <= D:
            break  
        
        if P[i] == 'C' and P[j] == 'S':
            P = P.replace('CS', 'SC', 1)
            numOfSwitch += 1
        elif P[i] == P[j]:
            if len(P) <= 3:
                return 'IMPOSSIBLE'
            elif P[i + 1 % (len(P) - 1)] == P[j+1%(len(P) - 2)] and alienDamage(P) > D:
                return 'IMPOSSIBLE'
            else:
                i += 1 % (len(P) - 1)
                j += 1 % (len(P) - 2)
                continue
        else:
            i += 1 % (len(P) - 1)
            j += 1 % (len(P) - 2)
            continue


    return numOfSwitch
#print(alienDamage('SSSCC'))

# Main part of the program
T = int(input())
for t in range(1, T+1):
    D, P = tuple(input().split())
#   print(D, P)
    print("Case #{}: {}".format(t, modify(int(D), P)), flush=True)
        
csscsc