import json
import os
from modules.usuarios import usuario_existe
from datetime import datetime


CAMINHO_ARQUIVO = "data/consultas.json"

def carregar_consultas():
      if os.path.exists(CAMINHO_ARQUIVO):
            with open(CAMINHO_ARQUIVO, 'r', encoding="utf-8") as arquivo:
                  return arquivo
            
      return []


def salvar_consulta(consulta):
      os.makedirs("data", exist_ok=True)
      with open(CAMINHO_ARQUIVO, 'w') as arquivo:
            json.dump(consulta, arquivo, indent=4, ensure_ascii=False)

def cadastrar_consulta():

      cpf = input("CPF do usuário: ")
      if not usuario_existe(cpf):
            print("Usuario não encontrado. Cadastre o usuário primeiro.")

            return
      medico_responsavel = input("Médico responsável: ")
      data_consulta_str = input("Data da consulta (dd/mm/aaaa): ")
      try:
            data_consulta = datetime.strptime(data_consulta_str, "%d/%m/%Y")
      except ValueError:
            print("Data inválida! Use o formato dd/mm/aaaa.")
      especialidade = input("Especialidade: ")
      observacao = input("Observação: ")

      consulta = {
            'cpf_usuario': cpf,
            'medico_reponsavel': medico_responsavel,
            'data': data_consulta.strftime("%d/%m/%Y"),
            'especialidade': especialidade,
            'observacao': observacao
      }

      salvar_consulta(consulta)
      print("Consulta agendada.")



consultas = carregar_consultas()
