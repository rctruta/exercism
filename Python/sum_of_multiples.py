def sum_of_multiples(limit, factors):
    if limit == 0 or len(factors) == 0:
        return 0
    if 0 in factors:
        factors_remove_0 = factors.remove(0)    
    return sum(set((i*factor for factor in factors for i in range(1, limit//factor + 1) if i*factor < limit)))
