import os 

def processo_resposta(pergunta, nome):
    if pergunta == '1':
        print(f'''{os.linesep}{nome}{os.linesep}Email do Professor Antônio: antonio.brandao@unifacs.br{os.
        linesep}Email do Professorjoberto: joberto.martins@gmail.com{os.
        linesep}Email do Professor Marcelo: marcelo.ataide@unifacs.br{os.
        linesep}Contato do Professor Eldman: https://www.eldman.com.br/contato/{os.linesep}''')
    elif pergunta == '2':
        print(f'{os.linesep}{nome} Aqui vai ficar o email da coordenação{os.linesep}')
    elif pergunta == '3':
        print(f'{os.linesep}{nome} Aqui vai ficar onde fica o boleto{os.linesep}')
    else:
        print('Digite alguma das opções: 1, 2 ou 3')
def start():
    print('Olá seja bem-vindo(a) ao BootChat!')
    print('Desenvolvido por Guilherme Santos Cabral')
#Nome aqui:
    nome = input('Por gentileza me informe seu nome: ')
#Sessão de loopin:
    while True: 
        pergunta = input(f'''######################################{os.linesep}Vamos lá, o que você quer saber hoje?{os.
        linesep}######################################{os.linesep}[1] - Email dos professores desse semestre?{os.linesep}[2] - Email para com a coordenação? {os.
        linesep}[3] - Onde posso achar o boleto?{os.linesep}''')

        processo_resposta(pergunta,nome)
#Final codigo:
if __name__ == '__main__':
    start()   