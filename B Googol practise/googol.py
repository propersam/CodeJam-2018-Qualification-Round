import time

#start = time.time()

# while len(data) <= 1000000000000000000:  
def update_data(dat):
    if len(dat) == 0:
        return []
    reverse = dat
    for i in range(len(reverse)):# Change all 1s to 0s and all 0s to 1s
        if reverse[i] == 0: 
            print("0 to 1\n")
            reverse[i] = 1
        else:
            print("1 to 0\n")
            reverse[i] = 0
   # reverse = [0] + reverse[-1::-1] # Reversing String
    return reverse

def switch(file):
    return file[-1::-1]


T = int(input().strip())

for testCase in range(1,T+1):
    data = []
    length = 1
    pos = 0
    K = int(input().strip())
    while True:
        if K < length:
            pos = ((length - K) - 1) % len(data)
            break
        elif K == length:
            pos = (len(data) - 1) % len(data)
            break
        else:
            data = [0] + switch(update_data(data))
            print(data)
            length = (length * 2) + 1

#    print(data, length, K, sep=' ')
    print(f"Case #{testCase}: {data[pos]}")

# print('This program ran in', time.time() - start, 'seconds', sep=' ')
    
    