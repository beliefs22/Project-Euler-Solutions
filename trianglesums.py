import prime
import factorials
import time

def triangle_sums_factors(n, primes):
    answer = sum(xrange(1,n+1))

    return answer, factorials.factor(answer, primes)

def main():
    myfile = open("primeresults.txt", 'w')
    primes = prime.Prime()
    for i in xrange(1,1000000):
        result, factors = triangle_sums_factors(i, primes)
        myfile.write("%s: %s %s %s \n" % \
                (str(i), str(result), str(factors), str(len(factors))))
        if len(factors) > 500:
            myfile.write("yay\n")

    myfile.close()
           
        

if __name__=='__main__':
    main()


    
    
