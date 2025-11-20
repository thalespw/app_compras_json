import os
import msvcrt

compras = {}

def limpar_tela():
    os.system('cls')

def pausar():
    print("\nPressione qualquer tecla para continuar...")
    msvcrt.getch()

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
    pass

def carregar_compras(nome_arquivo):
    pass

def gerenciar_compras(compras):
    pass


def main():
    pass

while True:
    limpar_tela()
    visualizar_compras(compras)
    opt =int(input("Digite a opção desejada:\n1. Adcionar ítem\n2. Remover ítem\n3. Visualizar lista\n4. Encerrar\n"))
    if opt == 1:
        item = input(f'Informe o nome do produto:\n')
        qtde = input(f'Informe a quantidade do produto:\n')
        adicionar_item(compras, item, qtde)
        limpar_tela() 
        print(f'{item} adicionado com sucesso.')
        pausar()
    elif opt == 2:
        item = input(f'Informe o nome do produto:\n')
        remover_item(compras,item)
        print(compras)
    if opt ==4:
        break





