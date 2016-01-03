def fib():

    yield 1

    yield 1
    prev1 = 1
    prev2 = 1
    while True:
        newnum = prev1 + prev2
        prev1 = prev2
        prev2 = newnum
        yield newnum
fibs = fib()
index = 1
for item in fibs:
    if len(str(item)) >= 1000:
        print item, index
        break
    index += 1

        
