def split(n):
    return n // 10, n % 10

def luhn_sum(n):
    ''' Calculate the luhn_sum for the odd-position digits'''
    assert n > 0 and type(n) == int, "N must be a positve integer."
    
    if n < 10:
        return n
    all_but_last, last = split(n)
    return luhn_double_sum(all_but_last) + last

def luhn_double_sum(n):
    ''' Calculate the luhn_sum for the even-position digits'''

    all_but_last, last = split(n)
    double_sum = last * 2
    double_sum = double_sum // 10 + double_sum % 10
    if n < 10:
        return double_sum
    else:
        return luhn_sum(all_but_last) + double_sum

def valid_number_counter(num_digits = 16):
    i, count = 10 ** (num_digits - 1), 0
    limit = i * 10
    while i < limit:
        if luhn_sum(i) % 10 == 0:
            print(i)
            count += 1
        i += 1
    return count
