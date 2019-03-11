
#import time

def city_counter(data, elem):
    if len(data) < 3:
        start, stop = data
        if elem in range(start, stop+1):
            return 1
        else:
            return 0    
    start,stop = data[:2]
    if elem in range(start, stop+1):
        return 1 + city_counter(data[2:], elem)
    else:
        return 0 + city_counter(data[2:], elem)
    
#start = time.time()
T = int(input().strip())

for i in range(1, T + 1):
    
    N = int(input().strip())
    data = [int(j) for j in input().strip().split(" ")]
    n_check = int(input().strip())
    answers = []
    for k in range(n_check):
        city = int(input().strip())
        answers.append(city_counter(data, city))

    print(f"Case #{i}:",end=' ')
    for ansa in answers:
        print(ansa, end=' ')
    print()
    input().strip()
        
#diff = time.time() - start 
#print(diff)