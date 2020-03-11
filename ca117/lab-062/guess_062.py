from random import randint

top = 1000000
bottom = 0
z = randint(bottom, top)

def guess(g):
    if g == z:
        return 0
    elif g < z:
        return -1
    else:
        return 1

# Find z *efficiently* by calling guess() (and without peeking at z!)
def find():
    top_func = top
    bottom_func = bottom
    while top_func > bottom_func:
        mid = (top_func + bottom_func) // 2
        result = guess(mid)
        if result == -1:  # mid is less than z, set bottom to mid
            bottom_func = mid
        elif result == 1:  # mid is greater than z, set top to mid
            top_func = mid
        else:
            return mid

def main():
    a = find()
    if a == z:
        print('Correct!')
    else:
        print('Incorrect!')
    print('You said {:d} and answer is {:d}'.format(a, z))

if __name__ == '__main__':
    main()
