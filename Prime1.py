#this program will check a number is prime or not.
N = int(input(''))
for i in range(N):
    X = int(input(''))
    if X == 1:
        print(X, 'Not Prime')
    else:
        for i in range(2, X):
            if X % i == 0:
                print(X, 'Prime')
                break
        else:
            print(X, 'Prime')