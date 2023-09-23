# teste

class Tarefa:

    def __init__(self,lista_tarefas,titulo,descricao,status):
        self.lista_tarefas = lista_tarefas
        self.titulo = titulo
        self.descricao = descricao
        self.status = status

    def marcar_concluido(self):
        self.status = 'concluido'

    @classmethod
    def criar_tarefa(cls,lista_tarefas,titulo,descricao,status='pendente'):
        tarefa = Tarefa(lista_tarefas,titulo,descricao,status)
        lista_tarefas.append(tarefa)

    def remover_tarefa(self):
        lista_tarefas.remove(self)

    def __str__(self):
        return f'TAREFA {lista_tarefas.index(self)+1:02}:\nTitulo: {self.titulo}\nDescrição: {self.descricao}\nStatus: {self.status}'

lista_tarefas = []

Tarefa.criar_tarefa(lista_tarefas,'Comprar leite','Leite desnatado')
Tarefa.criar_tarefa(lista_tarefas,'Comprar pão','5 pães doces')

def iniciar():
    print('Bem vindo ao gerenciador de tarefas!\n\n1. Adicionar Tarefa \n2. Listar Tarefas\n3. Marcar Tarefa como Concluída\n4. Remover Tarefa \n5. Sair\n')
    print('Teste')
    escolha = 0

    while escolha != 5:
        escolha = int(input('Escolha uma opção: '))

        if escolha < 1 or escolha > 5:
            print('Entrada inválida, tente novamente.\n')
        else:
            if escolha == 1:
                titulo = input('Digite o titulo da tarefa: ')
                descricao = input('Digite a descrição da tarefa: ')
                Tarefa.criar_tarefa(lista_tarefas,titulo,descricao)
                print('Tarefa criada!\n')
            else:
                if escolha == 2:
                    if lista_tarefas == []:
                        print('Não há tarefas.\n')
                    else:
                        print('Minhas Tarefas:\n')
                        for tarefa in lista_tarefas:
                            print(f'{tarefa}\n')
                else:
                    if escolha == 3:
                        num_tarefa = int(input('Digite o número da tarefa que você concluiu: '))
                        print(f'Tarefa {lista_tarefas[num_tarefa-1].titulo} concluida!\n')
                        Tarefa.marcar_concluido(lista_tarefas[num_tarefa-1])
                    else:
                        if escolha == 4:
                            num_tarefa = int(input('Digite o número da tarefa que você deseja remover: '))
                            print(f'Tarefa {lista_tarefas[num_tarefa-1].titulo} removida.\n')
                            Tarefa.remover_tarefa(lista_tarefas[num_tarefa-1])

iniciar()

