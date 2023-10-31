numbers_x = [10, 20, 30, 40, 10]
numbers_y = [75, 65, 35, 75, 30]

def if_same(numberlist):
    print("Given list:", numberlist)
    first_num = numberlist[0]
    second_num = numberlist[-1]
    if first_num == second_num:
        return True
    else:
        return False


print("result is", if_same(numbers_x))
print("result is", if_same(numbers_y))