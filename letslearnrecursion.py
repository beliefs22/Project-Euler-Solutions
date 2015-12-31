def combinations(iterable, r):
    # combinations('ABCD', 2) --> AB AC AD BC BD CD
    # combinations(range(4), 3) --> 012 013 023 123
    pool = tuple(iterable)
    n = len(pool)
    if r > n:
        return
    indices = range(r)
    found = []
    comb = tuple(pool[i] for i in indices)
    if comb not in found:
        found.append(comb)
        yield comb
    while True:
        for i in reversed(range(r)):
            if indices[i] != i + n - r:
                break
        else:
            return
        indices[i] += 1
        for j in range(i+1, r):
            indices[j] = indices[j-1] + 1
        comb = tuple(pool[i] for i in indices)
        if comb not in found:
            found.append(comb)
            yield comb
            
def main():
    iterable = '123345'
    combs = combinations(iterable, 2)
    for comb in combs:
        print comb


if __name__=='__main__':
    main()
