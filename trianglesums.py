import prime
import factorials
import time
import recursivelist

def triangle_sums(n, primes):


    return sum(xrange(1,n+1))

def main():
    myfile = open("primeresults.txt", 'w')
    primes = prime.Prime()
    primes_list = primes.gen_prime_list()
    for i in xrange(1,1000000):
        prime_factors = recursivelist.factors(i, primes_list)
        myfile.write("%s: %s %s \n" % \
                (str(i), str(prime_factors), str(len(prime_factors))))
        if len(prime_factors) > 7:
            myfile.write("yay\n")

    myfile.close()
           
        

if __name__=='__main__':
    main()


    
    
