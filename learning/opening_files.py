file_ = open("employ.txt", 'r')
for employee in (file_.readlines()):
    print(employee)

file_.close()