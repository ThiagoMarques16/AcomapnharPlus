import modules.usuarios as usuarios

def exibir_menu_usuario():
      while True:
            print("\n==== MENU ====")
            print("1. Cadastrar usuarios")
            print("2. Listar usuarios")
            print("3. Editar usuario")
            print("4. Deletar usuario")
            print("0. Sair")

            
            try:
                  opcao = int(input("Escolha uma opção: " ))
                  if opcao == 1:
                        usuarios.cadastrar_usuarios()
                  elif opcao == 2:
                        usuarios.listar_usuarios()
                  elif opcao == 3:
                        print("Em breve")
                  elif opcao == 4:
                        print("Em breve")
                  elif opcao == 0:
                        print("\n👋 Encerrando o programa...")
                        break
                  else:
                        print("Opção invalida")

                  input("\nAperte enter para continuar...")

            except ValueError:
                  print("\nInforme uma opção valida")

exibir_menu_usuario()