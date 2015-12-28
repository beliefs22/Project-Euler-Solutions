
def brutefactor(n):
    factors = list()
    factors.append(n)
    i = 1
    while i < n/2:
        if n % i == 0:
            factors.append(i)
        i += 1
    return factors

def brutefacor2(start,stop):
    factors = list()
    i = start
    while i < stop / 2:
        if stop % i == 0:
            factors.append(i)
        i += 1
    return factors

    

def main():
    myfile = open("1000000 factors.txt",'w')
    try:
        for i in xrange(429496729,429496730):
            factors = brutefactor(i)
            print sorted(factors), len(set(factors))
            if len(factors) > 500:
                 myfile.write("yay!!!!!\n")
            myfile.write(str(i) + str(factors) + str(len(factors)) + "\n")
    except OverflowError as e:
        print "Error", e, "for number", i
    myfile.close()
        

if __name__=='__main__':
    main()
            
