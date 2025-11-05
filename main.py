import modules.usuarios as usuarios
import modules.consultas as consultas

def exibir_menu_usuario():
      while True:
            print("==== MENU PRINCIPAL ====\n")
            print("1. Gerenciar Usuários")
            print("2. Gerenciar Consultas")
            print("0. Sair")
            opcao_principal = input("Escolha uma opção: ")

            if opcao_principal == "1":
                  menu_usuarios()
            elif opcao_principal == "2":
                  menu_consultas()
            elif opcao_principal == "0":
                  print("\n👋 Encerrando o programa...")
                  break

def menu_usuarios():
      while True:
            print("\n==== MENU USUÁRIOS ====")
            print("1. Cadastrar usuarios")
            print("2. Listar usuarios")
            print("3. Editar usuario")
            print("4. Deletar usuario")
            print("0. Retornar ao menu principal")


            opcao = input("Escolha uma opção: " )
            if opcao == "1":
                  usuarios.cadastrar_usuarios()
            elif opcao == "2":
                  usuarios.listar_usuarios()
            elif opcao == "3":
                  print("Em breve")
            elif opcao == "4":
                  print("Em breve")
            elif opcao == "0":
                  print("\nRetornando ao menu principal...")
                  break
            else:
                  print("Opção invalida")
            input("\nAperte enter para continuar...")

      return

def menu_consultas():
      while True:
            print("\n==== MENU CONSULTAS ====")
            print("1. Cadastrar consulta")
            print("2. Minhas consultas")
            print("3. Editar consulta")
            print("4. Deletar consulta")
            print("0. Retornar ao menu principal")

            opcao = int(input("Escolha uma opção: " ))
            if opcao == 1:
                  consultas.cadastrar_consulta()
            elif opcao == 2:
                  consultas.listar_consultas()
            elif opcao == 3:
                  print("Em breve")
            elif opcao == 4:
                  print("Em breve")
            elif opcao == 0:
                  print("\nRetornando ao menu principal..")
                  break
            else:
                  print("Opção invalida")

            input("\nAperte enter para continuar...")

exibir_menu_usuario()