# using list method from bottom up approach
def fibonacci(fib_len):

    fib = [0, 1]
    for i in range(2,fib_len+1):
        fib.append(fib[-1]+fib[-2])
    
    return fib

print(fibonacci(40))

#using memoization-- relatively advanced

# def fibonacci_ad():




