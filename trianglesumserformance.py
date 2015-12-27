import prime
import factorials
import time

def triangle_sums(n):

    return sum(range(1,n+1))

def main():
    start1 = time.time()
    primes = prime.Prime()
    total = 0
    for i in xrange(10000):
        start2 = time.time()
        result = triangle_sums(i)
        factors = factorials.factor(result,primes)
        if len(factors) > 25:
            print result, factors
        end2 = time.time()
        total += (end2 - start2)
    end1 = time.time()
    print "Took %f seconds to complete program" % (end1-start1)
    print "Took %f seconds on aveage to complete one search" %(total/100000)
    
           
        

if __name__=='__main__':
    main()


    
    
