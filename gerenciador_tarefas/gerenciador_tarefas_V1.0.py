class Tarefa:

    def __init__(self,titulo,descricao,status):
        self.titulo = titulo
        self.descricao = descricao
        self.status = status

    def marcar_concluido(self,num_tarefa):
        if self.status == 'concluido':
            print('Essa tarefa já foi concluida.')
        else:
            print(f'Tarefa {lista_tarefas[num_tarefa - 1].titulo} concluida!\n')
            self.status = 'concluido'

    @classmethod
    def criar_tarefa(cls,lista_tarefas,titulo,descricao,status='pendente'):
        tarefa = Tarefa(titulo,descricao,status)
        lista_tarefas.append(tarefa)

    def remover_tarefa(self,num_tarefa):
        print(f'Tarefa {lista_tarefas[num_tarefa - 1].titulo} removida.\n')
        lista_tarefas.remove(self)\


    @staticmethod
    def adicionar_tarefa():
        titulo = input('Digite o titulo da tarefa: ')
        descricao = input('Digite a descrição da tarefa: ')
        Tarefa.criar_tarefa(lista_tarefas, titulo, descricao)
        print('Tarefa criada!\n')

    @staticmethod
    def listar_tarefas():
        if lista_tarefas == []:
            print('Não há tarefas.\n')
        else:
            print('Minhas Tarefas:\n')
            for tarefa in lista_tarefas:
                print(f'{tarefa}\n')

    @staticmethod
    def marcar_concluida():
        num_tarefa = int(input('Digite o número da tarefa que você concluiu: '))
        if num_tarefa < 1 or num_tarefa > len(lista_tarefas):
            print('Essa tarefa não existe.')
        else:
            Tarefa.marcar_concluido(lista_tarefas[num_tarefa - 1], num_tarefa)

    @staticmethod
    def tarefa_remover():
        num_tarefa = int(input('Digite o número da tarefa que você deseja remover: '))
        if num_tarefa < 1 or num_tarefa > len(lista_tarefas):
            print('Essa tarefa não existe.')
        else:
            Tarefa.remover_tarefa(lista_tarefas[num_tarefa - 1], num_tarefa)

    def __str__(self):
        return f'TAREFA {lista_tarefas.index(self)+1:02}:\nTitulo: {self.titulo}\nDescrição: {self.descricao}\nStatus: {self.status}'

lista_tarefas = []

Tarefa.criar_tarefa(lista_tarefas,'Comprar leite','Leite desnatado')
Tarefa.criar_tarefa(lista_tarefas,'Comprar pão','5 pães doces')

def iniciar():
    print('Bem vindo ao gerenciador de tarefas!\n\n1. Adicionar Tarefa \n2. Listar Tarefas\n3. Marcar Tarefa como Concluída\n4. Remover Tarefa \n5. Sair\n')
    escolha = 0
    while escolha != 5:
        escolha = int(input('Escolha uma opção: '))
        if escolha < 1 or escolha > 5:
            print('Entrada inválida, tente novamente.\n')
        else:
            if escolha == 1:
                Tarefa.adicionar_tarefa()
            else:
                if escolha == 2:
                    Tarefa.listar_tarefas()
                else:
                    if escolha == 3:
                        Tarefa.marcar_concluida()
                    else:
                        if escolha == 4:
                            Tarefa.tarefa_remover()

if __name__ == '__main__':
    iniciar()
