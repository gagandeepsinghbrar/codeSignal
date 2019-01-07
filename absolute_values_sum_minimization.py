def absolute_values_sum_minimization(a):
    i = int(len(a) / 2)
    if i % 2 == 0 or len(a) == 2:
        return a[i - 1]
    return a[i]