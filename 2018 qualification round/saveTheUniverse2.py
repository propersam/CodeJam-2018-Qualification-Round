def alienDamage(program):
    damageRate = 1
    damage = 0
    for c in program:
        if c == 'S':
            damage += damageRate
        else:
            damageRate *= 2
    return damage

def altar(d, p):
    count = 0
    while True:
        damage = alienDamage(p)
        if damage <= d:
            break
        if 'CS' in p:
            p = p.replace('CS', 'SC', 1)
            count += 1
        else:
            return 'IMPOSSIBLE'
    
    return count


T = int(input())
for t in range(1, T+1):
    D, P = input().split()
    print("Case #{}: {}".format(t, altar(int(D), P)))        


