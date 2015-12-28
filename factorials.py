import prime
import math
import brutefactor
import recursivelist
import time

def all_divisors(num, Prime, longval=None):
    """Finds divisors of a given number using Primes.

    Args:
        num (int): number to find divisors of
        Prime (Prime): Prime object used to generate primes for functions
        longval (bool): tells function that the value is too large to use
            available primes, switches to brute force method

    Returns:
        list: contains divisors for given number

    """
    #start = time.time()
    if Prime.is_prime(num) or num == 0:
        return [1,num] # , 0, 0
    found_primes = [1]
    prime_factors = []
    all_factors = []
    maxval = math.sqrt(num)
    if longval:
        possible_divisors = Prime.prime_generator_count()  #for large values
    else:
        possible_divisors = Prime.prime_generator_value(maxval)
    for prime in possible_divisors:
        if num % prime == 0:
            temp = num #place holder for number since we will modify it
            result = num / prime #find non prime match for prime factor
            count = 0
            prime_factors.append(prime)
            found_primes.append(prime)
            if result not in all_factors:
                all_factors.append(result)
                
            while temp % prime == 0:
                result = temp / prime  #place holder for matched non prime
                multiple = prime**count #how many times does prime go in
                if multiple not in all_factors:
                    all_factors.append(multiple)
                if result not in all_factors and result != 0:
                    all_factors.append(result)
                temp = result
                count += 1

    all_factors.append(num)
    #end = time.time()
    #first = end - start
    #start1 = time.time()
    missed_primes = [a*b for a in found_primes for b in found_primes]
    for item in missed_primes:
        if num % item == 0 and item not in all_factors:
            all_factors.append(item)


    for factor in all_factors[:]:

        result = num / factor
        if result not in all_factors:
            all_factors.append(result)
    #end1 = time.time()
    #second = end1 - start1

    return sorted(all_factors) # , first, second

def prime_factors(num, primes):
    #print "number is", num
    setup_start = time.time()
    possible_primes = primes
    prime_factors = []
    done = False
    temp = num
    if num == 0:
        return []
    if num == 1:
        return [1]
    if num in possible_primes:
        return [1,num]
    setup_end = time.time()
    #print "took %f seconds to set up" % (setup_end - setup_start)
    find_prime_start = time.time()
    while  temp != 1 and temp != 0:        
        for prime in possible_primes:
            ##print temp,prime ,"temp is prime is"
            if temp % prime == 0:
                prime_factors.append(prime)
                temp = temp/prime
                break
            if prime == possible_primes[len(possible_primes)-1]:
                return brutefactor.brutefactor(num)
    find_prime_end = time.time()
    #print "prime factors are", prime_factors
    #print "took %f seconds to find initial primes" \
          #% (find_prime_end - find_prime_start)
    recursive_start = time.time()
    all_factors = recursivelist.recursive_add(prime_factors)
    recursive_end = time.time()
    #print "took %f seconds to find recursive factors" \
         # % (recursive_end - recursive_start)
    append_start = time.time()
    append_to_all_factors = all_factors.append
    for prime in prime_factors:
        append_to_all_factors(prime)
    final_factors = [num /factor for factor in all_factors]
    for item in final_factors:
        append_to_all_factors(item)
    append_end = time.time()
    #print "took %f seconds to append" % (append_end - append_start)
  
    return sorted(list(set(all_factors)))
    
def factor(num, primes):
    """Finds diviors of a given number, switches methods if number is too large.

    Args:
        num (int): number to find divisors
        primes (Prime): Prime object used to generate primes for function

    Returns:
        list: contains divisors of given number

    """
    try:
        divisors = all_divisors(num,primes) 
        return divisors
    except IndexError:  #switches to brute force if number is > 
        divisors = all_divisors(num,primes,longval=True)
        largest_div = divisors[len(divisors)-1]
        i = largest_div
        while i < num/2 :
            if num % i == 0:
                divisors.append(i)
            i += 1
        return divisors
 
def main():
    #start = time.time()
    primes = prime.Prime()
    prime_list = primes.gen_prime_list()
    #total_first = 0
    #total_second = 0
    number = 1000
    for i in range(1000,1001):
        using_primes = factor(i,primes)
        ##print using_primes, len(using_primes), i, "primes"
        #print "calling using primes with", i
        using_only_primes = prime_factors(i, prime_list)
        print using_only_primes, len(using_only_primes), i, "onlyprimes"
    #    total_first += first
    #    total_second += second
        
    #end = time.time()
    #print "took %f seconds to 1st part, %f seconds %f average to run second part" \
    #      % (total_first,total_second, total_second/(10000.00-1000.00))
    #print "took", end - start, " seconds to run"

if __name__ == '__main__':
    main()
    
