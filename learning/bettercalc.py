def calc(num1, op, num2):
    if op == '+':
        return num1 + num2
    elif op == '-':
        return num1 - num2
    elif op == '*':
        return num1 * num2
    elif op == '/':
        return num1 / num2
    else:
        print("enter a valid number")
        return
quest = input("enter the question")

lis = quest.split(" ")
nu1 = int(lis[0])
op = lis[1]
nu2 = int(lis[2])

answer = calc(nu1, op, nu2)
print(answer)