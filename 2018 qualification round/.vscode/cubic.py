
# Main Part of program
t = int(input()) # num of test cases
for _ in range(1, t+1):
    A, pos = input().split('.')
    A = float(A) # The desired area of the shadow
    pos = int(pos) # The positional rotations

    print("Case #{}".format(_))
    