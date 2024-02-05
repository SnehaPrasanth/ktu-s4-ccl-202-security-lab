n = int(input("Enter a number: "))

if n > 1:
    prime_flag = True
    for i in range(2, int(n/2) + 1):
        if (n % i) == 0:
            prime_flag = False
            break
    if prime_flag:
        print("Prime")
    else:
        print("Not prime")
elif n == 1 or n == 0:
    print("Neither prime nor composite")
else:
    print("Enter a number greater than 1")
