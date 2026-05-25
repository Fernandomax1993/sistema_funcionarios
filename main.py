funcionarios = []

while True:
    print("\n===================================")
    print("   SISTEMA DE FUNCIONÁRIOS")
    print("===================================")

    print("1 - Cadastrar")
    print("2 - Listar")
    print("3 - Buscar")
    print("4 - Remover")
    print("5 - Sair")

    opcao = input("Escolha uma opção: ").strip()

    if opcao == "1":
        nome = input("Nome do funcionário: ").strip()
        
        if nome  == "":
            print("Nome não pode ser vazio.")
        else:
            funcionarios.append(nome)
            print("Funcionário cadastrado!")

    elif opcao == "2":
        print("\nFuncionários Cadastrados: ")

        for funcionario in funcionarios:
            print(funcionario)
        
    elif opcao == "3":
        busca = input ("Digite o nome: ").strip()

        if busca in funcionarios:
            print("Funcionário Encontrado! ")
        else:
            print("Funcionário não encontrado! ")

    elif opcao == "4":
        remover = input("Nome para remover: ").strip()
        if remover in funcionarios:
            funcionarios.remove(remover)
            print("Funcionário removido! ")
        else:
            print("Funcionário não encontrado! ")
    elif opcao == "5":
        print("Sistema encerrado. ")
        break

    else:
        print("OPÇÃO INVÁLIDA! ")
