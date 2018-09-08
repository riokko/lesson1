def get_summ(one, two, delimeter='&'):
    return str.upper(one) + str(delimeter) + str.upper(two)

print(get_summ("learn","python"))