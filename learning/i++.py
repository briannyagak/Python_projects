def palindrome(number):
    num_str = str(number)
    length = len(num_str)

    for index in range(length // 2):
        if num_str[index] != num_str[length - index - 1]:
            return False

    return True

print(palindrome(54433235))