print(2**3)
#line 3 - 6 is a really short way of writing exponents.
 ##def raise_to_power(base_num, pow_num):
     ##return base_num ** pow_num

  ##print(raise_to_power(2, 3))

def raise_to_power(base_num, pow_num):
    result = 1
    for index in range(pow_num):
        result = result * base_num
    return result


print(raise_to_power(3,3))
