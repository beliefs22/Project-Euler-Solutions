import trianglesums
import factoring
import prime

def main():
    choice = True
    p = prime.Prime()
    p_list = p.gen_prime_list()
    factor_only = raw_input("would you only like to factor? ")
    if not factor_only.lower().startswith('y'):
        while choice:
            try:  
                number = raw_input("What number shall we factor? ")
                if number == "":
                    choice = False
                else:
                    print factoring.factor(sum(xrange(int(number))), p_list)
            except OverflowError as e:
                print "Error", e, "for number: ", int(number)
    else:
        while choice:
            try:  
                number = raw_input("What number shall we factor? ")
                if number == "":
                    choice = False
                else:
                    print factoring.factor(int(number),p_list)
            except OverflowError as e:
                print "Error", e, "for number: ", int(number)



if __name__ == '__main__':
    main()
