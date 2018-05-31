def powerset(set,m):
    all=[[]]
    for x in set:
        all.extend([subset+[x] for subset in all])
        #difference between extend and append
        result=[subset for subset in all if len(subset)==m]
    return result
