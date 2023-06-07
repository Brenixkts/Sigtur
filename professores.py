professores = {}
matricula_professor = 0 

def cadastrar_professor():
    global matricula_professor
    nome_professor = input('Nome do professor:\n').capitalize()
    materia_professor = input('Matéria quel ele leciona?:\n').capitalize()
    matricula_professor += 1
    professores[matricula_professor] = {nome_professor : materia_professor}
    for chave, valor in professores.items():
        print(chave, valor)

def editar_professor():
    pass

def mostrar_professor():
    busca_professor = int(input('Insira (1) para pesquisar um professor por matrícula e (2) para pesquisar pelo nome:\n'))
    if busca_professor == 1:
        buscar_matricula_professor = int(input('Insira a matrícula do professor:\n'))
        achar_professor = professores.get(buscar_matricula_professor)
        if achar_professor is not None: #verifica se o valor está no dicionário
            print(achar_professor)
        else:
      
            print('Professor não encontrado')
    '''
    elif busca_professor == 2:
        buscar_nome_professor = str(input('Digite o nome do professor:\n'))
        for chave, valor in professores.items():
        '''
while True:
    pergunta = int(input('Insira 1 para cadastrar e 2 para mostrar:\n'))
    if pergunta == 1:
        print(cadastrar_professor())
    elif pergunta == 2:
        mostrar_professor()