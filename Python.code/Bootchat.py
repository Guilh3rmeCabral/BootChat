import os 

def processo_resposta(pergunta, nome):
    if pergunta == '1':
        print(f'''{os.linesep}{nome}{os.linesep}Email do Professor Antônio: antonio.brandao@unifacs.br.{os.
        linesep}Email do Professor joberto: joberto.martins@gmail.com.{os.
        linesep}Email do Professor Marcelo: marcelo.ataide@unifacs.br.{os.
        linesep}Contato do Professor Eldman: https://www.eldman.com.br/contato/.{os.linesep}''')
    elif pergunta == '2':
        print(f'''{os.linesep}{nome}{os.linesep}Para atividades complementaes: ac@unifacs.br.{os.
        linesep}Para estágios: carreiras@unifacs.br.{os.linesep}Para disciplinas onlines: nead@unifacs.br.{os.
        linesep}Para os demais contate o CAE: cae@unifacs.br.{os.
        linesep}Contato por Whatsapp: 0800 284 0212.{os.linesep}Rematrícula: www.unifacs.br/rematricula.{os.linesep}''')
    elif pergunta == '3':
        print(f'''{os.linesep}{nome} Para falar com a coordenadora entre em contato através do email:{os.
        linesep}daniela.araujo@unifacs.br.{os.linesep}''')
    elif pergunta == '4':
        print(f'''{os.linesep}{nome} Primeiro acesse o portal do estudante, entre com o seu RA e sua senha,{os.
        linesep}depois de logado vai até a sessão de financeiro e clique na mesma, a seguir clique em portal financeiro.{os.linesep}''')
    else:
        print('Digite alguma das opções: 1, 2 ou 3')
def start():
    print('Olá seja bem-vindo(a) ao BootChat!')
    print('Desenvolvido por Guilherme Santos Cabral')
#Nome aqui:
    nome = input('Por gentileza me informe seu nome: ').strip()
#Sessão de loopin:
    while True: 
        pergunta = input(f'''######################################{os.linesep}Vamos lá, o que você quer saber hoje?{os.
        linesep}######################################{os.linesep}[1] - Email dos professores desse semestre?{os.
        linesep}[2] - Para falar com a coordenação? {os.
        linesep}[3] - Email para falar com a coordenadora?{os.linesep}[4] - Como faço para acessar meu boleto?{os.
        linesep}######################################{os.linesep}''').strip()

        processo_resposta(pergunta,nome)
#Final codigo:
if __name__ == '__main__':
    start()   