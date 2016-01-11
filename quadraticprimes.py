import prime

def formula(a,b):
    return lambda x: x**2 + (a*x) + (b)

p = prime.Prime()

under_1000 = p.prime_generator_value(1000)
all_forms = list()
for num in under_1000:
    for pos in range(1000):
        all_forms.append((formula(pos,num),pos,num))
        all_forms.append((formula((pos*-1),num), pos*-1, num))
all_answers = list()
maxlen = 0
maxindex = 0
for index,form in enumerate(all_forms):
    i = 0
    #print "new form", form[1], form[2]
    primes = list()
    while True:        
        ans = form[0](i)
        if p.is_prime(ans):
            #print 'its prime', i
            #print ans
            primes.append(ans)
            i += 1
        else:
            #print "not prime"
            #print ans
            if len(primes) > maxlen:
                maxindex = index
                maxlen = len(primes)
            break
        
print all_forms[maxindex], maxlen

'''
Brute forced it, the only good thing was I used lambda functions to make each
possible function.
'''

        
