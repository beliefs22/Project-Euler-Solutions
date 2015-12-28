import factorials
import prime
def recursive_add(mylist, total = []):

    if len(mylist) == 1:
        return total
    else:
        
        return recursive_add(
            mylist[1:], total + [mylist[0]*num for num in  mylist[1:]])
def recursive_factor(num, prime_list):
    print "number is", num
    possible_primes = prime_list
    prime_factors = []
    done = False
    temp = num
    if num == 0:
        return []
    if num == 1:
        return [1]
    if num in possible_primes:
        return [1,num]
    while  temp != 1 and temp != 0:        
        for prime in possible_primes:
            print temp,prime ,"temp is prime is"
            if temp % prime == 0:
                prime_factors.append(prime)
                temp = temp/prime
                break
    return prime_factors
def main():
    number = 150000000
    p = prime.Prime()
    prime_list = p.gen_prime_list()
    prime_factors = recursive_factor(number, prime_list)
    possible_factors = list(set(recursive_add(prime_factors)))
    distinct_prime_factors = list(set(prime_factors))
    all_factors = [a*b for a in distinct_prime_factors \
                   for b in possible_factors]
    all_factors = all_factors + distinct_prime_factors+possible_factors+[1,number]
    print sorted(list(set(all_factors))), "all factors?"
    print prime_factors, distinct_prime_factors, "prime factors"
    print sorted(possible_factors), "factors found recursively"
    print sorted(list(set(recursive_add(all_factors))))


if __name__=='__main__':
    main()
        
