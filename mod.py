from random import randint

def random_with_N_digits(n):
    range_start = 10**(n-1)
    range_end = (10**n)-1
    return randint(3*range_start, 4*range_start)

def count_digits_in_number(num):
    print("Number : ", num)
    count = 0
    while num != 0:
        num //= 10
        count += 1

    print("Number of digits: " + str(count))

# print(random_with_N_digits(2))
# print(random_with_N_digits(32))

# count_digits_in_number(random_with_N_digits(32))


def get_modulo_one_num(digits, modulo):
    range_start = 10**(digits-1)
    num = random_with_N_digits(digits)
    rem = num % modulo
    print(f"{num} % {modulo} = {rem}")
    op = num+(modulo-rem)+1
    if op >= 4*range_start:
        op = num - rem+1
    rem_op = op % modulo
    print(f"{op} % {modulo} = {rem_op}")
    count_digits_in_number(op)
    print("{:,}".format(op))
    return op

get_modulo_one_num(32, 97)


