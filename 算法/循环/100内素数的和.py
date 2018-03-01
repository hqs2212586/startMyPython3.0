sum_prime = 0
for i in range(2,101):
    n = 0
    for j in range(2,i-1):
        if i % j == 0:
            n = 1
            break
    if n == 0:
        sum_prime += i
print(sum_prime)