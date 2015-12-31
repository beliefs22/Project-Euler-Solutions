import prime
import time

def recursive_perms(sequence):
    """Finds all possible combinationrs of a sequence"""
    if len(sequence) == 0:
        raise Exception("list must be > 0")
    if len(sequence) == 1:
        return {tuple(sequence): 1}

    # get all permutations of length N-1
    all_perms = recursive_perms(sequence[1:])
    insert = [sequence[0]]
    result = {}
    for perm in all_perms.keys():
        perm = list(perm)#convert from tuples to list slow performance?
        for i in range(len(perm) + 1):
            permutation = tuple(perm[:i] + insert + perm[i:])
            result[permutation] = result.get(permutation, 0) + 1
    return result

def combinations(iterable, r):
    #modified to only return unique combinations
    # combinations('ABCD', 2) --> AB AC AD BC BD CD
    # combinations(range(4), 3) --> 012 013 023 123
    pool = tuple(iterable)
    n = len(pool)
    if r > n:
        return
    indices = range(r)

    yield tuple(pool[i] for i in indices)#yeild helps performance?

    while True:
        for i in reversed(range(r)):
            if indices[i] != i + n - r:
                break
        else:
            return
        indices[i] += 1
        for j in range(i+1, r):
            indices[j] = indices[j-1] + 1

        yield tuple(pool[i] for i in indices)


def prime_factors(num, Prime):
    prime_factors = []
    temp = num
    if num == 0:#raise exception?
        return []
    if num == 1:
        return [1]
    if Prime.is_prime(num) :
        return [1, num]#need to be strings?
    #Keep dividing by primes until the result is two primes
    while temp != 1 and temp != 0:
        for prime in iter(Prime):
            if temp % prime == 0:
                prime_factors.append(prime)
                temp = temp / prime
                break#if you find a prime stop and start loop again
    return prime_factors

def factor(num, prime_list, withprime=False):
    #factoring using reursive combinations from python
    prime_facts = prime_factors(num, prime_list)
    results = {1:1,num:1}#add 1 and number for final list display
    for i in range(1,len(prime_facts)):
        all_factors = combinations(prime_facts, i)#b =[eval("*".join([str(num) for num in generator])) for generator in c]
        for comb in possible_combs:
            #first find value of perm to add only unique values
            temp = eval("*".join([str(num) for num in comb]))
            results[temp] = results.get(temp, 0) + 1
    if withprime:
        return results.keys()
    else:
        return results.keys()
        


def main():
    p = prime.Prime()
    for i in xrange(1,10):
        a = factor(i, p)
        print a, "factors are"
        for i in range(1,len(a)+1):
            for comb in combinations(a,i):
                print comb

if __name__ == '__main__':
    start = time.time()
    main()
    end = time.time()
    print "took %f seconds to run 1,10000" % (end-start)
