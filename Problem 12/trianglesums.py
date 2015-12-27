import prime
import factorials

def triangle_sums(n):

    return sum(range(1,n+1))

def main():

   primes = prime.Prime()
   for i in xrange(100000):
       print i
       result = triangle_sums(i)
       primes = prime.Prime()
       factors = factorials.factor(result,primes)
       if len(factors) > 500:
           print result, ": ", factors
           
        

if __name__=='__main__':
    main()


    
    
