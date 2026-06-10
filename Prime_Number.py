

# ================== start =====================

def is_prime(n):
    prime = True
    if n > 1:
        for i in range(2, n):
            if n % i == 0:
                prime = False
                break
            else:
                prime = False

    return prime


print(is_prime(7))
