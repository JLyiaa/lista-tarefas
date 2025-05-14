tarefas = []

def mostrar_menu():
    print("1. adicionar tarefa")
    print("2. listar tarefas")
    print("3. remover tarefa")
    print("4. sair")

def adicionar_tarefa():
    tarefa = input("digite a tarefa: ")
    tarefas.append(tarefa)
    print(f"tarefa {tarefa} adicionada com sucesso!")

def listar_tarefa():
    if not tarefas:
        print("tarefa não encontrada")
    else:
        print("\ntarefas:")
        for i in enumerate(tarefas , 1):
            print(f"{i}.{tarefas}")

def remover_tarefa():
    listar_tarefa()
    try:
        indice = int(input("digite o numero da tarefa que deseja remover: ")) -1
        removida = tarefas.pop(indice)
        print(f"tarefa,{removida} removida")
    except (ValueError , IndexError):
        print("numero invelido, tente novamente")

while True:
    mostrar_menu()
    escolha = input("escolha opção 01-04: ")

    if escolha == "1":
        adicionar_tarefa()
    elif escolha == "2":
        listar_tarefa()
    elif escolha == "3":
        remover_tarefa()
    elif escolha == "4":
        print("saindo, até logo <3")
        break
    else:
        print("opção invalida, tente novamente")