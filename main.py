a = int(input('digite um numero:'))
b = int(input('digite um segundo número:'))
c = int(input('digite um terceito numero:'))
if (a + b) > c and (a + c) > b and b + c > a:
    if a == b == c:
        print('Equilátero')
    elif a == b or a == c or c == b:
       print('Isósceles')  
    elif a != b or a != c or b != c:
       print('Escaleno')  
else:
    print('Não é um triângulo')          