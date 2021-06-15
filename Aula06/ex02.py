a = 1
num = int(input("Digite um número para saber seus divisores: "))
while a <= num:
    x = num % a
    a = a + 1
    if x == 0:
        print (a - 1)
    