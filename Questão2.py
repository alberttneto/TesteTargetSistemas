num = int(input("Informe um número: "))

def fibo(num):

    if num == 0:
        return 0
    elif num == 1:
        return 1
    else:
        return fibo(num-1) + fibo(num-2)

i = 0
while(1):
    
    if num == fibo(i):
        print("Pertence a sequencia de fibonacci") 
        break
    elif num < fibo(i):
        print("Não pertence a sequencia de fibonacci")
        break

    i += 1 