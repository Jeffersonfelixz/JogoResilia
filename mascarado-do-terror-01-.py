#Variaveis
personagem_a = "ELISABETH"
personagem_b = "FERNANDO"
personagem_c = "HENRIQUE"
local_a = "ESCOLA"
local_b = "PRACA"
local_c = "HOSPITAL"
vitoria_s = "NAO"
reiniciar_s = "NAO"
parar = "NAO"
restart_s = ""
#variaveis teste
teste = "R"
def restart():
    linha()
    print("Estamos fechando o jogo atual......\n")
    restart_in=input("Aperte - R - para reiniciar  :").upper()
    linha()
()
def vitoria():
    linha()
    print("Parabéns! Você foi um otimo detetive! Será que você e capaz de encontrar novas pistas em locais diferentes?, que tal começar uma nova rodada?\n"
          ". Digite NAO para Sair\n" 
          "ou Digite R para reiniciar\n") 
    linha()
    entrada_vitoria=input("Digite: ").upper()
    if entrada_vitoria == vitoria_s :
        linha()
        linha()
        print("Fim de Jogo. Esperamos que você tenha se divertido\n. "
        "Versão 0.1 : Historia,Enredo e desenvolvimento do game por Jefferson Felix")
        linha()
        linha()         
()
def reiniciar():
    linha()
    print("Infelizmente! Você não foi capaz de descobrir o culpado. que tal reiniciar o jogo e tentar novamente?\n"
          "Digite R para reiniciar ou Não para Sair") 
    linha()
    entrada_reiniciar=input("Digite: ")
    if str(entrada_reiniciar == reiniciar_s).upper() :
        print("Fechando o Jogo. Esperamos que tenha se divertido\n. "
        "Versão 0.1 : Historia,Enredo e Produção do game por Jefferson Felix")
    else:
        print("Aguarde! Estamos reiniciando o game.....\n"
              "Digite R para reiniciar")
()
def linha ():
    print("-"*80)
    print("-"*80)
()
def inicio ():
    print("-"*80)
    print ("   Diante de uma pequena Cidade do Brasil, mas conhecida por Sergipe \n"
    "   acontecia diversos casos diariamente de homicidios e crimes\n" 
    "   mas nada igual ao que estava preste acontecer...\n" 
    "   pessoas mascaradas estavam ampliando os homicidios na cidade.\n"
    "   era questão de tempo para a cidade ser dominadas por eles\n"
    "   será que você e capaz de descobrir os responsaveis pelos crimes, antes que aconteça o pior? ")
    print("-"*80)
()   
def personagem ():
    print(f"Escolha o seu personagem a seguir.\n"
    f"{personagem_a}\n"
    f"{personagem_b}\n" 
    f"{personagem_c}\n")
()
def escolha_o_local ():
    print ("Que legal! 3 informações de crimes ao mesmo tempo\n"
           "Onde devo verificar primeiro ?\n"
       f"{local_a} - {local_b}  - {local_c}  ")
()
def praca():
    print("Você prefere - INTERROGAR pessoas procurando o culpado\n" " ou \n" 
           "aguarda até a noite escondido com a policia?\n"
           "INTERROGAR? ou ESPERAR?")
    praca_1_saida = "INTERROGAR"
    praca_2_saida = "ESPERAR"
    praca_1_entrada=input("Digite :").upper()
    if praca_1_entrada == praca_1_saida:
        linha()
        print ("​- Você interrogou pessoas procurando o culpado\n" 
        "Você Interrogou Pedro\n" 
        "Obteve a informação que os culpados estava em um galpão\n"
        "ir até lá? Sim ou Não? ")
        linha()
        historia1 = "sim"
        historia1_entrada1 = input("Digite: ").lower()
        if historia1_entrada1 == historia1 :
            linha()
            print ("você prosseguiu até la com a policia e\n" 
            "viram que se tratava apenas de um galpão comum.\n"
            "perdeu apenas o seu tempo e os verdadeiros culpados foram a outro local.")
            linha()
            reiniciar()

        else:
            linha()
            restart()
            linha()            
    if praca_1_entrada == praca_2_saida:
        linha()
        print ("​- Você Aguarda até a noite escondido com a policia\n"
           "Indício de crimes acontecendo neste momento\n" 
           "esperar chegar perto de vocês para prende-los? Sim ou Não? ")
        linha()
        historia1_escolha2 = "sim"
        historia1_escolha3 = "nao"
        historia1_entrada2 = input("Digite: ").lower()
        if historia1_entrada2 == historia1_escolha2 :
            linha()
            print ("Uhuum, Prisão efetuadas. conseguimos desarticulhar a quadrilha dos Mascarados do Terror ")
            linha()
            vitoria()
        else:
            linha()
            restart()
            linha() 
() 
def escola():

    print("Estou na escola: devo procurar na Diretoria ou na Sala do Zelador\n"
         "Diretoria? ou Zelador?")
    escola_1_saida = "diretoria"
    escola_2_saida = "zelador"
    escola_1_entrada=input("Digite :").lower()

    if escola_1_entrada == escola_1_saida:
        linha()
        print ("​-Foi analizada as camera de seguranças e a pista me leva até o refeitorio?\n" 
        " Devo ir até lá? Sim ou Não? ")
        linha()
        historia2 = "sim"
        historia2_entrada1 = input("Digite :").lower()

        if historia2_entrada1 == historia2 :
            linha()
            print ("Poxa, Você foi descoberto pelos Mascarados\n"
                   "e foi capturado")
            linha()
            reiniciar()
        else:
            linha()
            restart()
            linha()        

    if escola_1_entrada == escola_2_saida:

        linha()
        print ("​- Procurei na sala do Zelador, foi descoberto\n"
           "o possivel local de reunião dos Mascarados\n" 
           "preparar a emboscada? Sim ou Não? ")
        linha()
        historia2_escolha2 = "sim"
        historia2_escolha3 = "nao"
        historia2_entrada2 = input("Digite :").lower()

        if historia2_entrada2 == historia2_escolha2 :
            linha()
            print ("Você preparou a emboscada e conseguiu, desarticular a quadrilha .")
            linha()
            vitoria()

        else:
            linha()
            restart()
            linha()        
()
def hospital():
    print("Estou no Hospital, devo interrogar a enfermeira elena ou procurar\n" 
            "na sala do medico\n"
            "Elena ou Medico")
    hospital_1_saida = "elena"
    hospital_2_saida = "medico"
    hospital_1_entrada=input("Digite :").lower()

    if hospital_1_entrada == hospital_1_saida:

        linha()
        print ("​-Elena diz que ouviu barulhos no sub-solo\n" 
        " devo ir até lá? Sim ou Não? ")
        linha()
        historia3 = "sim"
        historia3_entrada1 = input("Digite :").lower()

        if historia3_entrada1 == historia3 :
            linha()
            print ("Que pena você deu de cara com os\n"
                   "Mascarados do Terror e morreu")
            linha()
            reiniciar()
        else:
            linha()
            restart()
            linha() 

    if hospital_1_entrada == hospital_2_saida:

        linha()
        print ("​- Deseja procurar evidencias diante a ultima vitima dos mascarados ?\n")
        linha()
        historia2_escolha2 = "sim"
        historia2_entrada2 = input("Digite: ").lower()

        if historia2_entrada2 == historia2_escolha2 :
            linha()
            print ("não foram encontradas evidencias.\n"
                   "você apenas perdeu seu tempo, e eles fugiram para outro lugar")
            linha()
            reiniciar()

        else:
            linha()
            restart()
            linha()
()
while (teste):

    inicio ()
    personagem ()

    personagem_entrada = input("Escolha um personagem\n"
    "ou digite o crie o nome do seu personagem:  ").upper()

    if personagem_entrada == personagem_a :

        linha()
        print("Você escolheu: Elisabeth, 35 anos de idade. Ela é conhecida pelos seus truques medicos e por seu palpites corretos. \n")
        linha()
        escolha_o_local()
        onde= input("Onde deseja ir ? :").upper()
        linha()

        if onde == local_a:
            escola()
        if onde == local_b:
            praca()
        if onde == local_c: 
            hospital()
    if personagem_entrada == personagem_b :

        linha()
        print("Você escolheu Fernando, 21 anos de idade. Novo nas investigações, mais cheio de coragem.  \n")
        linha()
        escolha_o_local()
        onde = input("Onde deseja ir ? :").upper()
        linha()

        if onde == local_a:
            escola()
        if onde == local_b:
            praca()
        if onde == local_c: 
            hospital() 
        
    if personagem_entrada == personagem_c :

        linha()
        print("Você escolheu Henrique, 25 anos de idade. Investigador: Experiente! só que ainda tem muito a aprender \n")
        escolha_o_local()
        linha()
        onde = input("Onde deseja ir ? :").upper()
        
        if onde == local_a:
            escola()
        if onde == local_b:
            praca()
        if onde == local_c: 
            hospital()

    if personagem_entrada:
        
        idade= input("Digite sua idade:")
        faz = input("Quais são as Habilidades do seu\n" 
                    "Jogador? :")
        linha()
        print(f"Você escolheu {personagem_entrada}, {idade} anos de idade. Investigador: {faz}.\n")
        escolha_o_local()
        linha()
        onde = input("Onde deseja ir ? :").upper()
        
        if onde == local_a:
            escola()
        if onde == local_b:
            praca()
        if onde == local_c: 
            hospital()

    else:
        linha()
        linha()
        print ("Olá, alguns erros podem ter acontecido !\n"
        "Verifique se as informações digitadas, são as mesmas que e pedida no texto!\n"
        "Caso contrario, reinicie a aplicação e teste novamente. !\n"
        "Lembre-se estamos trabalhando em cima da aplicação para a melhoria!\n"
        "se foi algum erro com o codigo, fique tranquilo. em breve será corrigido !\n")
        linha()
        linha()