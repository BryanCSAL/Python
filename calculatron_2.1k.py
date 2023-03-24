
def somar(x,y):
    z = x + y
    print(x,'+',y,'=',z)

def subtrair(x,y):
    z = x - y
    print(x,'-',y,'=',z)

def multiplicar(x,y):
    z = x * y
    print(x,'x',y,'=',z)

def elevar(x,y):
    z = x ** y
    print(x,'^',y,'=',z)

def dividir(x,y):
    z = x / y
    print(x,'÷',y,'=',z)

while True:
    try:
        num1 = float(input("Insira o primeiro valor: "))
        break
    except ValueError:
        print("Valor desconhecido, insira um número!")
        continue
print("O primeiro valor é: ",num1)

while True:
    try:
        num2 = float(input("Insira o segundo valor: "))
        break
    except ValueError:
        print("Valor desconhecido, insira um número!")
        continue
print("O segundo valor é: ",num2)

while True:
    operacao = input('Escolha o tipo de operação | + | - | / | ^ | X |: ')
    
    if operacao == '-':
        print('A operação escolhida foi: -')
        print('')
        subtrair(num1,num2)    
        break

    elif operacao == '+':
        print('A operação escolhida foi: +')
        print('')
        somar(num1,num2)   
        break
    
    elif operacao == '/':
        print('A operação escolhida foi: /')
        print('')
        dividir(num1,num2)   
        break

    elif operacao == '^':
        print('A operação escolhida foi: ^')
        print('')
        elevar(num1,num2)   
        break
    
    elif operacao == 'x':
        print('A operação escolhida foi: X')
        print('')
        multiplicar(num1,num2)   
        break

    else:
        print('Apenas operações são aceitas!')






