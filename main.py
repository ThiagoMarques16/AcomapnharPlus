import modules.usuarios as usuarios

while True:
      print("==== MENU ====")
      print("1. Cadastrar usuarios")
      print("2. Listar usuarios")
      opcao = int(input("Escolha uma opção: " ))

      if opcao == 1:
            usuarios.cadastrar_usuarios()
      if opcao == 2:
            usuarios.listar_usuarios()