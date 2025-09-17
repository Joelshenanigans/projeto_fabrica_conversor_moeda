# crie um codigo que faça a conversão de 

# etapas da resolução:
# 1) criar uma variavel chamada cotação
# 2) solicitar ao usuario a opção de conversão desejada
# 3) apresentar o resultado da conversão de moeda
# 4) perguntar se ele deseja continuar a conversão

letra = 's'
while letra == 's':
    cotacao = float(input('digite a cotação do dolar:'))
    print('-'*50)
    print(f'-'*15, 'escolha a opção', '-'*15)
    print('-'*50)

    opcao = int(input('1 - converter dolar para real |2 - conversor real para dolar'))

    if opcao == 1:
        valor = float(input('digite o valor em dolar a ser convertido para real U$: '))
        resultado = valor * cotacao
        print(f'o valor em reais é: {resultado:.2f}')
    elif opcao == 2:
        valor1 = float(input('digite o valor em real a ser convertido para dolar R$: '))
        resultado1 = valor1/ cotacao
        print(f'o valor em dolar é: {resultado:.2f}')
    else:
        print('digite uma opcão válida')
    letra = input('deseja continuar? (s/n): ').lower
    
 
    
    







