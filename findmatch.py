import decimal
def find_match(num):
    found = False
    match = num[:5]
    for index, posmatch in enumerate(num[1:]):
        if posmatch == match[0]:
            found = (match == num[1:][index:len(match)+index])
            if found: break
            #extend match by one then repeat
        if index >= len(match) - 1: match += posmatch
    if found:
        return match
    else:
        return None

def main():
    maximum = 0
    for i in range(2,1000):
        decimal.getcontext().prec = 10000
        result = decimal.Decimal(1)/decimal.Decimal(i)
        match = find_match(str(result)[2:])
        #print result
        if match:
            if len(match) > maximum: maximum = len(match)
            print "match found at 1/%d" % (i), len(match)
    print maximum

if __name__ == '__main__':
    main()
