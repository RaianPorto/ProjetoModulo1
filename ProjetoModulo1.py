##### MENU ##### MENU #### MENU #### MENU #### MENU #### MENU #### MENU #### MENU #### MENU #### MENU #####
def menuPrincipal():
    print('MENU PRINCIPAL')

    print('''
        1 - Iniciar jogo
        2 - Sobre o jogo
        0 - Finalizar Jogo
    ''')

    opcaoEscolhida = int(input('Informe a opção desejada: '))

    if opcaoEscolhida == 0:
        print('FIM DO JOGO!')
        
    elif opcaoEscolhida == 1:
        print('INICIANDO JOGO!')
        inicioDoJogo()
    elif opcaoEscolhida == 2:
        print('SOBRE O JOGO!')
        print('''
        1 - Voltar para o menu principal
        2 - Finalizar jogo
        ''')
        subMenuOpcao = int(input('Informa a opção desejada: '))
        if subMenuOpcao == 1:
            menuPrincipal()
        elif subMenuOpcao == 2:
            print('Finalizando Jogo...')
            print('Finalizado!')
        else:
            print('Opção inválida!')
    else:
        print('Você informou uma opção inválida. Escolha um número entre os indicados abaixo!')
        opcao = int(menuPrincipal())    
###########################################################################################################


def inicioDoJogo():
    print('[datadeIniciodocurso] de [mesdeInicio] de 2021')

    print('Quatro jovens buscam o mesmo objetivo: alcançar o grande conhecimento de pitão! Mas para atingir esse objetivo cada um deles enfretam diferentes problemas pessoais e precisarão da sua ajuda para conquistar o poder de pitão.')

    print('Bru - Aquela pessoa que sempre tem o hábito de deixar tudo para última hora. Uma procrastinadora nata para tudo que deveria levar mais à sério')
    print('Jonas - um jovem muito introvertido meio antisocial que possui muita dificuldade de trabalhar em equipe.') 
    print('Nat - Uma mulher independente, ocupada que precisa se disciplinar e conciliar trabalho e estudo.')

    personagem = escolhaDePersonagem()
    if personagem == 1:
        jogandoComBru()
    elif personagem == 2:
        jogandoComJonas()
    elif personagem == 3:
        jogandoComNat()
    else:
        print('Personagem Inválido. Informe um personagem válido')
        personagem = escolhaDePersonagem()

###########################################################################################################


def escolhaDePersonagem():
    print('Escolha o personagem que você quer ajudar a alcançar o conhecimento de Pitão!')

    print('''
        1 - Procastinadora Bru
        2 - Antisocial Jonas
        3 - Ocupada Nat
    ''')

    personagemEscolhido = int(input('Informe o personagem: '))
    return personagemEscolhido
###########################################################################################################


def jogandoComBru():
    print('Espero que tenha trago um guindaste porque Bru está com a preguiça do tamanho de um mamute e só assim você irá conseguir retirar Bru da cama.')
    print('Está pronto(a)? Espero que sim, vamos lá!')

    print('FASE 1 - O início do projeto?')

    # print('FASE 2 - Priorizando o que deve ser priorizado')

    # print('FASE 3 - O inesperado Pitão')

    print('''

    Faltando apenas 2 dias para a entrega do projeto, Bru percebe que precisará criar um programa simples que dará um resultado mais detalhado sobre o projeto e para a criação do projeto ela precisa ter conhecimento em uma linguagem de programação chamada Pitão.
    Ela não sabe nada sobre a linguagem.

    ''')

    # print('Fase 4 - O dia da entrega')

    

    print('''Bru posssui um projeto para entregar em uma sexta-feira, ela tem total ciencia da importância do projeto e apenas 5 dias para chegar o dia da entrega, mas para conseguir entrega-lo a tempo ela precisa encarar a procrastinação. Na noite passada Bru havia ido para uma festa mesmo sabendo que teria uma semana cheia. Ela sabe que tem que usar a semana para trabalhar no projeto logo cedo.

    [1] - Acordar bem cedo
    [2] - Dormir até tarde
    [3] - Se lamentar por ter ido para a festa.

    ''')

    resposta = input('O que Bru deve fazer? ')

    if resposta == '1':
        print('''
        Bru acordou cedo preparou o café e pensou em assistir uma série enquanto comia. Seria uma boa ideia?
        
        [1] - Assitir uma série enquanto come
        [2] - Comer sem distrações
        [3] - Deixar de tomar café para iniciar o projeto
        
        ''')

        resposta = input('O que Bru deve fazer? ')

        if resposta == 1:
            print('''
            Bru terminou a comida mas a série não. A campanhia toca e quando ela vai abrir a porta se depara com sua amiga Marisa segurando um pote de sorvete. Lembrou que havia a convidado para almoçar em sua casa.
            No momento, Bru torceu para que dentro do pote não houvesse sorvete e sim feijão pois não havia preparado nada para o almoço.
            Marisa imediatamente a cumprimenta e alerta Bru de que havia trazido a sobremesa.
            

            [1] - Pegar o sorvete e dispensar Marisa educadamente
            [2] - Honrar seu compromisso e almoçar com Marisa
            [3] - Pedir para Marisa fazer o almoço enquanto Bru trabalha no projeto.
            ''')

            resposta = input('O que Bru deve fazer?')

        elif resposta == 2:
            print('''
            Bru tomou seu café e imediatamente deu inicio ao seu projeto. Ela planejou minuciosamente tudo o que deverá fazer nos proximos dias para conseguir entregar o projeto a tempo. Por volta de 11:30h já havia produzido mais que o suficiente para um dia e pensa em parar pela tarde e voltar a adiantar o projeto pela noite. Porem, no fim da tarde, seu namorado liga convidando Bru para jantar.

            [1] - Bru aceita o convite
            [2] - Bru explica que precisa se dedicar ao projeto e 
            [3] - Bru recusa o convite
            ''')

            print('')

            print('FASE 2 - Priorizando o que deve ser priorizado')

            print('''No dia seguinte, Bru estava com vontade de ler o livro que havia ganhado de seu namorado e como havia rendido bastante no dia anterior pensou que poderia se permitir ler um pouco do livro.

            [1] - Deixar para ler o livro depois da entrega do projeto
            [2] - Ler um pouco para relaxar e voltar a pegar no projeto
            [3] - Ler o livro todo

            ''')
            resposta = input('O que Bru deve fazer?')

        elif resposta == 3:
            print('''

            
            [1] -
            [2] - 
            [3] -

            ''')
            resposta = input('O que Bru deve fazer?')
        
        else:
            print()

    elif resposta == '2':
        print('''
        Bru chegou da festa 5h da manhã e caiu de cansaço na cama. Quando acordou já era 15h e tinha apenas a noite para trabalhar no projeto.
        ''')
    
    elif resposta == '3':
        print('''
        Bru passou o dia com uma ressaca daquelas e não tinha cabeça para se concentrar no projeto.

        [1] - Tomar um banho gelado, um remedio e tentar começar o projeto.
        [2] - Tirar o dia para se recuperar da farra
        [3] - 
        ''')
    else:
        print()
###########################################################################################################


def jogandoComJonas():
    print('Então você prefere ajudar o Jonas a se inturmar e perder a timidez?')
    print('Tudo bem, boa sorte, você vai precisar!')

    print('Fase 1 - Conhecendo Jonas')





    # # Conheça seu público. Saber para quem você fala deve ser um dos primeiros passos na hora de montar sua apresentação. ...
    # # Conheça a si mesmo. ...
    # # Trace um roteiro. ...
    # # Ensaie. ...
    # # Domine o conteúdo. ...
    # # Ferramentas de suporte. ...
    # # Prepare-se para o inesperado. ...
    # # Seja flexível.

    # if resultadoFinalDoJogo == True:
    #     print('PARABÉNS!')
    # else:
    #     print('Ga..ga..ga..gaguejou, se atrapalhou e ficou travado.')
    #     print('Jonas saiu correndo do auditorio de nervosismo!')
###########################################################################################################


def jogandoComNat():
    print('Como diria Cazuza: O tempo não para, então corre para ajudar a Nat antes que o tempo acabe!')

    # Nat é uma moça que possui uma rotina muito corrida e precisa 

    # Fase 1 - 

    # resposta = input('O que Nat vai fazer?')

    # if resposta == '1':

    # elif resposta == '2':

    # elif resposta == '3': # CAMINHO MAIS CORRETO
    #     if resposta == '1':

    #     elif resposta == '2':

    #     elif resposta == '3': # CAMINHO MAIS CORRETO
    #         if resposta == '1': # CAMINHO MAIS CORRETO
    #             if resposta == '1':

    #             elif resposta == '2':

    #             elif resposta == '3': # CAMINHO MAIS CORRETO
    #                 if resposta == '1':

    #                 elif resposta == '2': # FIM DA FASE 1 <---------------------------------------

    #                 elif resposta == '3':

    #                 else:

    #             else:

    #         elif resposta == '2':

    #         elif resposta == '3': 

    #         else:

    #     else:

    # else:
    #     print()
    # FASE 2 - 

    # FASE 3 - 



    # totalPontosFase1 = 0
    # totalPontosFase2 = 0
    # totalPontosFase3 = 0

    # while totalPontosFase1 < 0.3*100:

    #     print('FASE 1 - ')

    #     print('''Fase 1.1 - 
        
    #     a) 
    #     b) 
    #     c) 
    #     d) 
    #     e) 

    #     ''')
    #     resposta = input('Resposta: ')

    #     if resposta == 'd':
    #         totalPontosFase1 += totalPontosFase1

    #     print('Fase 1.2 - ')

    #     print('Fase 1.3 - ')

    #     print('Fase 1.4 - ')

    #     print('Fase 1.5 - ')

    #     if totalPontosFase1 < 0.3*100:
    
    #         print('Triiiiiiiiim... Seu tempo acabou!')
    #         print('Você não ajudou Nat a gerir seu tempo da melhor forma.')
    #         print('Gostaria de tentar de novo?')
    #         resposta = input('Sim ou Não?')
    #         if resposta == 'Não' or 'não' or 'nao' or 'n' or 'N':
    #             print('Voltando para a seleção de personagens...')
    #             escolhaDePersonagem()
    #         else:
    #             totalPontosFase1 = totalPontosFase1

    # print('Parabéns, você concluiu a fase 1!')

    # while totalPontosFase2 < 0.5*100:

    #     print('FASE 2 - ')

    #     if totalPontosFase2 < 0.5*100:
    
    #         print('Triiiiiiiiim... Seu tempo acabou!')
    #         print('Você não ajudou Nat a gerir seu tempo da melhor forma.')
    #         print('Gostaria de tentar de novo?')
    #         resposta = input('Sim ou Não?')
    #         if resposta == 'Não' or 'não' or 'nao' or 'n' or 'N':
    #             print('Voltando para a seleção de personagens...')
    #             escolhaDePersonagem()
    #         else:
    #             totalPontosFase2 = totalPontosFase2

    # print('Parabéns, você concluiu a fase 2!')

    # while totalPontosFase3 < 0.7*100:

    #     print('FASE 3 - ')

    #     if totalPontosFase3 < 0.7*100:
    
    #         print('Triiiiiiiiim... Seu tempo acabou!')
    #         print('Você não ajudou Nat a gerir seu tempo da melhor forma.')
    #         print('Gostaria de tentar de novo?')
    #         resposta = input('Sim ou Não?')
    #         if resposta == 'Não' or 'não' or 'nao' or 'n' or 'N':
    #             print('Voltando para a seleção de personagens...')
    #             escolhaDePersonagem()
    #         else:
    #             totalPontosFase3 = totalPontosFase3

    # print('Parabéns, você conseguiu ajudar Nat a gerir o seu tempo e ainda sobrou!')

    # if resultadoFinalDoJogo == True:
    #     print('PARABÉNS!')
    # else:
    #     print('Triiiiiiiiim... Seu tempo acabou!')
    #     print('Você não ajudou Nataly a gerir seu tempo da melhor forma.')
###########################################################################################################


print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
print('Bem vindos(as) ao jogo')
print('- EM BUSCA DE PITÃO -'.center())
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')

print('INTRODUÇÃO')
print('Jovens com diferentes personalidades mais algo muito em comum, a enorme vontade de adquirir o conhecimento de Pitão. Porem, querer não é o suficiente. Vamos ajudar essas almas perdidas a obter e se tornarem os maiores especialistas em Pitão?')

menuPrincipal()


# Sábia Marisa, grande conhecedora dos ensinamentos de Pitão.

# Conselheira Taís, a maior orientadora para o caminho do autocontrole.


# resposta = input('Gostaria de tentar novamente? ')

# resposta = input('Vamos tentar novamente? ')