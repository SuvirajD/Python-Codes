def fibo_seq(num):
    a = 1
    b = 1
    for i in range(num):
        yield a                 #Using Generators
        a,b = b,a+b

x = input('Till what number do you want a Fibonacci Sequence generated?\n')
entry = int(x)

for item in fibo_seq(entry):
    print('\n')
    print(item)
