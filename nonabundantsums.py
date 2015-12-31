from prime import Prime
from factoring import factor
def non_abundant(maxnum):
    primes = Prime()
    primes_list = primes.gen_prime_list()

    abundant_num = {}
    for num in xrange(1, maxnum):
        proper_divs = factor(num, primes_list)
        print "%d: %s" % (num, str(proper_divs))

def main():

    non_abundant(28123)

if __name__ == '__main__':
    main()
