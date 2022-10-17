def string_or_not(param):
    result = ((isinstance(param, str)==True) and 'yes' or 'no')
    print(result)
    return result
string_or_not('10')
