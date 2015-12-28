import factorials
import prime
def recursive_add(mylist, total = []):

    if len(mylist) == 1:
        return total
    else:
        
        return recursive_add(
            mylist[1:], total + [mylist[0]*num for num in  mylist[1:]])

def recursive_perms(sequence):
    if len(sequence) == 0:
        raise Exception("list must be > 0")
    if len(sequence) == 1:
        return {tuple(sequence):1}

    #get all permutations of length N-1
    all_perms = recursive_perms(sequence[1:])
    insert = [sequence[0]]
    result = {}
    for perm in all_perms.keys():
        perm = list(perm)
        for i in range(len(perm) + 1):
            permutation = perm[:i] + insert + perm[i:]
            result[tuple(permutation)] = result.get(tuple(permutation),0) + 1
    return result
def recursive_combs(sequence):
    #expects list?
    results = {}
    for i in range(1,len(sequence)+1): # creates [] --> len(seq)*[]
        combs = split_sequence(sequence,i)
        for comb in combs:
            results[comb] = results.get(comb, 0) + 1 #only add uniqe results
    return results

def split_sequence(sequence,size):
    """Creates max number olist of specified size from sequence in given order.

    """
    results = {}
    i = 0
    #run until size becomes greater than size of sequence
    while i + size < len(sequence)+1: 
        split = sequence[i:i+size]
        results[split] = results.get(split,0) + 1
        i += 1
    return results
    
def prime_factors(num, prime_list):
    possible_primes = prime_list
    prime_factors = [1]
    done = False
    temp = num
    if num == 0:
        return []
    if num == 1:
        return ['1']
    if num in possible_primes:
        return ['1',str(num)]
    while  temp != 1 and temp != 0:        
        for prime in possible_primes:
            if temp % prime == 0:
                prime_factors.append(str(prime))
                temp = temp/prime
                break
    return prime_factors

def factors(num,prime_list):
    all_perms = recursive_perms(prime_factors(num,prime_list))
    factors = {}
    for perm in all_perms.keys():
        possible_combs = recursive_combs(perm)
        for comb in possible_combs.keys():
            factor = eval("*".join([str(num) for num in comb]))
            factors[factor] = factors.get(factor, 0) +1
    return sorted(factors.keys())
def main():
    number = 150000000
    p = prime.Prime()
    prime_list = p.gen_prime_list()
    for i in xrange(1,10000):
        result = sum(xrange(1, i+1))
        a = prime_factors(result, prime_list)
        if len(set(a)) > 6:
            b = factors(result,prime_list)
            print "checking factors" , i
            if len(b) > 300:
                print i, "found one"
    print "done"
        


if __name__=='__main__':
    main()
        
