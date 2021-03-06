import factorials
import prime

def recursive_mul(mylist, total=[]):
    """Multipis numbers in a list with it self"""
    if len(mylist) == 1:
        return total
    else:

        return recursive_add(
                mylist[1:], total + [mylist[0] * num for num in mylist[1:]])

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


def recursive_combs(sequence):
    #Finds all combinations of the prime factors to generate all proper factors
    results = {}
    for i in range(1, len(sequence) + 1):  # creates [] --> len(seq)*[]
        combs = combinations(sequence, i)
        for comb in combs:
            results[comb] = results.get(comb, 0) + 1  # only add uniqe results
    return results


def split_sequence(sequence, size):
    """Splits a sequence into pieces of given size"""
    results = {}
    i = 0
    # run until size becomes greater than size of sequence
    while i + size < len(sequence) + 1:
        split = sequence[i:i + size]#create split at i
        results[split] = results.get(split, 0) + 1
        i += 1#move one step to create next split
    return results


def prime_factors(num, prime_list):
    possible_primes = prime_list
    prime_factors = []
    temp = num
    if num == 0:#raise exception?
        return []
    if num == 1:
        return ['1']
    if num in possible_primes:
        return ['1', str(num)]#need to be strings?
    #Keep dividing by primes until the result is two primes
    while temp != 1 and temp != 0:
        for prime in possible_primes:
            if temp % prime == 0:
                prime_factors.append(str(prime))
                temp = temp / prime
                break#if you find a prime stop and start loop again
    return prime_factors

def factors_comb(num, prime_list):
    #factoring using reursive combinations from python
    prime_facts = prime_factors(num, prime_list)
    results = {1:1,num:1}#add 1 and number for final list display
    for i in range(1,len(prime_facts)):
        possible_combs = combinations(prime_facts, i)
        for comb in possible_combs:
            #first find value of perm to add only unique values
            temp = eval("*".join([str(num) for num in comb]))
            results[temp] = results.get(temp, 0) + 1
    return sorted(results.keys()), prime_facts
        
def factors(num, prime_list):
    #factoring using different recursive method to find combinations
    all_perms = recursive_perms(prime_factors(num, prime_list))
    factors = {1:1}
    for perm in all_perms.keys():
        possible_combs = recursive_combs(perm)
        for comb in possible_combs.keys():
            factor = eval("*".join([str(num) for num in comb]))
            factors[factor] = factors.get(factor, 0) + 1
    return sorted(factors.keys())


def main():
    p = prime.Prime()
    prime_list = p.gen_prime_list()
    a= factors(10539, prime_list)
    print a


if __name__ == '__main__':
    main()
