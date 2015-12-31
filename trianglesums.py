#Found all factors of a number using prime numbers and recursively generating
#All factors using Prime factors (combinations yay)
import prime
import recursivelist

def triangle_sum(n):

    return sum(xrange(1,n+1))

def main():
    primes = prime.Prime()
    primes_list = primes.gen_prime_list()
    for i in xrange(1,1000000):
        all_factors, prime_facts = recursivelist.factors_comb(i, primes_list)
        print "%s: %s %s %s %s\n" % \
              (str(i), str(prime_facts),str(all_factors),
               str(len(prime_facts)), str(len(all_factors)))
        if len(all_factors )> 499:
            print "yay\n"
            
if __name__=='__main__':
    main()


    
    
