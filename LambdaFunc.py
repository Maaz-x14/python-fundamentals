class LambdaFunc:
    def myfunc(n):
        return lambda a,b : a * n

    add = lambda a,b,c: a+b+c
    print(add(1,2,3))

    mydoubler = myfunc(2)
    print(mydoubler(11))        
