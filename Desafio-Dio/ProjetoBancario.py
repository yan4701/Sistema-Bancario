#Construindo o Menu  
menu = '''  
\n Escolha uma opção:\n  
[1] - Depositar  
[2] - Sacar  
[3] - Extrato  
[4] - Sair  
\n Insira o número da opção desejada: '''  

# Iniciando as Variáveis  
saldo = 0  
limite = 500  
extrato = []  
qntd_saques = 0  
LIMITE_SAQUES = 3  

# Definindo Parâmetros  
while True:  
    opcao = input(menu)  
    
    if opcao == '1':  
        valor = float(input("Informe o valor do depósito: "))  
        
        if valor > 0:  
            saldo += valor  
            extrato.append(f"Depósito: R$ {valor:.2f}") 
            print("Depósito realizado com sucesso!")  
        else:  
            print("Operação não realizada! O valor informado é inválido.")  
    
    elif opcao == '2': 
        valor = float(input("Informe o valor do saque: "))  
        excedeu_saldo = valor > saldo  
        excedeu_limite = valor > limite  
        excedeu_saques = qntd_saques >= LIMITE_SAQUES  

        if excedeu_saldo:  
            print("Operação não realizada! Saldo insuficiente, verifique o saldo da sua conta.")  

        elif excedeu_limite:  
            print("Operação não realizada! O valor do saque excede o valor limite de saque.")  

        elif excedeu_saques:  
            print("Operação não realizada! Você excedeu a quantidade limite de saques.")  
        
        elif valor > 0:
            saldo -= valor  
            extrato.append(f"Saque: R$ {valor:.2f}")  
            qntd_saques += 1  
            print("Saque realizado com sucesso!")  
        else:  
            print("Operação não realizada! O valor informado é inválido.")  

    elif opcao == '3':  
        print("Extrato da conta: ")  
        if not extrato:  
            print("Não há movimentações registradas.")  
        else:  
            for operação in extrato:  
                print(operação)  
        print(f"Saldo atual: R$ {saldo:.2f}")  

    elif opcao == '4':  
        print("Saindo do sistema... Obrigado por utilizar nosso serviço.")
        break  

    else:
        print("Opção inválida! Por favor, selecione uma opção válida.")