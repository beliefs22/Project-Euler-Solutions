import prime
import factorials
import time

def triangle_sums(n):

    return sum(range(1,n+1))

def main():
    primes = prime.Prime()
   for i in xrange(100000):
       
       result = triangle_sums(i)
       factors = factorials.factor(result,primes)
       if len(factors) > 500:
           print i, "--", result, ": ", factors
           break
           
        

if __name__=='__main__':
    main()


    
    
