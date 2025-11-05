import os
import json
from datetime import datetime
from modules.usuarios import usuario_existe 

CAMINHO_ARQUIVO = "data/consultas.json"

def carregar_consultas():
      if os.path.exists(CAMINHO_ARQUIVO):
            with open(CAMINHO_ARQUIVO, 'r', encoding="utf-8") as arquivo:
                  try:
                        return json.load(arquivo)
                  except json.JSONDecodeError:
                        return []  # se o arquivo estiver vazio ou corrompido
      return []


def salvar_consultas(consultas):
      os.makedirs("data", exist_ok=True)
      with open(CAMINHO_ARQUIVO, 'w', encoding="utf-8") as arquivo:
            json.dump(consultas, arquivo, indent=4, ensure_ascii=False)


def cadastrar_consulta():
      consultas = carregar_consultas()

      cpf = input("CPF do usuário: ")
      if not usuario_existe(cpf):
            print("Usuário não encontrado. Cadastre o usuário primeiro.")
            return

      medico_responsavel = input("Médico responsável: ")
      data_consulta_str = input("Data da consulta (dd/mm/aaaa): ")
      try:
            data_consulta = datetime.strptime(data_consulta_str, "%d/%m/%Y")
      except ValueError:
            print("Data inválida! Use o formato dd/mm/aaaa.")
            return

      especialidade = input("Especialidade: ")
      observacao = input("Observação: ")

      consulta = {
            'cpf_usuario': cpf,
            'medico_reponsavel': medico_responsavel,
            'data': data_consulta.strftime("%d/%m/%Y"),
            'especialidade': especialidade,
            'observacao': observacao
      }

      consultas.append(consulta)
      salvar_consultas(consultas)
      print("Consulta agendada com sucesso!")


def listar_consultas():
      consultas = carregar_consultas()
      print("\n==== DADOS DA CONSULTA ====")

      cpf = input("CPF do usuário: ")
      if not usuario_existe(cpf):
            print("Usuário não encontrado. Cadastre o usuário primeiro.")
            return

      encontrou = False
      for consulta in consultas:
            if consulta['cpf_usuario'] == cpf:
                  encontrou = True
                  print("======================")
                  print(f"\nMédico: {consulta['medico_reponsavel']}")
                  print(f"Especialidade: {consulta['especialidade']}")
                  print(f"Data: {consulta['data']}")
                  print(f"Observação: {'Sem observação' if consulta['observacao'] == '' else consulta['observacao']}")
                  print()

      if not encontrou:
            print("Nenhuma consulta encontrada para este CPF.")
