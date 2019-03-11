# python googol solution tinz
def switch(raw):
    processed = []
    for i in raw:
        if i == '1':
            processed.append('0')
        else:
            processed.append('1')
    return ''.join(processed)

def main():


    T = int(input().strip())

    for i in range(1, T+1):
        data = ''
        K = int(input().strip())
        while len(data) < K:
            new = switch(data) # switching 1s and 0s
            new = new[-1::-1] # REversing string
            data = ''.join([data, '0' ,new])# Joining final details into string form
        print(data)




if __name__=='__main__':
    main()