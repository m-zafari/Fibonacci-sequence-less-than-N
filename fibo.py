# Mohammad Zafari
# mhdzafari80@gmail.com

def fun_fibo (n):
    a=1
    b=1
    if n==1 : 
        return 0
    if n==2 :
        print(1)
        return 1
    print(f"{1}\n{1}")
    fibn=2
    sum_fibo=2
    while  fibn <= n - 1 :
        print(fibn)
        sum_fibo += fibn
        a = b
        b = fibn
        fibn = a + b
    return sum_fibo

n1 = int(input("Enter the n>0 :"))
print(f"The sum of fibo(k<{n1}):{fun_fibo(n1)} ")

