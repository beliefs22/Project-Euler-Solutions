import prime
import factorials
import brutefactor
import time

def triangle_sums_prime(n, primes):   

    return factorials.factor(sum(xrange(1, n+1)), primes)

def triangle_sums_brute(n):

    return brutefactor.brutefactor(sum(xrange(1, n+1)))

def triangle_sums_only_primes(n, prime_list):
    
    return factorials.prime_factors(sum(xrange(1, n+1)), prime_list)
                                 

def main():
    
    start1 = time.time()
    ranges = [10]
    primes = prime.Prime()
    prime_list = primes.gen_prime_list()        
    for rangechoice in ranges:
        start1 = time.time()
        for i in xrange(rangechoice):
            factors = triangle_sums_only_primes(i,prime_list)
        end1 = time.time()
        print "Took %f seconds to complete using prime" % (end1-start1), rangechoice
                                    

if __name__=='__main__':
    main()


    
    
