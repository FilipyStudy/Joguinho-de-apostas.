import queue
import random
print("""


 ▐▄▄▄       ▄▄ •           ·▄▄▄▄  ▄▄▄ . 
  ·██▪     ▐█ ▀ ▪▪         ██▪ ██ ▀▄.▀· 
▪▄ ██ ▄█▀▄ ▄█ ▀█▄ ▄█▀▄     ▐█· ▐█▌▐▀▀▪▄ 
▐▌▐█▌▐█▌.▐▌▐█▄▪▐█▐█▌.▐▌    ██. ██ ▐█▄▄▌ 
 ▀▀▀• ▀█▄▀▪·▀▀▀▀  ▀█▄▀▪    ▀▀▀▀▀•  ▀▀▀  
 ▄▄▄·  ▄▄▄·      .▄▄ · ▄▄▄▄▄ ▄▄▄· .▄▄ · 
▐█ ▀█ ▐█ ▄█▪     ▐█ ▀. •██  ▐█ ▀█ ▐█ ▀. 
▄█▀▀█  ██▀· ▄█▀▄ ▄▀▀▀█▄ ▐█.▪▄█▀▀█ ▄▀▀▀█▄
▐█ ▪▐▌▐█▪·•▐█▌.▐▌▐█▄▪▐█ ▐█▌·▐█ ▪▐▌▐█▄▪▐█
 ▀  ▀ .▀    ▀█▄▀▪ ▀▀▀▀  ▀▀▀  ▀  ▀  ▀▀▀▀ 



Olá!
Bem vindo ao jogo de apostas!
Por breve momento, apenas as apostas contra a máquina estarão disponíveis. Peço sua compreensão. :)
Apenas números entre 1 e 10 dígitos serão permitidos!
Para jogar:
Apenas digite o número que você deseja apostar (deve ser entre 0 e 60)
Ganha o maior número :)
Good Luck :)
""")
def restricao():
   if jogador < 0:
      print('Número não permitido!')
      exit()
   elif jogador > 10**10:
      print('Número não permitido!')
      exit()
while True:
 jogador = int(float(input("Insira seu número para apostar contra a máquina: ")))
 maquina = int(random.randrange(0, 10**10))
 if jogador < 0:
    restricao()
 if jogador > 10*10:
    restricao()
 else:
    print("Você escolheu " + str(jogador))
    print("A máquina escolheu " + str(maquina))
    if jogador > maquina:
        print("Você venceu! Sua recompensa é um grande nada!!! :D")
        restart_win = input("Você deseja se arriscar denovo? ")
        if restart_win in ('S', 'Sim', 's'):
                print("Reiniciando! :D")
        else:
                print("Você que manda!")
                exit()
    elif maquina > jogador:
        print("Você perdeu! Ainda bem que não valia dinheiro ou valia? '-'")
        restart_win = input("Você deseja se arriscar denovo? ")
        if restart_win in ('S', 'Sim', 's'):
             print("Reiniciando! :D")
        elif restart_win in ('N', 'n'):
             print("Você que manda!")
             exit()
    elif maquina == jogador:
            print("Você e a maquina empataram. Uoool!!! :O")
            restart_win = input("Você deseja se arriscar denovo? ")
            if restart_win in ('N', 'nao', 'não', 'Não', 'n'):
             print("Reiniciando! :D")
            else:
             if restart_win in ('N', 'n'):
                print("Você que manda!")