import re
import json
import os

CAMINHO_ARQUIVO = "data/usuarios.json"


def salvar_usuario(usuarios):
      os.makedirs("data", exist_ok=True)
      with open(CAMINHO_ARQUIVO, 'w') as arquivo:
            json.dump(usuarios, arquivo, indent=4, ensure_ascii=False)

def carregar_dados():
      if os.path.exists(CAMINHO_ARQUIVO):
            with open(CAMINHO_ARQUIVO, 'r', encoding="utf-8") as arquivo:
                  return json.load(arquivo)
      
      return []

def formatar_telefone(telefone):

      telefone_limpo = re.sub(r'[^0-9]', "", telefone)
      if len(telefone_limpo) == 11:
            return f'({telefone_limpo[0:2]}) {telefone_limpo[2:7]}-{telefone_limpo[7:]}'
      else:
            return None
      
def validar_cpf(cpf, usuarios):
      cpf_limpo = re.sub(r'[^0-9]', "", cpf)

      if len(cpf_limpo) != 11 or cpf_limpo == cpf_limpo[0] * 11:
            print("❌ CPF inválido. Digite novamente.")
            return False

      nove_digitos = cpf_limpo[:9]

      soma = 0
      for i, digito in enumerate(nove_digitos):
            soma += int(digito) * (10 - i)
      primeiro_digito = (soma * 10) % 11
      primeiro_digito = 0 if primeiro_digito == 10 else primeiro_digito

      dez_digitos = nove_digitos + str(primeiro_digito)
      soma = 0
      for i, digito in enumerate(dez_digitos):
            soma += int(digito) * (11 - i)
      segundo_digito = (soma * 10) % 11
      segundo_digito = 0 if segundo_digito == 10 else segundo_digito

      cpf_validado = nove_digitos + str(primeiro_digito) + str(segundo_digito)

      if cpf_limpo != cpf_validado:
            print("❌ CPF informado não é válido.")
            return False

      for usuario in usuarios:
            if usuario["cpf"] == cpf_limpo:
                  print("⚠️ CPF já está cadastrado.")
                  return False

      return cpf_limpo


def cadastrar_usuarios():
      print("\n=== CADASTRO DE USUARIOS ===")

      while True:
            cpf = input("CPF: ")
            cpf_validado = validar_cpf(cpf, usuarios)
            if cpf_validado:
                  break
            
      nome = input("Nome Completo: ")
      
      while True: 
            telefone = formatar_telefone(input("Telefone: "))
            if telefone:
                  break
            print("Número de telefone inválido. Digite novamente")

      while True:
            telefone_emergencia = formatar_telefone(input("Telefone de emergência: "))
            if telefone_emergencia:
                  break
            print("Número de telefone inválido. Digite novamente")

      while True:
            try:
                  idade = int(input("Idade: "))
                  break
            except ValueError:
                  print("Valor informado é inválido")

      usuario = {
            'cpf': cpf_validado,
            'nome': nome,
            'telefone': telefone,
            'telefone_emergencia': telefone_emergencia,
            'idade': idade
      }

      usuarios.append(usuario)
      salvar_usuario(usuarios)
      print("Cadastro Finalizado")


def listar_usuarios():
      print("\n=== LISTA DE USUÁRIOS ===")
      for usuario in usuarios:
            print(f"\nCPF: {usuario['cpf']}")
            print(f"Nome: {usuario['nome']}")
            print(f"Idade: {usuario['idade']}")
            print(f"Contato: {usuario['telefone']}")
            print(f"Contato de Emergência: {usuario['telefone_emergencia']}")


usuarios = carregar_dados()








