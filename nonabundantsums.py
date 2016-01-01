from prime import Prime
from factoring import factor
from itertools import combinations
import time
def non_abundant(maxnum):
    primes = Prime()
    primes_list = primes.gen_prime_list()

    abundant_num = {}
    non_abundant_sums = {}
    all_sums = list()
    for num in xrange(1, maxnum+1):
        proper_divs = factor(num, primes_list)#find facors
        sums = sum(proper_divs)#sum of factors
        abundant = (sums > num)
        if abundant:
            abundant_num[num] = abundant_num.get(num,0) + 1
            all_sums.append(num*2)
        #print "%d: divs = %s sum of dis = %d abundant = %s" \
              #% (num, str(proper_divs),sums, abundant)
    all_sums = all_sums + \
               [sum(comb) for comb in combinations(abundant_num.keys(),2) \
                 if sum(comb) < maxnum+1]
    all_sums = set(all_sums)
    
    for i in xrange(1,maxnum+1):
        non_abundant_sums[i] = (i in all_sums)
    print len(abundant_num), len(all_sums), len(set(all_sums)),len(non_abundant_sums)
    print sum([num for num in non_abundant_sums if not non_abundant_sums[num]])
    

    

def main():

    non_abundant(28123)

if __name__ == '__main__':
    start = time.time()
    main()
    end = time.time()
    print "Took %f seconds to find all sums" % (end-start)
