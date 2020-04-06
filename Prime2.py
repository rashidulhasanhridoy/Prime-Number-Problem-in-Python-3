#This program will show first 1500 prime number.
def prime(X):
    if X == 1:
        return 0
    else:
        for i in range(2, X):
            if X % i == 0:
                return 0
                break
        else:
            return 1
P = []
count = 0
i = 1
while True:
    Y = prime(i)
    if Y == 1:
        P.append(i)
        count += 1
    i += 1
    if count == 1500:
        # Here you can change the total number of prime,
        # you want to see. 1500 means this program will shom first 1500 prime numbers.
        break
print(P)