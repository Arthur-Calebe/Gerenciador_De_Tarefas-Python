## Define o nome do arquivo que vamos usar para salvar as tarefas
# (Conceito de Variáveis - PDF 01)
NOME_ARQUIVO = "minhas_tarefas.txt"

def carregar_tarefas(nome_arquivo):
    """
    Tenta carregar as tarefas do arquivo de texto.
    (Conceitos de Funções - PDF 04 e Manipulação de Arquivos - PDF 07)
    """
    tarefas = [] # Cria uma lista vazia (PDF 03 e 06)
    try:
        # Tenta abrir o arquivo em modo de leitura ("r")
        # (Conceito de Arquivos 'open' - PDF 07)
        arq = open(nome_arquivo, "r")
        
        # Itera sobre cada linha do arquivo
        # (Conceito de 'for' loop - PDF 03)
        for linha in arq:
            # Adiciona a linha na lista, removendo o '\n' do final
            # (Conceito de '.append()' - PDF 06 e '.strip()' - PDF 05)
            tarefas.append(linha.strip())
        
        arq.close() # Fecha o arquivo (PDF 07)
    except FileNotFoundError:
        # Se o arquivo não existir, apenas retorna a lista vazia
        # (Isso é um tratamento de erro, um conceito importante)
        pass 
    
    return tarefas

def salvar_tarefas(nome_arquivo, tarefas):
    """
    Salva a lista de tarefas atual no arquivo de texto, sobrescrevendo o antigo.
    (Conceitos de Funções - PDF 04 e Manipulação de Arquivos - PDF 07)
    """
    # Abre o arquivo em modo de escrita ("w"), que apaga o conteúdo anterior
    # (Conceito de Arquivos 'open' modo "w" - PDF 07)
    arq = open(nome_arquivo, "w")
    
    # Itera sobre cada item na nossa lista de tarefas
    # (Conceito de 'for' loop - PDF 03)
    for tarefa in tarefas:
        # Escreve a tarefa no arquivo, adicionando um '\n' para pular linha
        # (Conceito de '.write()' - PDF 07 e Concatenação de String - PDF 05)
        arq.write(tarefa + "\n")
    
    arq.close() # Fecha o arquivo (PDF 07)
    print("Tarefas salvas com sucesso!")

def exibir_menu():
    """
    Apenas exibe o menu de opções para o usuário.
    (Conceito de Função - PDF 04 e 'print' - PDF 01)
    """
    print("\n--- Gerenciador de Tarefas ---")
    print("1. Adicionar Tarefa")
    print("2. Listar Tarefas")
    print("3. Remover Tarefa")
    print("4. Sair")

def adicionar_tarefa(tarefas):
    """
    Pede ao usuário uma nova tarefa e a adiciona na lista.
    (Conceitos de Função - PDF 04, 'input' - PDF 01, Métodos de Lista - PDF 06)
    """
    # Pede ao usuário para digitar a tarefa
    # (Conceito de 'input()' - PDF 01)
    nova_tarefa = input("Digite a nova tarefa: ")
    
    # Adiciona a tarefa na lista, removendo espaços em branco extras
    # (Conceito de '.append()' - PDF 06 e '.strip()' - PDF 05)
    tarefas.append(nova_tarefa.strip())
    print(f"Tarefa '{nova_tarefa}' adicionada!")

def listar_tarefas(tarefas):
    """
    Exibe todas as tarefas da lista, numeradas.
    (Conceitos de Função - PDF 04, 'if' - PDF 02, 'for' loop - PDF 03)
    """
    print("\n--- Suas Tarefas ---")
    
    # Verifica se a lista está vazia
    # (Conceito de 'if' - PDF 02 e 'len' - PDF 06)
    if len(tarefas) == 0:
        print("Nenhuma tarefa cadastrada.")
    else:
        # Itera usando 'range' e 'len' para obter o índice (0, 1, 2...)
        # (Conceito de 'for' e 'range' - PDF 03)
        for i in range(len(tarefas)):
            # Exibe a tarefa formatada (1., 2., 3...)
            # (Conceito de f-string - PDF 05 e Acesso à Lista [i] - PDF 06)
            print(f"{i + 1}. {tarefas[i]}")

def remover_tarefa(tarefas):
    """
    Lista as tarefas e remove a que o usuário escolher pelo número.
    (Conceitos de Função - PDF 04, 'input'/'int' - PDF 01, 'if' - PDF 02, Métodos de Lista - PDF 06)
    """
    listar_tarefas(tarefas) # Reutiliza a função de listar
    
    if len(tarefas) == 0:
        return # Sai da função se não há nada para remover
        
    try:
        # Pede ao usuário o NÚMERO da tarefa e converte para inteiro
        # (Conceito de 'input()' e 'int()' casting - PDF 01)
        num_tarefa = int(input("Digite o NÚMERO da tarefa que deseja remover: "))
        
        # Verifica se o número é válido
        # (Conceito de 'if' e operadores lógicos - PDF 02)
        if 1 <= num_tarefa <= len(tarefas):
            # Remove o item da lista pelo índice (lembrando que o índice é número-1)
            # (Conceito de '.pop()' - PDF 06)
            tarefa_removida = tarefas.pop(num_tarefa - 1)
            print(f"Tarefa '{tarefa_removida}' removida com sucesso!")
        else:
            print("Número de tarefa inválido.")
    except ValueError:
        print("Entrada inválida. Por favor, digite um número.")

def main():
    """
    Função principal que roda o programa.
    """
    # 1. Carrega as tarefas do arquivo ao iniciar
    lista_de_tarefas = carregar_tarefas(NOME_ARQUIVO)
    
    # 2. Inicia o loop principal do programa
    # (Conceito de 'while' loop - PDF 03)
    while True:
        exibir_menu() # Mostra as opções
        
        # 3. Pede a escolha do usuário
        # (Conceito de 'input()' - PDF 01)
        escolha = input("Escolha uma opção (1-4): ").strip() # ('.strip()' - PDF 05)
        
        # 4. Decide o que fazer com base na escolha
        # (Conceito de 'if/elif/else' - PDF 02)
        if escolha == "1":
            adicionar_tarefa(lista_de_tarefas)
            salvar_tarefas(NOME_ARQUIVO, lista_de_tarefas) # Salva após modificar
        
        elif escolha == "2":
            listar_tarefas(lista_de_tarefas)
        
        elif escolha == "3":
            remover_tarefa(lista_de_tarefas)
            salvar_tarefas(NOME_ARQUIVO, lista_de_tarefas) # Salva após modificar
        
        elif escolha == "4":
            print("Saindo do programa...")
            break # (Conceito de 'break' para sair do loop - PDF 03)
        
        else:
            print("Opção inválida. Por favor, tente novamente.")

# Este 'if' garante que a função 'main()' só será executada
# quando você rodar o arquivo diretamente.
if __name__ == "__main__":
    main()