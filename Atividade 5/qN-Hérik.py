#ATIVIDADE AULA 5
op = int(input("Bom dia! digite qual exercício de 1 a 10 que você deseja observar: "))

#Exercício 1:
if op == 1:
    r = float(input("Digite o valor de R: "))
    p = 3.14159
    A = p * (r ** 2)
    print("A = {:.4f}".format(A)) 

#Exercício 2:    
if op == 2:
    n1 = float(input("Digite a primeira nota: "))
    n2 = float(input("Digite a segunda nota: "))
    n3 = float(input("Digite a terceira nota: "))

    r1 = n1 * 2
    r2 = n2 * 3
    r3 = n3 * 5
    res = (r1 + r2 + r3)/10
    print("MÉDIA = {:.1f}".format(res))

#Exercício 3:
if op == 3:
    km = int(input("Digite a distância percorrida em km: "))
    lit = float(input("Digite em litros quanto de combustível foi consumido: "))
    res = km / lit
    print("A média de consumo foi {:.3f} km/l.".format(res))

#Exercício 4:    
if op == 4:
    x1 = float(input("Digite o valor de x1:"))
    y1 = float(input("Digite o valor de y1: "))
    x2 = float(input("Digite o valor de x2: "))
    y2 = float(input("Digite o valor de y2: "))
    dis = ((x2 - x1)**2 + (y2 - y1)**2)**(1/2)
    print("O resultado é: {:.4f}".format(dis)) 

#Exercício 5:
if op == 5:
    a = int(input("Digite o primeiro valor: "))
    b = int(input("Digite o segundo valor: "))
    c = int(input("Digite o terceiro valor: "))

    ab = (a + b + abs(a-b))/2
    c = (ab + c + abs(ab-c))/2
    print("{:.0f} é o maior".format(c))

#Exercício 6:
if op == 6:
    n1 = int(input("Digite o valor do primeiro número: "))
    n2 = int(input("Digite o valor do segundo número: "))

    res = n2 % n1 

    if res == 0:
        print("Sim")
    else:
        print("Não")

#Exercício 7:
if op == 7:
    sal = float(input("Digite o valor do seu salário: "))

    aum1 = (sal / 100) * 20
    aum2 = (sal / 100) * 15

    res3 = sal + aum1
    res4 = sal + aum2

    if sal <= 1212.00:
        print("{:.2f}".format(res3))

    if sal > 1212.00:
        print("{:.2f}".format(res4))

#Exercício 8:
if op == 8:
    n1 = float(input("Digite a primeira nota: "))
    n2 = float(input("Digite a segunda nota: "))

    med = (n1 + n2) / 2

    if med <= 3.0:
        print("Reprovado!")

    if med >= 3.0 and med < 7.0: 
        print('Exame!')

    else:
        print("Aprovado")

#Exercício 9:
if op == 9:
    a = int(input("Digite o primeiro valor: "))
    b = int(input("Digite o segundo valor: "))
    c = int(input("Digite o terceiro valor: "))

    ab = (a + b + abs(a-b))/2
    c = (ab + c + abs(ab-c))/2
    print("{:.0f}".format(c))

#Exercício 10
if op == 10:
    n1 = float(input("Digite o primeiro número: "))
    n2 = float(input("Digite o segundo número: "))
    esc = int(input("Digite uma das 3 opções: "))

    res1 = n1**n2
    res2 = n1**2 + n2**2
    res3 = (n1**(1/2)) + (n2**(1/2))

    if esc == 1:
        print("{:.1f}".format(res1))
    elif esc == 2:
        print("{:.1f}".format(res2))  
    elif esc == 3:
        print("{:.1f}".format(res3))              	
    else:
        print("ERRO") 