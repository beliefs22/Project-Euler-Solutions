
def brutefactor(n):
    factors = list()
    factors.append(n/2)
    factors.append(n)
    i = 1
    while i < n/2:
        if n % i == 0:
            factors.append(i)
        i += 1
    return factors

def main():
    myfile = open("1000000 factors.txt",'w')
    for i in xrange(100000):
        factors = brutefactor(i)
        if len(factors) > 500:
             myfile.write("yay!!!!!\n")
        myfile.write(str(i) + str(factors) + str(len(factors)) + "\n")
    myfile.close()
    

if __name__=='__main__':
    main()
            
