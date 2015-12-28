import recursivelist

def recursive_product(mylist, total = []):
    if len(mylist) == 1:
        print "finished"
        return total
    else:
        print "else ran"
        print mylist,  total
        for index in range(len(mylist)-1):
            print "new loop"
            multiple = 1
            multipliers = mylist[:index + 1]
            print multipliers, "multipliers"
            for item in multipliers:
                multiple *= item
            print multiple, "multiple is"
            for number in mylist[index + 1: ]:
                total.append(multiple*number)
        return recursive_product(mylist[1:],total)
            

def main():

    mylist = [1,5,7,7,13,17,101]
    print sorted(set(recursive_product(mylist)+mylist))
    print recursivelist.recursive_add(mylist)

if __name__=="__main__":
    main()
