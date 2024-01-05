def power(base_num, pow_num):
    result = 1
    for index in range(pow_num):
        result *= base_num
    return result
print(power(3,4))