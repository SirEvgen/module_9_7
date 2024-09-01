def is_prime(func):
    def wrapper(*args):
        number = func(*args)
        k = 0
        for i in range(2, number // 2 + 1):
            if number % i == 0:
                k = k + 1
        if k <= 0 and number != 0:
            print("Простое")
        else:
            if number != 0:
                print("Составное")
            else:
                print('Ноль не является ни простым ни составным числом')
        return number
    return wrapper


@is_prime
def sum_three(*args):
    return sum(args)


result = sum_three(0, 0, 0)
print(result)
