def fibo():
    print ('Fibonacci Seqecence: ')
    a=0
    b=1
    temp=0
    i=0
    while i<13:
        print(a)
        temp=a
        a=a+b
        b=temp
fibo()