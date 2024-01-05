def palindrome(number):
    i = 0
    num = str(number)
    for index in range(len(num)):
        i += 1
        if num[index] != num[-i]:
            return False
    return True
print(palindrome(101))