a = int(input('digite um numero:'))
b = int(input('digite um segundo número:'))
c = int(input('digite um terceito numero:'))
if (a + b) < c or (a + c) < b or b + c < a:
    print('Não é um triângulo')
elif a == b == c:
    print('Equilatero')
elif a == b or a == c or c == b:
    print('Isóceles')  
elif a != b or a != c or b != c:
    print('Escaleno')     