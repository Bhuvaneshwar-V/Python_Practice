## Given two integer numbers, return their product only if the product is equal to or lower than 1000. Otherwise, return their sum.

def larger(a,b):
    mult = a * b
    if mult <= 1000:
        result = "The result is " + str(mult)
        return result

    else:
        add = a + b
        result = "The result is " + str(add)
        return result


larger(20,30)


