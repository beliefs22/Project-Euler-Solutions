import trianglesums
import factorials
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
                    print trianglesums.triangle_sums_factors(int(number),p)
            except OverflowError as e:
                print "Error", e, "for number: ", int(number)
    else:
        while choice:
            try:  
                number = raw_input("What number shall we factor? ")
                if number == "":
                    choice = False
                else:
                    print factorials.prime_factors(int(number),p_list)
            except OverflowError as e:
                print "Error", e, "for number: ", int(number)



if __name__ == '__main__':
    main()
