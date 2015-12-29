import prime
import recursivelist
p = prime.Prime()
p_list = p.gen_prime_list()

def test_setitem(range_size=1000, p_list=p_list ):

        for i in xrange(1,range_size):
                factors = recursivelist.factors_comb(i, p_list)

      
