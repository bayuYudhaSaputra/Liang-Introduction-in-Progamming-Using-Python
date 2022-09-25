# Return the gcd of two integers
def gcd(n1, n2):
    gcd = 1 # initial gcd is 1
    k = 2 # possible gcd

    while k <= n1 and k <= n2:
        if n1 % k == 0 and n2 % k == 0:
            gcd = k # update gcd
        k += 1
    return gcd # return gcd