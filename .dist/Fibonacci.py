def fibo(number):
    a = 0 
    b = 1
    result = []
    for i in range(number):
        result.append(a)
        temp = a # temporary 
        a = b
        b = a + b 
    return result

print(fibo(10))