import os
import msvcrt
import json
import time

compras = {'caneta':2,'lapis':4}

def limpar_tela():
    os.system('cls')

def pausar():
    print("\nPressione qualquer tecla para continuar...")
    msvcrt.getch()
    limpar_buffer()

def limpar_buffer():
    while msvcrt.kbhit():  # Verifica se há teclas no buffer
        msvcrt.getch()     # Remove a tecla do buffer

def adicionar_item(compras, item, qtde):
    compras[item] = qtde  

def remover_item(compras, item):
    while True:
        if item in compras:
            del compras[item]
        print("Ítem não encontrado")

def visualizar_compras(compras):
    for item,quantidade in compras.items():
        print(f'{item}: {quantidade}')

def salvar_compras(compras, nome_arquivo):
    with open(nome_arquivo.json,'w') as file:
        json.dump(compras, file)

def carregar_compras(nome_arquivo):
    with open(nome_arquivo,'r') as file:
        return json.load(file)
        
def gerenciar_compras(compras):
    while True:
        limpar_tela()
        opt_compras =int(input("1.Adicionar Ítem\n2.Remover Ítem\n3.salvar e sair\n4.Sair sem salvar\n"))
        if opt_compras == 1:
            item = input(f'Informe o nome do produto:\n')
            qtde = input(f'Informe a quantidade do produto:\n')
            adicionar_item(compras, item, qtde)
            limpar_tela() 
            print(f'{item} adicionado com sucesso.')
            pausar()
        elif opt_compras == 2:
            item = input(f'Informe o nome do produto:\n')
            remover_item(compras,item)
            print(compras)
        elif opt_compras == 3:
            nome_arquivo = input('Informe o nome da lista de compras:\n')
            salvar_compras(compras,nome_arquivo)
        elif opt_compras == 4:
            break
        else:
            print('Opção Inválida')
            time.sleep(1)

def main():
    while True:
        limpar_tela()
        opt =int(input("1.Abrir Lista\n2.Criar Lista\n3.Excluir Lista\n4.Sair\n"))
        if opt == 1:
            abrir_lista = input('Digite o nome da lista:\n')
            carregar_compras(abrir_lista)
        elif opt==2:
            gerenciar_compras(compras)
        elif opt==3:
            pass
        elif opt ==4:
            break
        else:
            print('Opção Inválida')
            time.sleep(1)
            limpar_buffer()

main()





